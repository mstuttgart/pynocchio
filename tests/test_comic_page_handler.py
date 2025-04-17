import pytest

from src.models.comic import Comic
from src.models.comic_handler import ComicHandler
from src.models.page import Page


@pytest.fixture
def comic_handler(qtbot):
    """
    Fixture to set up a ComicHandler instance with a mock Comic object.
    """
    comic = Comic("comic_test", "comic_dir")
    page_1 = Page(b"zyz", "page_title_1", 1)
    page_2 = Page(b"zyz", "page_title_2", 2)
    page_3 = Page(b"zyz", "page_title_3", 3)

    comic.setPages([page_1, page_2, page_3])

    handler = ComicHandler(comic)

    return handler, comic, [page_1, page_2, page_3]


def test_get_comic(comic_handler):
    """
    Test that the handler returns the correct comic object.
    """
    handler, comic, _ = comic_handler
    assert handler.getComic() == comic


def test_set_comic(comic_handler):
    """
    Test that the handler can set a new comic object.
    """
    handler, _, _ = comic_handler
    new_comic = Comic("new_comic", "new_dir")
    handler.setComic(new_comic)
    assert handler.getComic() == new_comic


def test_get_current_page_index(comic_handler):
    """
    Test that the handler returns the correct initial page index.
    """
    handler, _, _ = comic_handler
    assert handler.getCurrentPageIndex() == 0


def test_set_current_page_index_valid(comic_handler):
    """
    Test that the handler sets a valid page index correctly.
    """
    handler, _, _ = comic_handler
    handler.setCurrentPageIndex(2)
    assert handler.getCurrentPageIndex() == 2


def test_set_current_page_index_invalid(comic_handler):
    """
    Test that the handler resets to the first page when an invalid index is set.
    """
    handler, _, _ = comic_handler
    handler.setCurrentPageIndex(5)
    assert handler.getCurrentPageIndex() == 0


def test_get_current_page(comic_handler):
    """
    Test that the handler returns the correct current page.
    """
    handler, _, pages = comic_handler
    assert handler.getCurrentPage() == pages[0]
    handler.setCurrentPageIndex(1)
    assert handler.getCurrentPage() == pages[1]


def test_go_first_page(comic_handler):
    """
    Test that the handler navigates to the first page.
    """
    handler, _, _ = comic_handler
    handler.setCurrentPageIndex(2)
    handler.goFirstPage()
    assert handler.getCurrentPageIndex() == 0


def test_go_last_page(comic_handler):
    """
    Test that the handler navigates to the last page.
    """
    handler, _, _ = comic_handler
    handler.goLastPage()
    assert handler.getCurrentPageIndex() == 2


def test_get_current_page_image_not_implemented(comic_handler):
    """
    Test that getCurrentPageImage raises a NotImplementedError.
    """
    handler, _, _ = comic_handler
    with pytest.raises(NotImplementedError):
        handler.getCurrentPageImage()


def test_go_next_page_not_implemented(comic_handler):
    """
    Test that goNextPage raises a NotImplementedError.
    """
    handler, _, _ = comic_handler
    with pytest.raises(NotImplementedError):
        handler.goNextPage()


def test_go_previous_page_not_implemented(comic_handler):
    """
    Test that goPreviousPage raises a NotImplementedError.
    """
    handler, _, _ = comic_handler
    with pytest.raises(NotImplementedError):
        handler.goPreviousPage()
