from unittest import mock

import pytest

from src.models.comic_loader_factory import ComicLoaderFactory
from src.models.comic_loader_rar import ComicRarLoader
from src.models.comic_loader_tar import ComicTarLoader
from src.models.comic_loader_zip import ComicZipLoader


class TestComicLoaderFactory:
    """
    Unit tests for the ComicLoaderFactory class, which is responsible for creating
    appropriate loader instances based on the file type.
    """

    @mock.patch("src.models.comic_loader_factory.is_zipfile", lambda filename: True)
    def test_create_loader_zip(self):
        """
        Test that ComicLoaderFactory creates a ComicZipLoader instance
        when the file is identified as a ZIP file.
        """
        loader = ComicLoaderFactory.createLoader("test.zip")
        assert isinstance(loader, ComicZipLoader)

    @mock.patch("src.models.comic_loader_factory.is_rarfile", lambda filename: True)
    def test_create_loader_rar(self):
        """
        Test that ComicLoaderFactory creates a ComicRarLoader instance
        when the file is identified as a RAR file.
        """
        loader = ComicLoaderFactory.createLoader("test.rar")
        assert isinstance(loader, ComicRarLoader)

    @mock.patch("src.models.comic_loader_factory.is_tarfile", lambda filename: True)
    def test_create_loader_tar(self):
        """
        Test that ComicLoaderFactory creates a ComicRarLoader instance
        when the file is identified as a TAR file.
        """
        loader = ComicLoaderFactory.createLoader("test.tar")
        assert isinstance(loader, ComicTarLoader)

    @mock.patch(
        "src.models.comic_loader_factory.getFileExtension",
        lambda filename: ".unsupported",
    )
    def test_create_loader_unsupported_file_format(self):
        """
        Test that ComicLoaderFactory raises a TypeError when the file format
        is not supported.
        """
        with pytest.raises(TypeError, match="Unsupported file format: .unsupported"):
            ComicLoaderFactory.createLoader("test.unsupported")

    @mock.patch("src.models.comic_loader_factory.getFileExtension", lambda filename: ".zip")
    @mock.patch("src.models.comic_loader_factory.is_zipfile", lambda filename: False)
    @mock.patch("src.models.comic_loader_factory.is_rarfile", lambda filename: False)
    @mock.patch("src.models.comic_loader_factory.is_tarfile", lambda filename: False)
    def test_create_loader_unsupported_file_type(self):
        """
        Test that ComicLoaderFactory raises a TypeError when the file type
        is not recognized even if the extension is supported.
        """
        with pytest.raises(TypeError, match="Unsupported file type: .zip"):
            ComicLoaderFactory.createLoader("test.zip")
