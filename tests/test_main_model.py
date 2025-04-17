from unittest.mock import MagicMock

import pytest

from src.models.comic import Comic
from src.models.comic_handler import ComicHandler
from src.models.main_model import MainModel


@pytest.fixture
def main_model(qtbot):
    """Fixture for creating a MainModel instance."""
    return MainModel()


def test_set_and_get_comic(main_model):
    comic = MagicMock(spec=Comic)
    main_model.setComic(comic)
    assert main_model.getComic() == comic


def test_set_and_get_comic_handler(main_model):
    handler = MagicMock(spec=ComicHandler)
    main_model.setComicHandler(handler)
    assert main_model.getComicHandler() == handler


def test_set_and_get_current_comic_path(main_model):
    comic_path = "/path/to/comic"
    main_model.setCurrentComicPath(comic_path)
    assert main_model.getCurrentComicPath() == comic_path


def test_set_and_get_current_fit_mode(main_model):
    fit_mode = "fit_width"
    main_model.setCurrentFitMode(fit_mode)
    assert main_model.getCurrentFitMode() == fit_mode


def test_rotate_page_left(main_model):
    main_model.rotatePageLeft()
    assert main_model.getPageRotateAngle() == 270  # -90 % 360 = 270


def test_rotate_page_right(main_model):
    main_model.rotatePageRight()
    assert main_model.getPageRotateAngle() == 90
