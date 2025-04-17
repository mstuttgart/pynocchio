import pytest
from PySide6.QtGui import QPixmap

from src.models.comic import Comic
from src.models.comic_handler_single_page import ComicHandlerSinglePage
from src.models.page import Page


@pytest.fixture
def comic_handler(qtbot):
    """
    Fixture to set up a ComicHandlerSinglePage object with a mock comic and pages.
    """
    comic = Comic("comic_test", "comic_dir")
    page_1 = Page(b"zyz", "page_title_1", 1)
    page_2 = Page(b"zyz", "page_title_2", 2)
    page_3 = Page(b"zyz", "page_title_3", 3)

    comic.setPages([page_1, page_2, page_3])

    obj = ComicHandlerSinglePage(comic)

    return obj


def test_go_next_page(comic_handler):
    """
    Test that the goNextPage method correctly updates the current page index.
    """
    comic_handler.goNextPage()
    assert comic_handler.getCurrentPageIndex() == 1

    comic_handler.goNextPage()
    assert comic_handler.getCurrentPageIndex() == 2

    comic_handler.goNextPage()
    assert comic_handler.getCurrentPageIndex() == 2  # Should not exceed the last page


def test_go_previous_page(comic_handler):
    """
    Test that the goPreviousPage method correctly updates the current page index.
    """
    comic_handler.setCurrentPageIndex(2)

    comic_handler.goPreviousPage()
    assert comic_handler.getCurrentPageIndex() == 1

    comic_handler.goPreviousPage()
    assert comic_handler.getCurrentPageIndex() == 0

    comic_handler.goPreviousPage()
    assert comic_handler.getCurrentPageIndex() == 0  # Should not go below the first page


def test_get_current_page_image(comic_handler):
    """
    Test that the getCurrentPageImage method returns a QPixmap object.
    """
    pixmap = comic_handler.getCurrentPageImage()
    assert isinstance(pixmap, QPixmap)  # Check if it returns a mocked QPixmap
