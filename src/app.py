import logging
import sys

from PySide6.QtWidgets import QApplication

import src.app_rc  # noqa: F401
from src.__version__ import __version__
from src.controllers.main_controller import MainController
from src.models.constants import APP_NAME
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

        self._mainModel: MainModel = MainModel()
        self._MainController: MainController = MainController(self._mainModel)

        self._mainWindowView: MainWindowView = MainWindowView(self._MainController)

        self._mainWindowView.show()


def main():
    app: App = App(sys.argv)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
