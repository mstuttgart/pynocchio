import random
from unittest import mock

import pytest
import rarfile  # noqa: F401

from src.models.comic_loader_rar import ComicRarLoader, is_rarfile
from src.models.page import Page


class MockRarFile:
    """Mock class for rarfile.RarFile."""

    def __init__(self, filenames):
        self.filenames = filenames
        self.files = {}

    def write(self, filename, data=b""):
        self.files[filename] = data

    def namelist(self):
        return list(self.files.keys())

    def read(self, filename):
        if filename in self.files:
            return self.files[filename]
        raise rarfile.BadRarFile(f"File {filename} not found in archive.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.fixture
def setup_loader():
    loader = ComicRarLoader("dummy_file")
    mock_rar_file = MockRarFile([])

    valid_image_files = [f"image_{i}.jpg" for i in range(5)]
    invalid_files = [
        "text_file.txt",
        "document.pdf",
    ]
    all_files = valid_image_files + invalid_files

    random.shuffle(all_files)

    for file in all_files:
        mock_rar_file.write(file, data=b"mock_data")

    return loader, mock_rar_file, valid_image_files, invalid_files


def test_is_rarfile():
    """Test the is_rarfile function."""
    with mock.patch("rarfile.is_rarfile", return_value=True):
        assert is_rarfile("test.rar")

    with mock.patch("rarfile.is_rarfile", return_value=False):
        assert not is_rarfile("test.rar")


def test_load_valid_rar_file(setup_loader):
    """Test loading a valid RAR file with supported image formats."""
    loader, mock_rar_file, valid_image_files, _ = setup_loader

    with (
        mock.patch("rarfile.is_rarfile", return_value=True),
        mock.patch("rarfile.RarFile", return_value=mock_rar_file),
    ):
        loader.load("mock_comic.rar")

        data = loader.getData()
        assert len(data) == len(valid_image_files)

        sorted_files = sorted(valid_image_files)

        for idx, page in enumerate(data, start=1):
            assert isinstance(page, Page)
            assert page.getTitle() == sorted_files[idx - 1]
            assert page.getNumber() == idx + 1
            assert page.getData() == b"mock_data"


def test_load_invalid_data_rar_file(setup_loader):
    """Test loading a RAR file with no supported image formats."""
    loader, _, _, invalid_files = setup_loader

    mock_rar_file = MockRarFile(invalid_files)

    with (
        mock.patch("rarfile.is_rarfile", return_value=True),
        mock.patch("rarfile.RarFile", return_value=mock_rar_file),
    ):
        with pytest.raises(ValueError, match="No valid data found in the RAR file."):
            loader.load("mock_comic.rar")


def test_load_non_rar_file(setup_loader):
    """Test loading a file that is not a valid RAR file."""
    loader, _, _, _ = setup_loader

    with (
        mock.patch("rarfile.is_rarfile", return_value=True),
        mock.patch("rarfile.RarFile", side_effect=rarfile.Error),
    ):
        with pytest.raises(ValueError, match="Failed to load RAR file"):
            loader.load("not_a_rar_file.rar")


def test_load_invalid_file_type(setup_loader):
    """Test loading a file that is not recognized as a RAR file."""
    loader, _, _, _ = setup_loader

    with mock.patch("rarfile.is_rarfile", return_value=False):
        with pytest.raises(TypeError, match="is not a valid RAR file"):
            loader.load("invalid_file.txt")
