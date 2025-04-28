import logging
import sys

from PySide6.QtCore import QLocale, QTranslator
from PySide6.QtWidgets import QApplication

import src.app_rc  # noqa: F401
from src.__version__ import __version__
from src.controllers.main_controller import MainController
from src.models.constants import APP_NAME, LANGUAGE, Language
from src.models.main_model import MainModel
from src.views.main_window_view import MainWindowView

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class App(QApplication):
    """
    A custom QApplication subclass that serves as the main application class.

    This class initializes the application with the specified system arguments,
    sets up the organization and application names, and creates the main model,
    controller, and main window view for the application.
    """

    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        self.setOrganizationName(APP_NAME)
        self.setApplicationName(APP_NAME)
        self.setApplicationVersion(__version__)

        self.setStyle("Fusion")


def main() -> None:
    """
    Main function to run the application.
    This function initializes the QApplication, sets up internationalization,
    creates the main model and controller, and shows the main window view.
    """
    # Initialize the application
    app: App = App(sys.argv)

    # Internationalization
    translator: QTranslator = QTranslator(app)

    if LANGUAGE == Language.AUTO:
        if translator.load(QLocale.system(), ":/translations/i18n/"):
            logger.info("Loaded translation file.")
            app.installTranslator(translator)
        else:
            logger.warning("Failed to load translation file.")

    elif LANGUAGE != Language.ENGLISH:
        if translator.load(f":/translations/i18n/{LANGUAGE}.qm"):
            logger.info("Loaded translation file.")
            app.installTranslator(translator)
        else:
            logger.warning("Failed to load translation file.")

    mainModel: MainModel = MainModel()
    mainController: MainController = MainController(mainModel)

    mainWindowView: MainWindowView = MainWindowView(mainController)

    mainWindowView.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
