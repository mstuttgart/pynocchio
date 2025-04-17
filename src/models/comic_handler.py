from PySide6.QtGui import QPixmap

from src.models.comic import Comic
from src.models.page import Page


class ComicHandler:
    """Base class for handling comic pages."""

    def __init__(self, comic: Comic, index: int = 0):
        """
        Initialize the ComicHandler.

        Args:
            comic (Comic): The comic object containing pages.
            index (int, optional): The starting page index. Defaults to 0.
        """
        self._comic: Comic = comic
        self._currentPageIndex: int = index
        self._currentPageImage: QPixmap = QPixmap()

    def getComic(self) -> Comic:
        """
        Get the comic object.

        Returns:
            Comic: The comic object.
        """
        return self._comic

    def setComic(self, comic: Comic) -> None:
        """
        Set the comic object.

        Args:
            comic (Comic): The new comic object.
        """
        self._comic = comic

    def getCurrentPageCount(self) -> int:
        """
        Get the total number of pages in the comic.

        Returns:
            int: The total number of pages.
        """
        return len(self._comic.getPages())

    def getCurrentPageIndex(self) -> int:
        """
        Get the current page index.

        Returns:
            int: The current page index.
        """
        return self._currentPageIndex

    def getCurrentPageNumber(self) -> int:
        """
        Get the current page number.

        Returns:
            int: The current page number.
        """
        return self._currentPageIndex + 1

    def setCurrentPageIndex(self, idx: int):
        """
        Set the current page index.

        Args:
            idx (int): The new page index.
        """
        if 0 <= idx < self._comic.getPageCount():
            self._currentPageIndex = idx

    def getCurrentPage(self) -> Page:
        """
        Get the current page.

        Returns:
            Page: The current page object.
        """
        return self._comic.getPages()[self._currentPageIndex]

    def goNextPage(self) -> None:
        """
        Go to the next page.

        Raises:
            NotImplementedError: Must be implemented in a subclass.
        """
        raise NotImplementedError("Must subclass me!")

    def goPreviousPage(self) -> None:
        """
        Go to the previous page.

        Raises:
            NotImplementedError: Must be implemented in a subclass.
        """
        raise NotImplementedError("Must subclass me!")

    def goFirstPage(self) -> None:
        """
        Go to the first page.
        """
        self.setCurrentPageIndex(0)

    def goLastPage(self) -> None:
        """
        Go to the last page.
        """
        self.setCurrentPageIndex(len(self._comic.getPages()) - 1)

    def getCurrentPageImage(self) -> QPixmap:
        """
        Get the image of the current page.

        Raises:
            NotImplementedError: Must be implemented in a subclass.
        """
        raise NotImplementedError("Must subclass me!")

    def isLastPage(self) -> bool:
        """
        Check if the current page is the last page.

        Returns:
            bool: True if it's the last page, False otherwise.
        """
        return self._currentPageIndex == len(self._comic.getPages()) - 1

    def isFirstPage(self) -> bool:
        """
        Check if the current page is the first page.

        Returns:
            bool: True if it's the first page, False otherwise.
        """
        return self._currentPageIndex == 0
