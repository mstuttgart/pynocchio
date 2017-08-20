# -*- coding: utf-8 -*-

from .exception import InvalidTypeFileException
from .utility import get_file_extension
from .utility import IMAGE_FILE_FORMATS, SUPPORTED_FILES
from .comic_file_loader_zip import ComicZipLoader, is_zipfile
from .comic_file_loader_rar import ComicRarLoader, is_rarfile
from .comic_file_loader_tar import ComicTarLoader, is_tarfile
from .comic_file_loader_image import ComicImageLoader


class ComicLoaderFactory:

    @staticmethod
    def create_loader(filename):

        if get_file_extension(file_name=filename) not in SUPPORTED_FILES:
            raise InvalidTypeFileException('Format File is not supported: %s'
                                           % get_file_extension(filename))

        if get_file_extension(file_name=filename) in IMAGE_FILE_FORMATS:
            return ComicImageLoader()

        elif is_zipfile(file_name=filename):
            return ComicZipLoader()
        elif is_rarfile(file_name=filename):
            return ComicRarLoader()
        elif is_tarfile(file_name=filename):
            return ComicTarLoader()
        else:
            raise InvalidTypeFileException(
                'File is not folder: %s' % get_file_extension(filename))
