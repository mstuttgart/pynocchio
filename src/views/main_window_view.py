import enum
import logging
import sys
from typing import TYPE_CHECKING, Any, Callable, Union

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import (
    QAction,
    QActionGroup,
    QIcon,
    QKeySequence,
    QPixmap,
    QShortcut,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressDialog,
    QSizePolicy,
    QSpinBox,
    QToolBar,
    QVBoxLayout,
    QWidget,
)
from qt_material_icons import MaterialIcon

from src.models.constants import APP_NAME, COPYRIGHT, LICENSE_URL, VERSION
from src.widgets.qscroll_area_viewer import QScrollAreaViewer

if TYPE_CHECKING:
    from PySide6.QtGui import QCloseEvent

    from src.controllers.main_controller import MainController

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MainWindowView(QMainWindow):
    """
    Main application window.

    This class represents the main window of the application, setting its
    title and initial geometry.

    Attributes:
        _mainController (MainController): Reference to the main controller instance.
        _toolBar (QToolBar): The toolbar for the main window.
        _centralWidget (QWidget): The central widget to hold the main content.
        _centralWidgetLayout (QVBoxLayout): Layout for the central widget.
        _centralWidgetScrollArea (QScrollAreaViewer): Scroll area for the central content.
        _centralWidgetLabel (QLabel): Label to display content within the central widget.
        _globalShortcuts (list): List to store global shortcuts for the application.
        _pageSpinbox (QSpinBox): Spinbox for page navigation.
        _progressDialog (Union[QProgressDialog, None]): Progress dialog used during loading operations.
        _actionExit (QAction): Action for exiting the application.
        _actionOpenFile (QAction): Action for opening a file.
        _actionPreviousPage (QAction): Action for navigating to the previous page.
        _actionNextPage (QAction): Action for navigating to the next page.
        _actionFirstPage (QAction): Action for navigating to the first page.
        _actionLastPage (QAction): Action for navigating to the last page.
        _actionPreviousComic (QAction): Action for navigating to the previous comic.
        _actionNextComic (QAction): Action for navigating to the next comic.
        _actionFitVertical (QAction): Action for fitting content vertically.
        _actionFitHorizontal (QAction): Action for fitting content horizontally.
        _actionFitOriginal (QAction): Action for fitting content to its original size.
        _actionFitPage (QAction): Action for fitting content to the page.
        _actionRotateLeft (QAction): Action for rotating content to the left.
        _actionRotateRight (QAction): Action for rotating content to the right.
        _actionAbout (QAction): Action for displaying the "About" dialog.
        _actionReportBug (QAction): Action for reporting a bug.

    Methods:
        _setupUI(): Sets up the user interface components.
        _setupGlobalShortcuts(): Configures global shortcuts for the application.
        _setupPageSpinbox(): Configures the page spinbox for navigation.
        _setupActions(): Sets up actions for the menu bar and toolbar.
        _setupToolBar(): Configures the toolbar with actions and layout.
        _setupCentralWidget(): Sets up the central widget to display content.
        _connectSignals(): Connects signals to their respective slots.
    """

    class FitPage(enum.Enum):
        """
        Enum representing different fit options for a page view.

        Attributes:
            FITVERTICAL (str): Option to fit the content vertically within the view.
            FITHORIZONTAL (str): Option to fit the content horizontally within the view.
            FITORIGINAL (str): Option to display the content in its original size.
            FITPAGE (str): Option to fit the entire content within the view.
        """

        FITVERTICAL = "actionFitVertical"
        FITHORIZONTAL = "actionFitHorizontal"
        FITORIGINAL = "actionFitOriginal"
        FITPAGE = "actionFitPage"

    def __init__(self, MainController: "MainController") -> None:
        """
        Initializes the MainWindowView.

        Args:
            MainController (MainController): The main controller instance responsible for managing the application's logic.
        """

        logger.info("Initializing MainWindowView")

        super().__init__()
        self.setObjectName("mainWindow")

        # Initialize the main controller
        self._mainController: "MainController" = MainController

        # Create the toolbar for the main window
        self._toolBar: QToolBar = QToolBar(self)

        # Create a QWidget to hold the central content
        self._centralWidget: QWidget = QWidget()
        self._centralWidgetLayout: QVBoxLayout = QVBoxLayout(self._centralWidget)

        # Create a QScrollArea to enable scrolling for the central content
        self._centralWidgetScrollArea: QScrollAreaViewer = QScrollAreaViewer(self)

        # Create a QLabel to display content within the central widget
        self._centralWidgetLabel: QLabel = QLabel(self._centralWidget)

        # List to store global shortcuts for the application
        self._globalShortcuts = []

        # Create a QSpinBox for page navigation
        self._pageSpinbox: QSpinBox = QSpinBox(self)

        # Initialize the progress dialog (used during loading operations)
        self._progressDialog: Union[QProgressDialog, None] = None

        # Define QAction instances for various actions in the application
        self._actionExit: QAction = QAction(self)
        self._actionOpenFile: QAction = QAction(self)
        self._actionPreviousPage: QAction = QAction(self)
        self._actionNextPage: QAction = QAction(self)
        self._actionFirstPage: QAction = QAction(self)
        self._actionLastPage: QAction = QAction(self)
        self._actionPreviousComic: QAction = QAction(self)
        self._actionNextComic: QAction = QAction(self)
        self._actionFitVertical: QAction = QAction(self)
        self._actionFitHorizontal: QAction = QAction(self)
        self._actionFitOriginal: QAction = QAction(self)
        self._actionFitPage: QAction = QAction(self)
        self._actionRotateLeft: QAction = QAction(self)
        self._actionRotateRight: QAction = QAction(self)
        self._actionAbout: QAction = QAction(self)
        self._actionReportBug: QAction = QAction(self)

        # Set up the user interface components
        self._setupUI()

        # Set up global shortcuts for the application
        self._setupGlobalShortcuts()

        # Configure the page spinbox for page navigation
        self._setupPageSpinbox()

        # Set up actions for the menu bar and toolbar
        self._setupActions()

        # Configure the toolbar with actions and layout
        self._setupToolBar()

        # Set up the central widget to display content
        self._setupCentralWidget()

        # Connect signals to their respective slots
        self._connectSignals()

    def _connectSignals(self) -> None:
        """
        Connects signals from the main controller and central widget to their respective slots.
        """
        # Connect the signal to update the central widget content
        self._mainController.updateCentralWidgetContentSignal.connect(
            self.updateCentralWidgetContent
        )

        # Connect the resized signal of the scroll area to trigger content update
        self._centralWidgetScrollArea.resizedSignal.connect(
            self._mainController.updateCentralWidgetContent
        )

        # Connect the signal to update the page spinbox
        self._mainController.updatePageBoxSignal.connect(self.updatePageBox)

        # Connect the signal to update the window title
        self._mainController.updateWindowTitleSignal.connect(self.updateWindowTitle)

        # Connect the signal to close the main window
        self._mainController.closeMainWindowSignal.connect(self.close)

        # Connect the signal to update the status of page navigation actions
        self._mainController.updatePageActionsSignal.connect(self.updatePageActionsStatus)

        # Connect the signal to handle the start of a progress operation
        self._mainController.startProgressSignal.connect(self.onStartProgress)

        # Connect the signal to handle the completion of a loading operation
        self._mainController.doneProgressSignal.connect(self.onDoneProgress)

        # Connect the signal to handle errors during the loading process
        self._mainController.errorLoadSignal.connect(self.onErrorLoad)

        # Connect the signal to handle the finalization of a progress operation
        self._mainController.finishProgressSignal.connect(self.onFinishProgress)

    def _setupUI(self) -> None:
        """
        Initializes the window.

        This method sets the window's size, minimum size, title, icon, and
        position. It also handles platform-specific behavior for macOS.
        """
        logger.info("Setting up UI")

        # Get the device pixel ratio for scaling purposes
        r: float = self.devicePixelRatioF()

        # Get the available geometry of the primary screen
        desktop = QApplication.primaryScreen().availableGeometry()

        # Get the width and height of the screen
        w: int = desktop.width()
        h: int = desktop.height()

        # Resize the main window based on a proportion of the screen size
        self.resize(int(w * 1240 / 1920), int(h * 970 / 1080))

        # Set the minimum size of the window based on the screen size and pixel ratio
        self.setMinimumSize(int(w * r * 1030 / 1920), int(h * r * 780 / 1080))

        # Set the window title
        self.setWindowTitle(self.tr(APP_NAME))

        # Set the window icon
        self.setWindowIcon(QIcon(":/logo.ico"))

        # Center the window on the screen
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        # Show the main window
        self.show()

        # Enable unified title and toolbar on macOS for a consistent appearance
        if sys.platform == "darwin":
            self.setUnifiedTitleAndToolBarOnMac(True)

    def _setupPageSpinbox(self) -> None:
        """
        Configures the page spinbox.

        This method sets up the spinbox to display and allow navigation
        between pages. It also connects the spinbox's value change signal
        to the corresponding controller slot.
        """
        logger.debug("Setting up page spinbox")

        self._pageSpinbox.setSingleStep(1)
        self._pageSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._pageSpinbox.setToolTip(self.tr("Page Number"))
        self._pageSpinbox.setStatusTip(self.tr("Page Number"))

        # Connect spinbox value change to controller
        self._pageSpinbox.valueChanged.connect(self._mainController.onPageSpinBoxValueChanged)

    def _createAction(
        self,
        iconName: str,
        text: str,
        objectName: str,
        shortcut: str,
        slot: Callable[[], Any],
        checkable=False,
        enable=True,
    ) -> QAction:
        """
        Creates and returns a QAction with the specified properties.

        Args:
            iconName (str): The name of the icon to be used for the action.
            text (str): The display text for the action.
            objectName (str): The unique object name for the action.
            shortcut (str): The keyboard shortcut for triggering the action.
            slot (Callable[[], Any]): The function to be called when the action is triggered.
            checkable (bool, optional): Indicates if the action is checkable. Defaults to False.
            enable (bool, optional): Indicates if the action is enabled. Defaults to True.

        Returns:
            QAction: The configured QAction instance.
        """

        action = QAction(self)
        action.setIcon(MaterialIcon(iconName))
        action.setObjectName(objectName)
        action.setText(self.tr(text))
        action.setCheckable(checkable)
        action.setEnabled(enable)

        if slot:
            action.triggered.connect(slot)

        if shortcut:
            action.setToolTip(self.tr(f"{text} ({shortcut})"))
            action.setShortcut(self.tr(shortcut))

        return action

    def _setupActions(self) -> None:
        """
        Configures the actions for the menu bar and toolbar.

        This method initializes all actions, sets their icons, tooltips,
        shortcuts, and connects them to their respective slots.
        """
        logger.debug("Setting up actions for the menu bar")

        # Exit action
        self._actionExit = self._createAction(
            iconName="close",
            text="&Exit",
            objectName="actionExit",
            shortcut="Ctrl+Q",
            slot=self.close,
        )

        # Open File action
        self._actionOpenFile = self._createAction(
            iconName="file_open",
            text="&Open File",
            objectName="actionOpenFile",
            shortcut="Ctrl+O",
            slot=self.onActionOpenFileTriggered,
        )

        # Navigation actions
        self._setupNavigationActions()

        # Fit actions
        self._setupFitActions()

        # Rotate actions
        self._setupRotateActions()

        # About action
        self._actionAbout = self._createAction(
            iconName="info",
            text="&About",
            objectName="actionAbout",
            shortcut="F1",
            slot=self.onActionAboutTriggered,
        )

        # Report Bug action
        self._actionReportBug = self._createAction(
            iconName="bug_report",
            text="&Report a Bug",
            objectName="actionReportBug",
            shortcut="",
            slot=self._mainController.onActionReportBugTriggered,
        )

    def _setupNavigationActions(self) -> None:
        """
        Configures navigation actions for page and comic navigation.
        """
        logger.debug("Setting up navigation actions")

        # Previous Page action
        self._actionPreviousPage = self._createAction(
            iconName="keyboard_arrow_left",
            text="Previous Page",
            objectName="actionPreviousPage",
            shortcut="Left",
            slot=self._mainController.onActionPreviousPageTriggered,
            enable=False,
        )

        # Next Page action
        self._actionNextPage = self._createAction(
            iconName="keyboard_arrow_right",
            text="Next Page",
            objectName="actionNextPage",
            shortcut="Right",
            slot=self._mainController.onActionNextPageTriggered,
            enable=False,
        )

        # First Page action
        self._actionFirstPage = self._createAction(
            iconName="first_page",
            text="First Page",
            objectName="actionFirstPage",
            shortcut="Ctrl+Left",
            slot=self._mainController.onActionFirstPageTriggered,
            enable=False,
        )

        # Last Page action
        self._actionLastPage = self._createAction(
            iconName="last_page",
            text="Last Page",
            objectName="actionLastPage",
            shortcut="Ctrl+Right",
            slot=self._mainController.onActionLastPageTriggered,
            enable=False,
        )

        # Previous Comic action
        self._actionPreviousComic = self._createAction(
            iconName="reply_all",
            text="Previous Comic",
            objectName="actionPreviousComic",
            shortcut="Ctrl+Shift+Left",
            slot=self._mainController.onActionPreviousComicTriggered,
            enable=False,
        )

        # Next Comic action
        self._actionNextComic = self._createAction(
            iconName="forward",
            text="Next Comic",
            objectName="actionNextComic",
            shortcut="Ctrl+Shift+Right",
            slot=self._mainController.onActionNextComicTriggered,
            enable=False,
        )

    def _setupFitActions(self) -> None:
        """
        Configures fit actions for adjusting the content display.
        """
        logger.debug("Setting up fit actions")

        # Fit Vertical action
        self._actionFitVertical = self._createAction(
            iconName="height",
            text="Fit Vertical",
            objectName="actionFitVertical",
            shortcut="V",
            slot=lambda: None,
            checkable=True,
            enable=False,
        )

        # Fit Horizontal action
        self._actionFitHorizontal = self._createAction(
            iconName="arrow_range",
            text="Fit Horizontal",
            objectName="actionFitHorizontal",
            shortcut="H",
            slot=lambda: None,
            checkable=True,
            enable=False,
        )

        # Fit Original action
        self._actionFitOriginal = self._createAction(
            iconName="view_real_size",
            text="Fit Original",
            objectName="actionFitOriginal",
            shortcut="O",
            slot=lambda: None,
            checkable=True,
            enable=False,
        )

        # Fit Page action
        self._actionFitPage = self._createAction(
            iconName="open_with",
            text="Fit Page",
            objectName="actionFitPage",
            shortcut="P",
            slot=lambda: None,
            checkable=True,
            enable=False,
        )

        # Group fit actions
        self._actionFitGroup = QActionGroup(self)
        self._actionFitGroup.addAction(self._actionFitVertical)
        self._actionFitGroup.addAction(self._actionFitHorizontal)
        self._actionFitGroup.addAction(self._actionFitPage)
        self._actionFitGroup.addAction(self._actionFitOriginal)

        # Connect fit group actions to controller
        self._actionFitGroup.triggered.connect(
            lambda action: self._mainController.onActionFitGroupTriggered(action.objectName())
        )

        # Set the current fit mode based on the controller's state
        for act in self._actionFitGroup.actions():
            act.setChecked(self._mainController.getCurrentFitMode() == act.objectName())

    def _setupRotateActions(self) -> None:
        """
        Configures rotate actions for rotating the content.
        """
        logger.debug("Setting up rotate actions")

        # Rotate Left action
        self._actionRotateLeft = self._createAction(
            iconName="rotate_left",
            text="Rotate Left",
            objectName="actionRotateLeft",
            shortcut="Ctrl+Shift+R",
            slot=self._mainController.onActionRotateLeftTriggered,
            enable=False,
        )

        # Rotate Right action
        self._actionRotateRight = self._createAction(
            iconName="rotate_right",
            text="Rotate Right",
            objectName="actionRotateRight",
            shortcut="Ctrl+R",
            slot=self._mainController.onActionRotateRightTriggered,
            enable=False,
        )

    def _setupToolBar(self) -> None:
        """
        Sets up the toolbar.
        This method adds actions to the toolbar and sets up the layout.
        """
        logger.info("Setting up the toolbar")

        self._toolBar.setMovable(False)
        self._toolBar.setContentsMargins(0, 0, 0, 0)
        self._toolBar.setAutoFillBackground(False)
        self._toolBar.setStyleSheet("QToolBar { border: 0; padding: 0; margin: 5; }")
        self._toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self._toolBar.setFloatable(False)

        self._toolBar.addAction(self._actionOpenFile)
        self._toolBar.addSeparator()
        self._toolBar.addAction(self._actionPreviousComic)
        self._toolBar.addAction(self._actionFirstPage)
        self._toolBar.addAction(self._actionPreviousPage)
        self._toolBar.addAction(self._actionNextPage)
        self._toolBar.addAction(self._actionLastPage)
        self._toolBar.addAction(self._actionNextComic)
        self._toolBar.addSeparator()
        self._toolBar.addAction(self._actionRotateLeft)
        self._toolBar.addAction(self._actionRotateRight)
        self._toolBar.addSeparator()
        self._toolBar.addActions(self._actionFitGroup.actions())
        self._toolBar.addSeparator()

        # Add spacer to the toolbar
        # to push the page spinbox to the right
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self._toolBar.addWidget(spacer)

        self._toolBar.addWidget(QLabel("Page: "))
        self._toolBar.addWidget(self._pageSpinbox)
        self._toolBar.addAction(self._actionReportBug)
        self._toolBar.addAction(self._actionAbout)

        self.addToolBar(Qt.TopToolBarArea, self._toolBar)

    def _setupCentralWidget(self) -> None:
        """
        Sets up the central widget of the main window.

        This method sets the central widget of the main window to the canvas view.
        """
        logger.info("Setting up central widget")

        # Set the margins for the central widget layout to zero
        self._centralWidgetLayout.setContentsMargins(0, 0, 0, 0)

        # Configure the scroll area to make its content resizable
        self._centralWidgetScrollArea.setWidgetResizable(True)
        self._centralWidgetScrollArea.setAutoFillBackground(False)

        # Set scroll bar policies to show them only when needed
        self._centralWidgetScrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self._centralWidgetScrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # Align the content of the scroll area to the center
        self._centralWidgetScrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Configure the QLabel to display content in the central widget
        self._centralWidgetLabel.setObjectName("centralWidgetLabel")
        self._centralWidgetLabel.setText(self.tr("Press Ctrl+0 to Open a Comic File"))

        # Set QLabel properties for appearance and behavior
        self._centralWidgetLabel.setMouseTracking(False)
        self._centralWidgetLabel.setAutoFillBackground(False)
        self._centralWidgetLabel.setScaledContents(False)
        self._centralWidgetLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the QLabel to the central widget layout
        self._centralWidgetLayout.addWidget(self._centralWidgetLabel)

        # Set the central widget as the content of the scroll area
        self._centralWidgetScrollArea.setWidget(self._centralWidget)

        # Define the scroll area as the central widget of the main window
        self.setCentralWidget(self._centralWidgetScrollArea)

    def _setupGlobalShortcuts(self) -> None:
        """
        Sets up global shortcuts for the application.
        This method creates shortcuts for various actions and connects them to their respective slots.
        """
        logger.debug("Setting up global shortcuts")

        # Shortcut to toggle fullscreen mode using the "F" key
        self.fullScreenShortcut = QShortcut(
            QKeySequence("F"), self, self.onActionFullscreenTriggered
        )
        self.fullScreenShortcut.setEnabled(True)

        # Shortcut to close the application using "Ctrl+Q"
        self.closeShortcut = QShortcut(QKeySequence("Ctrl+Q"), self, self.close)
        self.closeShortcut.setEnabled(True)

        logger.debug("Setting up fullscreen and close shortcuts")

        # Dictionary of shortcuts to disable when in fullscreen mode
        shortcutsToDisable = {
            "Ctrl+O": self.onActionOpenFileTriggered,  # Open file shortcut
            "Ctrl+Left": self._mainController.onActionFirstPageTriggered,  # Navigate to first page
            "Ctrl+Right": self._mainController.onActionLastPageTriggered,  # Navigate to last page
            "Right": self._mainController.onActionNextPageTriggered,  # Navigate to next page
            "Left": self._mainController.onActionPreviousPageTriggered,  # Navigate to previous page
        }

        # Create and configure shortcuts, initially disabled for fullscreen mode
        for key, action in shortcutsToDisable.items():
            shortcut = QShortcut(QKeySequence(key), self, action)
            shortcut.setEnabled(False)  # Disabled by default for fullscreen
            self._globalShortcuts.append(shortcut)

        logger.debug("Configured shortcuts to disable in fullscreen mode")

    @Slot(int)
    def onStartProgress(self, maximum: int) -> None:
        """
        Slot to handle the start of a progress operation.
        This method initializes and displays a progress dialog.

        Args:
            maximum (int): The maximum value for the progress dialog.
        """
        logger.info("Starting progress operation with maximum value: %d", maximum)

        self._progressDialog = QProgressDialog(self.tr("Loading Comic..."), "", 0, maximum)

        self._progressDialog.setCancelButton(None)
        self._progressDialog.setWindowModality(Qt.WindowModal)
        self._progressDialog.setWindowFlags(Qt.FramelessWindowHint)
        self._mainController.loadProgressSignal.connect(self._progressDialog.setValue)

    @Slot(str)
    def onErrorLoad(self, errorMsg: str) -> None:
        """
        Slot to handle errors during the loading process.
        Displays an error message and closes the progress dialog if active.

        Args:
            errorMsg (str): The error message to display.
        """
        logger.error("Error during comic loading: %s", errorMsg)

        QMessageBox.critical(
            self,
            self.tr("Error Loading Comic"),
            errorMsg,
            buttons=QMessageBox.Close,
            defaultButton=QMessageBox.Close,
        )

    @Slot()
    def onFinishProgress(self) -> None:
        """
        Slot to handle the completion of a progress operation.
        Closes the progress dialog if active.
        """
        logger.info("Progress operation finished")

        if self._progressDialog:
            self._progressDialog.setValue(self._progressDialog.maximum())
            self._progressDialog = None

    @Slot()
    def onDoneProgress(self) -> None:
        """
        Slot to handle the completion of a loading operation.
        Enables relevant actions and updates the UI based on the controller's state.
        """
        logger.info("Loading operation completed, updating UI")

        # Enable fit and rotate actions
        for action in [
            self._actionFitVertical,
            self._actionFitHorizontal,
            self._actionFitPage,
            self._actionFitOriginal,
            self._actionRotateLeft,
            self._actionRotateRight,
        ]:
            action.setEnabled(True)

        # Update comic navigation actions
        self._actionNextComic.setEnabled(bool(self._mainController.getNextComicPath()))
        self._actionPreviousComic.setEnabled(bool(self._mainController.getPreviousComicPath()))

        if self._progressDialog:
            self._progressDialog.close()
            self._progressDialog = None

    @Slot(bool, bool)
    def updatePageActionsStatus(self, isFirstPage: bool, isLastPage: bool) -> None:
        """
        Updates the state of the page navigation and comic navigation actions.

            isFirstPage (bool): True if the current page is the first page,
                                which may disable certain navigation actions.
            isLastPage (bool): True if the current page is the last page,
                               which may disable certain navigation actions.
        """

        logger.info("Updating page actions")

        self._actionPreviousPage.setEnabled(not isFirstPage)
        self._actionFirstPage.setEnabled(not isFirstPage)

        self._actionNextPage.setEnabled(not isLastPage)
        self._actionLastPage.setEnabled(not isLastPage)

    @Slot()
    def updateCentralWidgetContent(self, pixmap: QPixmap, rotateAngle: int = 0) -> None:
        """
        Updates the canvas to display the given QPixmap.

        Args:
            pixmap (QPixmap): The pixmap to display on the canvas.
        """
        logger.info("Updating canvas with a new QPixmap")

        if pixmap.isNull():
            logger.warning("Received a null pixmap, not updating the canvas")
            return

        self._centralWidgetLabel.setText("")
        pixmap = self.rotateCentralWidgetContent(pixmap, rotateAngle)
        pixmap = self.resizeCentralWidgetContent(pixmap)
        self._centralWidgetLabel.setPixmap(pixmap)

    def resizeCentralWidgetContent(self, pixmap: QPixmap) -> QPixmap:
        """
        Resizes the canvas to fit the current QPixmap.

        Args:
            pixmap (QPixmap): The pixmap to display on the canvas.

        Returns:
            QPixmap: The resized pixmap.
        """
        logger.info("Resizing canvas")

        height = self.centralWidget().contentsRect().size().height()
        width = self.centralWidget().contentsRect().size().width()

        fitActionChecked = self._actionFitGroup.checkedAction().objectName()

        if fitActionChecked == "actionFitVertical":
            pixmap = pixmap.scaledToHeight(int(height), Qt.SmoothTransformation)

        elif fitActionChecked == "actionFitHorizontal":
            pixmap = pixmap.scaledToWidth(int(width), Qt.SmoothTransformation)

        elif fitActionChecked == "actionFitPage" and (
            width < pixmap.width() or height < pixmap.height()
        ):
            pixmap = pixmap.scaled(
                int(width), int(height), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )

        return pixmap

    def rotateCentralWidgetContent(self, pixmap: QPixmap, rotateAngle: int) -> QPixmap:
        """
        Rotates the canvas by the specified angle.

        Args:
            pixmap (QPixmap): The pixmap to rotate.
            rotateAngle (int): The angle to rotate the pixmap.

        Returns:
            QPixmap: The rotated pixmap.
        """

        if rotateAngle != 0:
            trans = QTransform().rotate(rotateAngle)
            pixmap = QPixmap(pixmap.transformed(trans))

        return pixmap

    @Slot()
    def onActionOpenFileTriggered(self) -> None:
        """
        Handles the action triggered to open a file.

        This method opens a file dialog for the user to select a file,
        and updates the model with the selected file path.
        """

        filename, _ = QFileDialog().getOpenFileName(
            self,
            self.tr("Open Comic File"),
            self._mainController.getCurrentComicPath(),
            self.tr(
                "All supported files (*.zip *.cbz *.rar *.cbr *.tar *.cbt);; "
                "ZIP files (*.zip *.cbz);; RAR files (*.rar *.cbr);; "
                "TAR files (*.tar *.cbt);; "
                "All files (*)"
            ),
        )

        if filename:
            self._mainController._loadComic(filename)

        else:
            logger.info("No file selected")

    @Slot(int, int)
    def updatePageBox(self, pageStart: int, pageLength: int) -> None:
        """
        Updates the page spinbox with the current page and total pages.

        This method is called to refresh the page spinbox when the model's state changes.

        Args:
            pageStart (int): The current page number to set in the spinbox.
            pageLength (int): The total number of pages to set as the maximum value.
        """

        logger.info(
            "Updating page box with current page %d and total pages %d", pageStart, pageLength
        )

        # update page number and size
        self._pageSpinbox.setValue(pageStart)
        self._pageSpinbox.setMaximum(pageLength)

        self._pageSpinbox.setSuffix(self.tr(" of %d") % pageLength)

    @Slot()
    def updateWindowTitle(self, title: str) -> None:
        """
        Updates the window title.

        This method is called to refresh the window title when the model changes.
        """
        logger.info("Updating window title")
        self.setWindowTitle(title)

    @Slot()
    def onActionFullscreenTriggered(self):
        """
        Slot to handle the 'Fullscreen' action triggered event.
        Toggles the fullscreen mode of the main window.
        """
        logger.info("Fullscreen action triggered")

        if self.isFullScreen():
            self._toolBar.show()
            self.showNormal()
            self._mainController.updateCentralWidgetContent()

            for shortcut in self._globalShortcuts:
                shortcut.setEnabled(False)

        else:
            self.showFullScreen()
            self._toolBar.hide()
            self._mainController.updateCentralWidgetContent()

            for shortcut in self._globalShortcuts:
                shortcut.setEnabled(True)

    @Slot()
    def onActionAboutTriggered(self) -> None:
        """
        Slot to handle the 'About' action triggered event.

        Displays the "About" dialog when the 'About' action is triggered.
        """
        logger.info("About action triggered")

        self._aboutDialog: QDialog = QDialog(parent=self)

        # Create the About dialog
        self._aboutDialog.setWindowTitle(self.tr(f"About {APP_NAME}"))
        self._aboutDialog.setObjectName("aboutDialog")
        self._aboutDialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self._aboutDialog.setAttribute(Qt.WidgetAttribute.WA_QuitOnClose, False)
        self._aboutDialog.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint, True)
        self._aboutDialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self._aboutDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        self._aboutDialog.setModal(True)
        self._aboutDialog.setMinimumWidth(400)
        self._aboutDialog.setMinimumHeight(400)

        layout: QVBoxLayout = QVBoxLayout()

        logoPixmap = QPixmap(":/logo.ico")
        logoPixmap = logoPixmap.scaledToHeight(
            int(logoPixmap.height() * 0.5), Qt.SmoothTransformation
        )

        # Add an icon to the dialog
        icon_label: QLabel = QLabel()
        icon_label.setPixmap(logoPixmap)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        description = self.tr(
            f'<h1>{APP_NAME}</h1><h3>Version {VERSION}</h3><br/>A minimalist comic book reader.\
            <br/><br/>GNU General Public License v3 (<a href="{LICENSE_URL}">GPLv3</a>) <br/><br/>{COPYRIGHT}<br/><br/>'
        )

        about_label: QLabel = QLabel(description)
        about_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        about_label.setWordWrap(True)
        about_label.setOpenExternalLinks(True)

        buttonBox: QDialogButtonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Close, self._aboutDialog
        )

        buttonBox.setCenterButtons(True)
        buttonBox.rejected.connect(self._aboutDialog.close)

        layout.addWidget(icon_label)
        layout.addWidget(about_label)
        layout.addWidget(buttonBox)

        self._aboutDialog.setLayout(layout)

        self._aboutDialog.show()

        logger.debug("UI setup for AboutView completed")

        # description = self.tr(
        #     f'<h3>{APP_NAME} - v{VERSION}</h3><br/>A minimalist comic book reader.\
        #     <br/><br/>GNU General Public License v3 (<a href="{LICENSE_URL}">GPLv3</a>) <br/><br/>{COPYRIGHT}<br/><br/>'
        # )

        # QMessageBox.about(
        #     self,
        #     f"About {APP_NAME}",
        #     description,
        # )

    def closeEvent(self, event: "QCloseEvent") -> None:
        """
        Handles the close event of the main window.
        This method is called when the user attempts to close the main window.
        It saves the current state of the application and closes the window.

        Args:
            event (QCloseEvent): The close event object.
        """
        logger.info("Closing main window")

        self._mainController.saveData()
        event.accept()

        # super().close()
