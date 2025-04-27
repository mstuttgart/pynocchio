import logging
from typing import TYPE_CHECKING, Any, Optional, Union

from PySide6.QtCore import QObject, QThreadPool, QUrl, Signal, Slot
from PySide6.QtGui import QDesktopServices, QPixmap

from src.models.comic_loader_factory import ComicLoaderFactory
from src.models.constants import HELP_URL
from src.models.main_model import MainModel

if TYPE_CHECKING:
    from src.models.comic_loader import ComicLoader

logger = logging.getLogger(__name__)


class MainController(QObject):
    """
    Main controller for the application.

    This class serves as the intermediary between the model and the view.
    It handles user interactions and updates the view accordingly.
    """

    # Signals
    updateCentralWidgetContentSignal = Signal(QPixmap, int)
    updatePageBoxSignal = Signal(int, int)
    updateWindowTitleSignal = Signal(str)
    closeMainWindowSignal = Signal()
    updatePageActionsSignal = Signal(bool, bool)
    loadProgressSignal = Signal(int)
    startProgressSignal = Signal(int)
    doneProgressSignal = Signal()
    errorLoadSignal = Signal(str)
    finishProgressSignal = Signal()

    def __init__(self, model: MainModel) -> None:
        """
        Initializes the MainController.

        Args:
            model (MainModel): The model instance to be controlled.
        """
        super().__init__()
        self._mainModel: MainModel = model
        self._loader: Union[None, ComicLoader] = None
        self.threadpool: Union[None, QThreadPool] = None

    def updateCentralWidgetContent(self) -> None:
        """
        Updates the central widget content with the current page image and rotation angle.
        """
        comicHandler = self._mainModel.getComicHandler()
        if comicHandler:
            self.updateCentralWidgetContentSignal.emit(
                comicHandler.getCurrentPageImage(),
                self._mainModel.getPageRotateAngle(),
            )

    def updatePageBox(self) -> None:
        """
        Updates the page box in the main window view with the current page number and total pages.
        """
        comicHandler = self._mainModel.getComicHandler()
        if comicHandler:
            self.updatePageBoxSignal.emit(
                comicHandler.getCurrentPageIndex() + 1, comicHandler.getCurrentPageCount()
            )

    def getCurrentFitMode(self) -> str:
        """
        Returns the current fit page mode.

        Returns:
            str: The current fit page mode.
        """
        return self._mainModel.getCurrentFitMode()

    def getCurrentComicPath(self) -> str:
        """
        Gets the current comic path.

        Returns:
            str: The current comic path.
        """
        return self._mainModel.getCurrentComicPath()

    def getPreviousComicPath(self) -> Optional[str]:
        """
        Gets the path to the previous comic.

        Returns:
            Optional[str]: The path to the previous comic, or None if unavailable.
        """
        return self._mainModel.getPreviousComicPath()

    def getNextComicPath(self) -> Optional[str]:
        """
        Gets the path to the next comic.

        Returns:
            Optional[str]: The path to the next comic, or None if unavailable.
        """
        return self._mainModel.getNextComicPath()

    def _loadComic(self, filename: str) -> None:
        """
        Loads a comic file and initializes the loader.

        This method creates a loader for the specified comic file and starts it
        in a separate thread using QThreadPool. Signals from the loader are connected
        to the appropriate slots to handle progress updates and completion.

        Args:
            filename (str): The path to the comic file to be loaded.
        """
        logger.info("Loading comic file: %s", filename)
        self._loader = ComicLoaderFactory.createLoader(filename)

        # Connect signals
        self._loader.getSignals().startProgressSignal.connect(self.startProgressSignal.emit)
        self._loader.getSignals().loadProgressSignal.connect(self.loadProgressSignal.emit)
        self._loader.getSignals().doneProgressSignal.connect(self.onDoneProgress)
        self._loader.getSignals().errorLoadSignal.connect(self.errorLoadSignal.emit)
        self._loader.getSignals().finishProgressSignal.connect(self.finishProgressSignal.emit)

        self.threadpool = QThreadPool()
        self.threadpool.start(self._loader)

    @Slot()
    def onFinishProgress(self) -> None:
        """
        Handles the finish progress signal when the comic loading process is completed.
        """
        logger.info("Finish progress signal emitted")
        self._loader = None
        self.threadpool = None
        self.finishProgressSignal.emit()

    @Slot(str, list)
    def onDoneProgress(self, filename: str, data: list[Any]) -> None:
        """
        Handles the completion of the comic loading process.

        Args:
            filename (str): The name of the loaded file.
            data (list): The loaded data.
        """
        logger.info("Finished loading comic: %s", filename)
        comic = self._mainModel.loadComic(filename, data)
        comicHandler = self._mainModel.getComicHandler()

        if comicHandler:
            self.updatePageBox()
            self.updateCentralWidgetContent()
            self.updateWindowTitleSignal.emit(comic.getFilename())
            self.doneProgressSignal.emit()
            self.updatePageActionsSignal.emit(
                comicHandler.isFirstPage(),
                comicHandler.isLastPage(),
            )
        else:
            logger.error("Failed to load comic file: %s", filename)

    @Slot()
    def onActionReportBugTriggered(self) -> None:
        """
        Opens the default web browser to the application's issue tracker URL.
        """
        logger.info("Report a Bug action triggered")
        QDesktopServices.openUrl(QUrl(HELP_URL))

    @Slot()
    def onActionPreviousPageTriggered(self) -> None:
        """
        Navigates to the previous page of the comic and updates the view.
        """
        logger.info("Previous Page action triggered")
        comicHandler = self._mainModel.getComicHandler()

        if comicHandler:
            comicHandler.goPreviousPage()
            self.updateCentralWidgetContent()
            self.updatePageBox()
            self.updatePageActionsSignal.emit(comicHandler.isFirstPage(), comicHandler.isLastPage())

    @Slot()
    def onActionNextPageTriggered(self) -> None:
        """
        Navigates to the next page of the comic and updates the view.
        """
        logger.info("Next Page action triggered")
        comicHandler = self._mainModel.getComicHandler()

        if comicHandler:
            comicHandler.goNextPage()
            self.updateCentralWidgetContent()
            self.updatePageBox()
            self.updatePageActionsSignal.emit(comicHandler.isFirstPage(), comicHandler.isLastPage())

    @Slot()
    def onActionFirstPageTriggered(self) -> None:
        """
        Navigates to the first page of the comic and updates the view.
        """
        logger.info("First Page action triggered")
        comicHandler = self._mainModel.getComicHandler()

        if comicHandler:
            comicHandler.goFirstPage()
            self.updateCentralWidgetContent()
            self.updatePageBox()
            self.updatePageActionsSignal.emit(comicHandler.isFirstPage(), comicHandler.isLastPage())

    @Slot()
    def onActionLastPageTriggered(self) -> None:
        """
        Navigates to the last page of the comic and updates the view.
        """
        logger.info("Last Page action triggered")
        comicHandler = self._mainModel.getComicHandler()

        if comicHandler:
            comicHandler.goLastPage()
            self.updateCentralWidgetContent()
            self.updatePageBox()
            self.updatePageActionsSignal.emit(comicHandler.isFirstPage(), comicHandler.isLastPage())

    @Slot()
    def onActionPreviousComicTriggered(self) -> None:
        """
        Loads the previous comic if available.
        """
        logger.info("Previous Comic action triggered")
        previousComicPath = self._mainModel.getPreviousComicPath()
        if previousComicPath:
            self._loadComic(previousComicPath)
        else:
            logger.warning("No previous comic available")

    @Slot()
    def onActionNextComicTriggered(self) -> None:
        """
        Loads the next comic if available.
        """
        logger.info("Next Comic action triggered")
        nextComicPath = self._mainModel.getNextComicPath()

        if nextComicPath:
            self._loadComic(nextComicPath)
        else:
            logger.warning("No next comic available")

    @Slot()
    def onPageSpinBoxValueChanged(self, value: int) -> None:
        """
        Navigates to the specified page number.

        Args:
            value (int): The page number to navigate to.
        """
        logger.info("Go To Page action triggered")
        comicHandler = self._mainModel.getComicHandler()

        if comicHandler:
            comicHandler.setCurrentPageIndex(value - 1)
            self.updateCentralWidgetContent()

    @Slot()
    def onActionFitGroupTriggered(self, actionFitObjectName: str) -> None:
        """
        Adjusts the view to fit the comic based on the specified fit mode.

        Args:
            actionFitObjectName (str): The name of the fit mode action.
        """
        logger.info("Fit action triggered: %s", actionFitObjectName)

        if self._mainModel.getComic():
            self._mainModel.setCurrentFitMode(actionFitObjectName)
            self.updateCentralWidgetContent()

    @Slot()
    def onActionRotateLeftTriggered(self) -> None:
        """
        Rotates the comic view to the left.
        """
        logger.info("Rotate Left action triggered")

        if self._mainModel.getComic():
            self._mainModel.rotatePageLeft()
            self.updateCentralWidgetContent()

    @Slot()
    def onActionRotateRightTriggered(self) -> None:
        """
        Rotates the comic view to the right.
        """
        logger.info("Rotate Right action triggered")

        if self._mainModel.getComic():
            self._mainModel.rotatePageRight()
            self.updateCentralWidgetContent()

    def saveData(self) -> None:
        """
        Saves the current data to the settings manager.
        """
        logger.info("Saving data")
        self._mainModel.saveData()
