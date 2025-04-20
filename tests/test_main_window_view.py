from unittest.mock import MagicMock

import pytest
from PySide6.QtWidgets import QApplication

import src.app_rc  # noqa: F401
from src.controllers.main_controller import MainController
from src.models.main_model import MainModel
from src.views.main_window_view import MainWindowView


@pytest.fixture
def app(qtbot):
    """Fixture for creating a QApplication instance."""
    return QApplication.instance() or QApplication([])


@pytest.fixture
def main_model():
    """Fixture for creating a mock MainModel."""
    model = MagicMock(spec=MainModel)
    model.updateMainView = MagicMock()
    return model


@pytest.fixture
def main_controller():
    """Fixture for creating a mock MainController."""
    return MagicMock(spec=MainController)


@pytest.fixture
def main_window_view(qtbot):
    """Fixture for creating the MainWindowView."""
    settings_manager = MagicMock()
    window = MainWindowView(settings_manager)
    qtbot.addWidget(window)
    return window


def test_setup_ui(main_window_view):
    """Test the setupUI method."""
    assert main_window_view.windowTitle() == "Pynocchio"
    # assert main_window_view.menuBar() is not None
    assert main_window_view.centralWidget() is not None


def test_setup_actions(main_window_view):
    """Test the setupActions method."""
    assert main_window_view._actionExit.text() == "Exit"
    assert main_window_view._actionOpenFile.text() == "Open File"
    assert main_window_view._actionAbout.text() == "About"
    assert main_window_view._actionReportBug.text() == "Report a Bug"
    assert main_window_view._actionPreviousPage.text() == "Previous Page"
    assert main_window_view._actionNextPage.text() == "Next Page"
    assert main_window_view._actionFirstPage.text() == "First Page"
    assert main_window_view._actionLastPage.text() == "Last Page"


def test_action_exit_triggered(main_window_view, qtbot):
    """Test the Exit action."""
    with qtbot.waitSignal(main_window_view._actionExit.triggered, timeout=0):
        main_window_view._actionExit.trigger()

        def test_fit_page_enum():
            """Test the FitPage enum."""
            assert MainWindowView.FitPage.FITVERTICAL.value == "actionFitVertical"
            assert MainWindowView.FitPage.FITHORIZONTAL.value == "actionFitHorizontal"
            assert MainWindowView.FitPage.FITORIGINAL.value == "actionFitOriginal"
            assert MainWindowView.FitPage.FITPAGE.value == "actionFitPage"
