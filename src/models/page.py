import logging

from PySide6.QtGui import QImage, QPixmap

from src.models.constants import LOGGING_VERBOSITY

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


class Page:
    """
    This is basic class of Pynocchio. Represents a comic page object
    """

    def __init__(self, data: bytes, title: str, number: int):
        """
        Comic Page class __init__ method

        Args:
            data (bin): comic page binary data
            title (str): page title
            number (int): page number
        """
        self._data: bytes = data
        self._title: str = title
        self._number: int = number
        self._pixmap: QPixmap = QPixmap()

    def getPixmap(self):
        """
        Get page pixmap.

        Returns:
            None: The return value. Represents page pixmap.
        """

        if self._pixmap.isNull():
            # Create a QImage from the binary data
            # and convert it to a QPixmap
            image = QImage()

            logger.debug("Loading image from data")

            if image.loadFromData(self._data):
                self._pixmap = QPixmap.fromImage(image)
                logger.debug("Image loaded successfully")
            else:
                logger.error("Failed to load image from data")

        return self._pixmap

    def getTitle(self) -> str:
        """
        Get page title.

        Returns:
            str: The return value. Represents page title.
        """
        return self._title

    def setTitle(self, title: str) -> None:
        """
        Set page title.

        Args:
            title (str): The title to set.
        """
        self._title = title

    def getNumber(self) -> int:
        """
        Get page number.

        Returns:
            int: The return value. Represents page number.
        """
        return self._number

    def getData(self) -> bytes:
        """
        Get page data.

        Returns:
            bytes: The return value. Represents page data.
        """
        return self._data
