# -*- coding: utf-8 -*-

from pynocchio import IMAGE_FILE_FORMATS, SUPPORTED_FILES

from .exception import InvalidTypeFileException
from .utility import get_file_extension
from .comic_file_loader import ComicZipLoader
from .comic_file_loader import ComicRarLoader
from .comic_file_loader import ComicTarLoader
from .comic_file_loader import ComicImageLoader


class ComicLoaderFactory:

    @staticmethod
    def create_loader(filename):

        if get_file_extension(file_name=filename) not in SUPPORTED_FILES:
            raise InvalidTypeFileException('Format File is not supported: %s'
                                           % get_file_extension(filename))

        if get_file_extension(file_name=filename) in IMAGE_FILE_FORMATS:
            return ComicImageLoader()

        elif ComicZipLoader.type_verify(file_name=filename):
            return ComicZipLoader()
        elif ComicRarLoader.type_verify(file_name=filename):
            return ComicRarLoader()
        elif ComicTarLoader.type_verify(file_name=filename):
            return ComicTarLoader()
        else:
            raise InvalidTypeFileException(
                'File is not folder: %s' % get_file_extension(filename))
