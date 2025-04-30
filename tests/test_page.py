from unittest.mock import patch

import pytest
from PySide6.QtGui import QImage

from src.models.page import Page


@pytest.fixture
def page(qtbot):
    """
    Fixture to create a Page object.
    """
    return Page(data=b"xyz", title="title", number=1)


def test_create_page(page):
    """
    Test creating a Page object.
    """
    assert page.getData() == b"xyz"
    assert page.getTitle() == "title"
    assert page.getNumber() == 1


def test_set_title(page):
    """
    Test setting the title of a Page object.
    """
    new_title = "new title"
    page.setTitle(new_title)
    assert page.getTitle() == new_title


def test_getTitle(page):
    """
    Test getting the title of a Page object.
    """
    assert page.getTitle() == "title"


def test_getNumber(page):
    """
    Test getting the number of a Page object.
    """
    assert page.getNumber() == 1


def test_getData(page):
    """
    Test getting the data of a Page object.
    """
    assert page.getData() == b"xyz"


# TOFIXME Fix QImage create on this test
# def test_get_pixmap_with_valid_data(page):
#     """
#     Test getPixmap with valid image data.
#     """
#     with (
#         patch("PySide6.QtGui.QImage.loadFromData") as mock_load,
#         patch("PySide6.QtGui.QPixmap.fromImage") as mock_from_image,
#     ):
#         mock_load.return_value = True
#         mock_from_image.return_value = QPixmap("resources/logo.png")

#         pixmap = page.getPixmap()
#         assert not pixmap.isNull()

#         mock_load.assert_called_once_with(page.getData())
#         mock_from_image.assert_called_once()


def test_get_pixmap_with_invalid_data(page):
    """
    Test getPixmap with invalid image data.
    """

    with patch.object(QImage, "loadFromData", return_value=True) as mock_load:
        pixmap = page.getPixmap()
        assert pixmap.isNull()
        mock_load.assert_called_once_with(page.getData())
