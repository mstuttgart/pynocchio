# -*- coding: utf-8 -*-

from .exception import InvalidTypeFileException
from .utility import get_file_extension, is_dir, is_file
from .comic_file_loader import ComicZipLoader
from .comic_file_loader import ComicRarLoader
from .comic_file_loader import ComicTarLoader
from .comic_file_loader import ComicFolderLoader


class ComicLoaderFactory:

    @staticmethod
    def create_loader(filename):

        if is_file(file_name=filename):

            loaders = [ComicZipLoader, ComicRarLoader, ComicTarLoader]

            # Return appropriate loader by with file compact coding
            for loader in loaders:
                if loader.type_verify(file_name=filename):
                    return loader()

            raise InvalidTypeFileException('Invalid file extension: %s' % get_file_extension(filename))  # noqa: 501
        elif is_dir(filename):
            return ComicFolderLoader()
        else:
            raise InvalidTypeFileException('File is not folder: %s' % get_file_extension(filename))  # noqa: 501
