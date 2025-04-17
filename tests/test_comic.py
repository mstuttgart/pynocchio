import os

import pytest

from src.models.comic import Comic
from src.models.page import Page


@pytest.fixture
def comic_data(qtbot):
    filename = "comic.zip"
    directory = "comic_dir"
    pages = [
        Page(b"123", "page 01", 1),
        Page(b"456", "page 02", 2),
    ]
    comic = Comic(filename, directory)
    return comic, filename, directory, pages


def test_get_filename(comic_data):
    """
    Test the getFilename method.
    This test checks if the filename is retrieved correctly.
    """
    comic, filename, _, _ = comic_data
    assert comic.getFilename() == filename


def test_set_filename(comic_data):
    """
    Test the setFilename method.
    """
    comic, _, _, _ = comic_data
    new_filename = "new_comic.zip"
    comic.setFilename(new_filename)
    assert comic.getFilename() == new_filename


def test_get_directory(comic_data):
    """
    Test the getDirectory method.
    """
    comic, _, directory, _ = comic_data
    assert comic.getDirectory() == directory


def test_set_directory(comic_data):
    """
    Test the setDirectory method.
    """
    comic, _, _, _ = comic_data
    new_directory = "new_comic_dir"
    comic.setDirectory(new_directory)
    assert comic.getDirectory() == new_directory


def test_get_pages(comic_data):
    """
    Test the getPages method.
    """
    comic, _, _, _ = comic_data
    assert comic.getPages() == []


def test_set_pages(comic_data):
    """
    Test the setPages method.
    """
    comic, _, _, pages = comic_data
    comic.setPages(pages)
    assert comic.getPages() == pages


def test_get_comic_path(comic_data):
    """
    Test the getComicPath method.
    """
    comic, filename, directory, _ = comic_data
    expected_path = os.path.join(directory, filename)
    assert comic.getComicPath() == expected_path


def test_comic_initialization(comic_data):
    """
    Test the initialization of the Comic class.
    """
    comic, filename, directory, _ = comic_data
    assert comic.getFilename() == filename
    assert comic.getDirectory() == directory
    assert comic.getPages() == []


def test_set_and_get_pages(comic_data):
    """
    Test setting and getting pages.
    """
    comic, _, _, pages = comic_data
    comic.setPages(pages)
    assert comic.getPages() == pages
    assert len(comic.getPages()) == len(pages)
    assert all(isinstance(page, Page) for page in comic.getPages())
