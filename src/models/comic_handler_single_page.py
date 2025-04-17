from PySide6.QtGui import QPixmap

from src.models.comic_handler import ComicHandler


class ComicHandlerSinglePage(ComicHandler):
    """
    Handler for single-page comic navigation.
    """

    def goNextPage(self) -> None:
        """
        Go to the next page.
        """
        self.setCurrentPageIndex(self._currentPageIndex + 1)

    def goPreviousPage(self) -> None:
        """
        Go to the previous page.
        """
        self.setCurrentPageIndex(self._currentPageIndex - 1)

    def getCurrentPageImage(self) -> QPixmap:
        """
        Get the image of the current page.

        Returns:
            QPixmap: The pixmap of the current page.
        """
        return self.getCurrentPage().getPixmap()
