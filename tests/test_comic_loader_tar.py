import random
import tarfile
from unittest import mock

import pytest

from src.models.comic_loader_tar import ComicTarLoader, is_tarfile
from src.models.page import Page


class MockTarFile:
    """Mock class for TarFile."""

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
        raise tarfile.ReadError(f"File {filename} not found in archive.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.fixture
def setup_loader():
    loader = ComicTarLoader("dummy_file")
    mock_tar_file = MockTarFile([])

    valid_image_files = [f"image_{i}.jpg" for i in range(5)]
    invalid_files = ["text_file.txt", "document.pdf"]
    all_files = valid_image_files + invalid_files

    random.shuffle(all_files)

    for file in all_files:
        mock_tar_file.write(file, data=b"mock_data")

    return loader, mock_tar_file, valid_image_files, invalid_files


def test_is_tarfile():
    """Test the is_tarfile function."""
    with mock.patch("tarfile.is_tarfile", return_value=True):
        assert is_tarfile("test.tar")

    with mock.patch("tarfile.is_tarfile", return_value=False):
        assert not is_tarfile("test.tar")


@mock.patch("tarfile.is_tarfile")
@mock.patch("src.models.comic_loader_tar.TarFile")
def test_load_valid_tar_file(mock_tarfile, mock_is_tarfile, setup_loader):
    """Test loading a valid TAR file with supported image formats."""
    loader, mock_tar_file, valid_image_files, _ = setup_loader

    mock_is_tarfile.return_value = True
    mock_tarfile.return_value = mock_tar_file

    loader.load("mock_comic.tar")

    data = loader.getData()
    assert len(data) == len(valid_image_files)

    sorted_files = sorted(valid_image_files)

    for idx, page in enumerate(data, start=1):
        assert isinstance(page, Page)
        assert page.getTitle() == sorted_files[idx - 1]
        assert page.getNumber() == idx + 1
        assert page.getData() == b"mock_data"


@mock.patch("tarfile.is_tarfile")
@mock.patch("src.models.comic_loader_tar.TarFile")
def test_load_invalid_data_tar_file(mock_tarfile, mock_is_tarfile, setup_loader):
    """Test loading a TAR file with no supported image formats."""
    loader, _, _, invalid_files = setup_loader

    mock_is_tarfile.return_value = True
    mock_tarfile.return_value = MockTarFile(invalid_files)

    with pytest.raises(ValueError, match="No valid data found in the TAR file."):
        loader.load("mock_comic.tar")


@mock.patch("tarfile.is_tarfile")
@mock.patch("src.models.comic_loader_tar.TarFile")
def test_load_non_tar_file(mock_tarfile, mock_is_tarfile, setup_loader):
    """Test loading a file that is not a valid TAR file."""
    loader, _, _, _ = setup_loader

    mock_is_tarfile.return_value = True
    mock_tarfile.side_effect = tarfile.ReadError

    with pytest.raises(ValueError, match="Failed to load TAR file"):
        loader.load("not_a_tar_file.tar")


@mock.patch("tarfile.is_tarfile")
def test_load_invalid_file_type(mock_is_tarfile, setup_loader):
    """Test loading a file that is not recognized as a TAR file."""
    loader, _, _, _ = setup_loader

    mock_is_tarfile.return_value = False

    with pytest.raises(TypeError, match="is not a valid TAR file"):
        loader.load("invalid_file.txt")
