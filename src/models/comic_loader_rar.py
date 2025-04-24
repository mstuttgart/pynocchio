import logging
import threading

import rarfile

from src.models.comic_loader import ComicLoader
from src.models.constants import IMAGE_FILE_FORMATS, LOGGING_VERBOSITY
from src.models.page import Page
from src.models.utils import getFileExtension

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


def is_rarfile(filename):
    """
    Verify if file is a rar file.

    Args:
        filename (str): Name of the file.

    Returns:
        bool: True if the file is a rar file, otherwise False.
    """
    return rarfile.is_rarfile(filename)


class ComicRarLoader(ComicLoader):
    """
    Comic RAR file loader class.
    This class is responsible for loading RAR files and creating Page
    objects with them. It inherits from the ComicLoader class and
    implements the load method to read RAR files.
    """

    def load(self, filename: str) -> None:
        """
        This method reads the contents of a RAR file, processes each file within the archive,
        and creates Page objects for valid image files. The loading process is performed
        using multiple threads to improve performance.

        Raises:
            ValueError: If the RAR file cannot be read, contains no valid pages, or if an error
            occurs during the loading process.

        Notes:
            - The method emits progress signals during the loading process:
              `startProgressSignal` is emitted with the total number of files to process,
              and `loadProgressSignal` is emitted after each file is processed.
            - Only files with extensions matching `IMAGE_FILE_FORMATS` are processed as pages.
            - Pages are sorted by their page number after loading.
        """

        logger.info("Attempting to load file: %s", filename)

        if not is_rarfile(filename):
            logger.error("The file %s is not a valid RAR file.", filename)
            raise TypeError(f"The file '{filename}' is not a valid RAR file.")

        try:
            with rarfile.RarFile(filename, "r") as rar:
                # Get the list of files in the RAR archive
                namelist: list[str] = sorted(rar.namelist())

                # Emit the start progress signal with the number of files
                self.getSignals().startProgressSignal.emit(len(namelist) - 1)

                def readRarFileThread(name: str, number: int) -> None:
                    """Thread function to read RAR file contents.
                    Args:
                        name (str): Name of the file in the RAR archive.
                        number (int): Page number.
                    """

                    if getFileExtension(name).lower() in IMAGE_FILE_FORMATS:
                        logger.debug("Adding page: %s", name)

                        try:
                            self._data.append(Page(rar.read(name), name, number))

                        except rarfile.BadRarFile as exc:
                            logger.error("Error reading RAR file '%s': %s", name, exc)

                        except Exception as exc:
                            logger.error("Other error reading RAR file %s: %s", name, exc)

                # Create a list to hold the threads
                threads = []

                # Start threads to read each file in the RAR archive
                for pageNumber, name in enumerate(namelist, start=1):
                    logger.debug("Processing file: %s", name)

                    thread = threading.Thread(target=readRarFileThread, args=(name, pageNumber))
                    threads.append(thread)
                    thread.start()

                # Wait for all threads to finish
                for index, thread in enumerate(threads):
                    thread.join()
                    self.getSignals().loadProgressSignal.emit(index)

                # Sort the pages by their number
                self._data.sort(key=lambda x: x.getNumber())

        except rarfile.Error as exc:
            logger.exception("Failed to load RAR file '%s': %s", filename, exc)
            raise ValueError(f"Failed to load RAR file '{filename}'.") from exc

        if not self._data:
            logger.error("No valid data found in the RAR file: %s", filename)
            raise ValueError("No valid data found in the RAR file.")

        logger.info("Successfully loaded %d pages from %s", len(self._data), filename)
