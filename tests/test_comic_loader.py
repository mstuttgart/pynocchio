import pytest

from src.models.comic_loader import ComicLoader
from src.models.page import Page


@pytest.fixture
def comic_loader():
    return ComicLoader("dummy_file")


def test_initialization(comic_loader):
    """
    Test that ComicLoader initializes with an empty data list.
    """
    assert comic_loader.getData() == []


def test_set_data(comic_loader):
    """
    Test that setData correctly sets the data.
    """
    pages = [Page(b"123", "page 01", 1), Page(b"123", "page 02", 2)]  # Mock Page instances
    comic_loader.setData(pages)
    assert comic_loader.getData() == pages


def test_get_data(comic_loader):
    """
    Test that getData returns the correct data.
    """
    pages = [Page(b"123", "page 01", 1), Page(b"123", "page 02", 2)]  # Mock Page instances
    comic_loader.setData(pages)
    assert comic_loader.getData() == pages


def test_load_raises_not_implemented_error(comic_loader):
    """
    Test that calling load raises NotImplementedError.
    """
    with pytest.raises(NotImplementedError, match="Subclasses must implement this method."):
        comic_loader.load("dummy_file")
