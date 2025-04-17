import random
import zipfile  # noqa: F401
from unittest import mock

import pytest

from src.models.comic_loader_zip import ComicZipLoader, is_zipfile
from src.models.page import Page


class MockZipFile:
    """Mock class for zipfile.ZipFile."""

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
        raise zipfile.BadZipFile(f"File {filename} not found in archive.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.fixture
def setup_loader():
    loader = ComicZipLoader("dummy_file")
    mock_zip_file = MockZipFile([])

    valid_image_files = [f"image_{i}.jpg" for i in range(5)]
    invalid_files = ["text_file.txt", "document.pdf"]
    all_files = valid_image_files + invalid_files

    random.shuffle(all_files)

    for file in all_files:
        mock_zip_file.write(file, data=b"mock_data")

    return loader, mock_zip_file, valid_image_files, invalid_files


def test_is_zipfile():
    """Test the is_zipfile function."""
    with mock.patch("zipfile.is_zipfile", return_value=True):
        assert is_zipfile("test.zip")

    with mock.patch("zipfile.is_zipfile", return_value=False):
        assert not is_zipfile("test.zip")


@mock.patch("zipfile.is_zipfile")
@mock.patch("zipfile.ZipFile")
def test_load_valid_zip_file(mock_zipfile, mock_is_zipfile, setup_loader):
    """Test loading a valid ZIP file with supported image formats."""
    loader, mock_zip_file, valid_image_files, _ = setup_loader

    mock_is_zipfile.return_value = True
    mock_zipfile.return_value = mock_zip_file

    loader.load("mock_comic.zip")

    data = loader.getData()
    assert len(data) == len(valid_image_files)

    sorted_files = sorted(valid_image_files)

    for idx, page in enumerate(data, start=1):
        assert isinstance(page, Page)
        assert page.getTitle() == sorted_files[idx - 1]
        assert page.getNumber() == idx + 1
        assert page.getData() == b"mock_data"


@mock.patch("zipfile.is_zipfile")
@mock.patch("zipfile.ZipFile")
def test_load_invalid_data_zip_file(mock_zipfile, mock_is_zipfile, setup_loader):
    """Test loading a ZIP file with no supported image formats."""
    loader, _, _, invalid_files = setup_loader

    mock_is_zipfile.return_value = True
    mock_zip_file = MockZipFile(invalid_files)
    mock_zipfile.return_value = mock_zip_file

    with pytest.raises(ValueError, match="No valid data found in the ZIP file."):
        loader.load("mock_comic.zip")


@mock.patch("zipfile.is_zipfile")
@mock.patch("zipfile.ZipFile")
def test_load_non_zip_file(mock_zipfile, mock_is_zipfile, setup_loader):
    """Test loading a file that is not a valid ZIP file."""
    loader, _, _, _ = setup_loader

    mock_is_zipfile.return_value = True
    mock_zipfile.side_effect = zipfile.BadZipFile

    with pytest.raises(ValueError, match="Failed to load ZIP file"):
        loader.load("not_a_zip_file.zip")


@mock.patch("zipfile.is_zipfile", return_value=False)
def test_load_invalid_file_type(mock_is_zipfile, setup_loader):
    """Test loading a file that is not recognized as a ZIP file."""
    loader, _, _, _ = setup_loader

    with pytest.raises(TypeError, match="is not a valid ZIP file"):
        loader.load("invalid_file.txt")
