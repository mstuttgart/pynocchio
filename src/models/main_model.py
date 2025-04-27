import logging
import os
from typing import Optional

from PySide6.QtCore import QDir, QObject, QSettings

from src.models import reading_list_model
from src.models.comic import Comic
from src.models.comic_handler import ComicHandler
from src.models.comic_handler_single_page import ComicHandlerSinglePage
from src.models.constants import COMPACT_FILE_FORMATS, LOGGING_VERBOSITY
from src.models.utils import getBaseName, getDirName

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


class MainModel(QObject):
    """
    Model class for the application.

    This class serves as the data model for the application, managing the
    application's state and providing methods to manipulate that state.
    It communicates with the controller to update the view when the model
    changes.
    """

    def __init__(self) -> None:
        """
        Initializes the MainModel.
        """
        logger.info("Initializing MainModel")
        super().__init__()

        self._comic: Optional[Comic] = None
        self._comicPageHandler: Optional[ComicHandler] = None
        self._settings = QSettings()
        self._pageRotateAngle: int = 0
        self._currentComicPath: str = ""
        self._currentFitMode: str = ""
        self._previousComicName: Optional[str] = None
        self._nextComicName: Optional[str] = None

        self.loadData()
        logger.info("MainModel initialized")

    def setComic(self, comic: Comic) -> None:
        """
        Sets the comic object.

        Args:
            comic (Comic): The comic object to set.
        """
        self._comic = comic

    def getComic(self) -> Optional[Comic]:
        """
        Gets the comic object.

        Returns:
            Optional[Comic]: The comic object, or None if not set.
        """
        return self._comic

    def setComicHandler(self, handler: ComicHandler) -> None:
        """
        Sets the comic handler.

        Args:
            handler (ComicHandler): The comic handler to set.
        """
        self._comicPageHandler = handler

    def getComicHandler(self) -> Optional[ComicHandler]:
        """
        Gets the comic handler.

        Returns:
            Optional[ComicHandler]: The comic handler, or None if not set.
        """
        return self._comicPageHandler

    def setCurrentComicPath(self, comic_path: str) -> None:
        """
        Sets the current comic path.

        Args:
            comic_path (str): The comic path to set.
        """
        self._currentComicPath = comic_path

    def getCurrentComicPath(self) -> str:
        """
        Gets the current comic path.

        Returns:
            str: The current comic path.
        """
        return self._currentComicPath

    def setCurrentFitMode(self, fit_mode: str) -> None:
        """
        Sets the current fit mode.

        Args:
            fit_mode (str): The fit mode to set.
        """
        self._currentFitMode = fit_mode

    def getCurrentFitMode(self) -> str:
        """
        Gets the current fit mode.

        Returns:
            str: The current fit mode.
        """
        return self._currentFitMode

    def loadComic(self, comicPath: str, data: list) -> Comic:
        """
        Loads a comic file, initializes the comic model, and updates the view.

        Args:
            comicPath (str): The path to the comic file to be loaded.
            data (list): The list of pages in the comic.

        Returns:
            Comic: The loaded comic object.

        Raises:
            Exception: If an error occurs during the loading process.
        """
        if self._comic and self._comicPageHandler:
            self.saveReadingList()

        self._comic = Comic(getBaseName(comicPath), getDirName(comicPath))
        self._comic.setPages(data)

        initialIndex = reading_list_model.getLastComicPage(comicPath) or 0
        self._comicPageHandler = ComicHandlerSinglePage(self._comic, initialIndex)

        self._previousComicName, self._nextComicName = self._getComicsInPath(
            self._comic.getDirectory(), self._comic.getFilename()
        )

        logger.info("Loading %s at page %d", comicPath, (initialIndex) + 1)
        return self._comic

    def _getComicsInPath(self, path: str, filename: str) -> tuple[Optional[str], Optional[str]]:
        """
        Gets the previous and next comic files in the specified path.

        Args:
            path (str): The directory path to search for comic files.
            filename (str): The current comic filename.

        Returns:
            tuple[Optional[str], Optional[str]]: A tuple containing the previous and next comic filenames.
        """
        logger.debug("Getting comic files in path: %s", path)

        qDir = QDir(path)
        qDir.setFilter(QDir.Filter.Files | QDir.Filter.NoDotAndDotDot)
        qDir.setSorting(QDir.SortFlag.Name)
        qDir.setNameFilters([f"*{ext}" for ext in COMPACT_FILE_FORMATS])

        entryList = qDir.entryList()
        logger.debug("Found comic files: %s", entryList)

        if not entryList:
            logger.warning("No comic files found in path: %s", path)
            return None, None

        try:
            currentComicIndex = entryList.index(filename)
        except ValueError:
            logger.warning("Current comic not found in path: %s", path)
            return None, None

        previousComicPath = entryList[currentComicIndex - 1] if currentComicIndex > 0 else None
        nextComicPath = (
            entryList[currentComicIndex + 1] if currentComicIndex < len(entryList) - 1 else None
        )

        logger.debug("Previous comic path: %s", previousComicPath)
        logger.debug("Next comic path: %s", nextComicPath)

        return previousComicPath, nextComicPath

    def rotatePageLeft(self) -> None:
        """
        Rotates the current page 90 degrees to the left (counterclockwise).
        """
        self._pageRotateAngle = (self._pageRotateAngle - 90) % 360

    def rotatePageRight(self) -> None:
        """
        Rotates the current page 90 degrees to the right (clockwise).
        """
        self._pageRotateAngle = (self._pageRotateAngle + 90) % 360

    def getPageRotateAngle(self) -> int:
        """
        Gets the current rotation angle of the page.

        Returns:
            int: The current rotation angle of the page.
        """
        return self._pageRotateAngle

    def getPreviousComicPath(self) -> Optional[str]:
        """
        Gets the path to the previous comic.

        Returns:
            Optional[str]: The path to the previous comic, or None if not available.
        """
        return (
            os.path.join(self._currentComicPath, self._previousComicName)
            if self._previousComicName
            else None
        )

    def getNextComicPath(self) -> Optional[str]:
        """
        Gets the path to the next comic.

        Returns:
            Optional[str]: The path to the next comic, or None if not available.
        """
        return (
            os.path.join(self._currentComicPath, self._nextComicName)
            if self._nextComicName
            else None
        )

    def loadData(self) -> None:
        """
        Loads data from the settings manager.
        """
        logger.info("Loading settings")
        self._currentComicPath = str(self._settings.value("currentComicPath", ""))
        self._currentFitMode = str(self._settings.value("currentFitMode", ""))
        logger.info("All settings loaded")

    def saveData(self) -> None:
        """
        Saves data to the settings manager.
        """
        logger.info("Saving settings")
        self._settings.setValue("currentComicPath", self._currentComicPath)
        self._settings.setValue("currentFitMode", self._currentFitMode)
        self.saveReadingList()
        logger.info("All settings saved")

    def saveReadingList(self) -> None:
        """
        Saves the reading list to the database.
        """
        logger.info("Saving reading list")
        if self._comic and self._comicPageHandler:
            reading_list_model.addEntry(
                self._comic.getFilename(),
                self._comic.getComicPath(),
                self._comicPageHandler.getCurrentPageIndex(),
            )
        logger.info("Reading list saved successfully")
