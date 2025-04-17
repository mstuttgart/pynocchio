import logging
import tarfile
import threading

from src.models.comic_loader import ComicLoader
from src.models.constants import IMAGE_FILE_FORMATS, LOGGING_VERBOSITY
from src.models.page import Page
from src.models.utils import getFileExtension

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


def is_tarfile(filename: str) -> bool:
    """
    Verify if file is tar file

    Args:
        filename: name of file

    Returns: True if file is a tar file otherwise, False

    """
    return tarfile.is_tarfile(filename)


class TarFile(tarfile.TarFile):
    """
    A subclass of tarfile.TarFile that provides additional utility methods
    for reading files and retrieving file names from a TAR archive.
    """

    def read(self, filename: str) -> bytes:
        """
        Read the contents of a file within the TAR archive.

        Args:
            filename (str): The name of the file to read from the TAR archive.

        Returns:
            bytes: The binary data of the specified file.

        Raises:
            KeyError: If the specified file is not found in the TAR archive.
            tarfile.ExtractError: If there is an error extracting the file.
        """
        file = self.extractfile(filename)
        if file is None:
            raise KeyError(f"File '{filename}' not found in the TAR archive.")
        return file.read()

    def namelist(self) -> list[str]:
        """
        Retrieve the list of file names contained in the TAR archive.

        Returns:
            list[str]: A list of file names present in the TAR archive.
        """
        return self.getnames()


class ComicTarLoader(ComicLoader):
    """
    Comic TAR file loader class.
    This class is responsible for loading TAR files and creating Page
    objects with them. It inherits from the ComicLoader class and
    implements the load method to read TAR files.
    """

    def load(self, filename: str) -> None:
        """
        This method reads the contents of a TAR file, processes each file within the archive,
        and creates Page objects for valid image files. The loading process is performed
        using multiple threads to improve performance.

        Raises:
            ValueError: If the TAR file cannot be read, contains no valid pages, or if an error
            occurs during the loading process.

        Notes:
            - The method emits progress signals during the loading process:
              `startProgressSignal` is emitted with the total number of files to process,
              and `loadProgressSignal` is emitted after each file is processed.
            - Only files with extensions matching `IMAGE_FILE_FORMATS` are processed as pages.
            - Pages are sorted by their page number after loading.
        """
        logger.info("Attempting to load file: %s", filename)

        if not is_tarfile(filename):
            logger.error("The file %s is not a valid TAR file.", filename)
            raise TypeError(f"The file '{filename}' is not a valid TAR file.")

        try:
            with TarFile(filename, "r") as tar:
                # Get the list of files in the TAR archive
                namelist: list[str] = sorted(tar.namelist())

                # Emit the start progress signal with the number of files
                self.getSignals().startProgressSignal.emit(len(namelist) - 1)

                def readTarFileThread(name: str, number: int) -> None:
                    """Thread function to read TAR file contents.
                    Args:
                        name (str): Name of the file in the TAR archive.
                        number (int): Page number.
                    """

                    if getFileExtension(name).lower() in IMAGE_FILE_FORMATS:
                        logger.debug("Adding page: %s", name)

                        try:
                            page_data = tar.read(name)
                            self._data.append(Page(page_data, name, number))

                        except tarfile.ExtractError as exc:
                            logger.error("Error reading TAR file %s: %s", name, exc)

                        except Exception as exc:
                            logger.error("Other error reading TAR file %s: %s", name, exc)

                # Create a list to hold the threads
                threads = []

                # Start threads to read each file in the TAR archive
                for pageNumber, name in enumerate(namelist, start=1):
                    logger.debug("Processing file: %s", name)

                    thread = threading.Thread(target=readTarFileThread, args=(name, pageNumber))
                    threads.append(thread)
                    thread.start()

                # Wait for all threads to finish
                for index, thread in enumerate(threads):
                    thread.join()
                    self.getSignals().loadProgressSignal.emit(index)

                # Sort the pages by their number
                self._data.sort(key=lambda x: x.getNumber())

        except tarfile.ReadError as exc:
            logger.exception("Failed to load TAR file %s: %s", filename, exc)
            raise ValueError(f"Failed to load TAR file {filename}: {exc}")

        if not self._data:
            logger.error("No valid data found in the TAR file: %s", filename)
            raise ValueError("No valid data found in the TAR file.")

        logger.info("Successfully loaded %d pages from %s", len(self._data), filename)
