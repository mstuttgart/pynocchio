import logging
import threading
import zipfile

from src.models.comic_loader import ComicLoader
from src.models.constants import IMAGE_FILE_FORMATS, LOGGING_VERBOSITY
from src.models.page import Page
from src.models.utils import getFileExtension

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


def is_zipfile(filename: str) -> bool:
    """
    Verify if a file is a ZIP file.

    Args:
        filename (str): Name of the file.

    Returns:
        bool: True if the file is a ZIP file, otherwise False.
    """
    return zipfile.is_zipfile(filename)


class ComicZipLoader(ComicLoader):
    """
    Comic ZIP file loader class.
    This class is responsible for loading ZIP files and creating Page
    objects with them. It inherits from the ComicLoader class and
    implements the load method to read ZIP files.
    """

    def load(self, filename: str) -> None:
        """
        This method reads the contents of a ZIP file, processes each file within the archive,
        and creates Page objects for valid image files. The loading process is performed
        using multiple threads to improve performance.

        Raises:
            ValueError: If the ZIP file cannot be read, contains no valid pages, or if an error
            occurs during the loading process.

        Notes:
            - The method emits progress signals during the loading process:
              `startProgressSignal` is emitted with the total number of files to process,
              and `loadProgressSignal` is emitted after each file is processed.
            - Only files with extensions matching `IMAGE_FILE_FORMATS` are processed as pages.
            - Pages are sorted by their page number after loading.
        """
        logger.info("Attempting to load file: %s", filename)

        if not is_zipfile(filename):
            logger.error("The file %s is not a valid ZIP file.", filename)
            raise TypeError(f"The file '{filename}' is not a valid ZIP file.")

        try:
            with zipfile.ZipFile(filename, "r") as zf:
                # Get the list of files in the ZIP archive
                namelist: list[str] = sorted(zf.namelist())

                # Emit the start progress signal with the number of files
                self.getSignals().startProgressSignal.emit(len(namelist) - 1)

                def readZipFileThread(name: str, number: int) -> None:
                    """Thread function to read ZIP file contents.
                    This function is executed in a separate thread to
                    read the contents of a ZIP file and create Page
                    objects from image files.

                    Args:
                        name (str): Name of the file in the ZIP archive.
                        number (int): Page number for the image.
                    """

                    if getFileExtension(name).lower() in IMAGE_FILE_FORMATS:
                        logger.debug("Adding page: %s", name)

                        try:
                            page_data = zf.read(name)
                            self._data.append(Page(page_data, name, number))

                            logger.debug("Page %d loaded successfully.", number)

                        except zipfile.BadZipfile as exc:
                            logger.error("Error reading ZIP file %s: %s", name, exc)

                        except Exception as exc:
                            logger.error("Other error reading ZIP file %s: %s", name, exc)

                # Create a list to hold the threads
                threads = []

                # Start threads to read each file in the RAR archive
                for pageNumber, name in enumerate(namelist, start=1):
                    logger.debug("Processing file: %s", name)

                    thread = threading.Thread(target=readZipFileThread, args=(name, pageNumber))
                    threads.append(thread)
                    thread.start()

                # Wait for all threads to finish
                for index, thread in enumerate(threads):
                    thread.join()
                    self.getSignals().loadProgressSignal.emit(index)

                # Sort the pages by their number
                self._data.sort(key=lambda x: x.getNumber())

        except zipfile.BadZipfile as exc:
            logger.exception("Failed to load ZIP file %s: %s", filename, exc)
            raise ValueError(f"Failed to load ZIP file {filename}: {exc}")

        if not self._data:
            logger.error("No valid data found in the ZIP file: %s", filename)
            raise ValueError("No valid data found in the ZIP file.")

        logger.info("Successfully loaded %d pages from %s", len(self._data), filename)
