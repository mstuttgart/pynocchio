import logging
import os

from src.models.constants import LOGGING_VERBOSITY
from src.models.page import Page

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


class Comic:
    """
    This is basic class of Pynocchio. Represents a comic object
    """

    def __init__(self, filename: str, directory: str) -> None:
        """
        Comic class __init__ method

        Args:
            filename (str): comic filename
            directory (str): comic file directory
        """
        self._filename: str = filename
        self._directory: str = directory

        # list of Page: list to store the comic pages objects
        self._pages: list[Page] = []

    def setFilename(self, filename: str) -> None:
        """
        Set comic filename.

        Args:
            filename (str): The filename to set.
        """
        self._filename = filename

    def getFilename(self) -> str:
        """
        Get comic filename.

        Returns:
            str: The return value. Represents comic filename.
        """
        return self._filename

    def setDirectory(self, directory: str) -> None:
        """
        Set comic directory.

        Args:
            directory (str): The directory to set.
        """
        self._directory = directory

    def getDirectory(self) -> str:
        """
        Get comic directory.

        Returns:
            str: The return value. Represents comic directory.
        """
        return self._directory

    def setPages(self, pages: list[Page]) -> None:
        """
        Set comic pages.

        Args:
            pages (list[Page]): The pages to set.
        """
        self._pages = pages

    def getPages(self) -> list[Page]:
        """
        Get comic pages.

        Returns:
            list[Page]: The return value. Represents comic pages.
        """
        return self._pages

    def getComicPath(self) -> str:
        """
        Get comic path.

        Returns:
            str: The return value. Represents comic path.
        """
        return os.path.join(self._directory, self._filename)

    def getPageCount(self) -> int:
        """
        Get the number of pages in the comic.

        Returns:
            int: The number of pages in the comic.
        """
        return len(self._pages)
