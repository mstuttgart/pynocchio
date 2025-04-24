import logging

from src.models.comic_loader import ComicLoader
from src.models.comic_loader_pdf import ComicPdfLoader
from src.models.comic_loader_rar import ComicRarLoader, is_rarfile
from src.models.comic_loader_tar import ComicTarLoader, is_tarfile
from src.models.comic_loader_zip import ComicZipLoader, is_zipfile
from src.models.constants import LOGGING_VERBOSITY, SUPPORTED_FILES
from src.models.utils import getFileExtension

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


class ComicLoaderFactory:
    """
    Factory class to create appropriate comic file loaders based on file type.
    """

    @staticmethod
    def createLoader(filename: str) -> ComicLoader:
        """
        Creates and returns the appropriate loader for the given comic file.

        Args:
            filename (str): The path to the comic file.

        Returns:
            ComicLoader: An instance of the appropriate loader class.

        Raises:
            TypeError: If the file format is not supported.
        """
        file_extension = getFileExtension(filename)

        if file_extension not in SUPPORTED_FILES:
            logger.error(f"Unsupported file format: {file_extension}")
            raise TypeError(f"Unsupported file format: {file_extension}")

        if file_extension == ".pdf":
            logger.info("Creating PDF loader")
            return ComicPdfLoader(filename)

        if is_zipfile(filename):
            logger.info("Creating ZIP loader")
            return ComicZipLoader(filename)

        if is_rarfile(filename):
            logger.info("Creating RAR loader")
            return ComicRarLoader(filename)

        if is_tarfile(filename):
            logger.info("Creating TAR loader")
            return ComicTarLoader(filename)

        logger.error(f"Unsupported file type: {file_extension}")
        raise TypeError(f"Unsupported file type: {file_extension}")
