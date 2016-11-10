# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5 import QtCore

import glob
import logging
import zipfile
import tarfile

try:
    import rarfile
except ImportError as err:
    msg = """"rarfile module not installed.
          you not can load .rar and .cbr files.
          Please install it using: sudo pip install rarfile"""
    raise DependenceNotFoundException(msg)

from .utility import Utility
from .page import Page
from .exception import LoadComicsException
from .exception import InvalidTypeFileException
from .exception import NoDataFindException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ComicLoader(QtCore.QObject):

    progress = QtCore.pyqtSignal(int)
    done = QtCore.pyqtSignal()

    def __init__(self, extension):
        super(ComicLoader, self).__init__()
        self.extension = extension
        self.data = []

    def load(self, file_name):
        raise NotImplementedError("Must subclass me")

    @staticmethod
    def type_verify(file_name):
        raise NotImplementedError("Must subclass me")


class ComicRarLoader(ComicLoader):

    def __init__(self, extension):
        super(ComicRarLoader, self).__init__(extension)

    def load(self, file_name):
        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError as exception:
            raise InvalidTypeFileException(exception.message)
        except IOError as exception:
            raise LoadComicsException(exception.strerror)

        name_list = rar.namelist()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                try:
                    self.data.append(Page(rar.read(name), name, page_number))
                    page_number += 1
                except rarfile.BadRarFile as exc:
                    logger.exception('Error in read %s file. ' % name)

            self.progress.emit(idx * aux)

        rar.close()

        if not self.data:
            raise NoDataFindException

    @staticmethod
    def type_verify(file_name):
        return rarfile.is_rarfile(file_name)


class ComicZipLoader(ComicLoader):

    def __init__(self, extension):
        super(ComicZipLoader, self).__init__(extension)

    def load(self, file_name):

        try:
            zf = zipfile.ZipFile(file_name, 'r')
        except zipfile.BadZipfile as exception:
            raise InvalidTypeFileException(exception.message)
        except zipfile.LargeZipFile as exception:
            raise LoadComicsException(exception.message)
        except IOError as exception:
            raise LoadComicsException(exception.message)

        name_list = zf.namelist()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                try:
                    self.data.append(Page(zf.read(name), name, page_number))
                    page_number += 1
                except zipfile.BadZipfile as exc:
                    logger.exception('Error in read %s file' % name)

            self.progress.emit(idx * aux)

        zf.close()

        if not self.data:
            raise NoDataFindException('No one file is loaded!')

    @staticmethod
    def type_verify(file_name):
        return zipfile.is_zipfile(file_name)


class ComicTarLoader(ComicLoader):

    def __init__(self, extension):
        super(ComicTarLoader, self).__init__(extension)

    def load(self, file_name):

        try:
            tar = tarfile.open(file_name, 'r')
        except tarfile.CompressionError as exception:
            raise InvalidTypeFileException(exception.message)
        except IOError as exception:
            raise LoadComicsException(exception.message)

        name_list = tar.getnames()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                try:
                    data = tar.extractfile(name).read()
                    self.data.append(Page(data, name, page_number))
                    page_number += 1
                except tarfile.ExtractError as err:
                    logger.exception('%20s' % name)
                except tarfile.ReadError as err:
                    logger.exception('%20s' % name)

            self.progress.emit(idx * aux)

        tar.close()

        if not self.data:
            raise NoDataFindException

    @staticmethod
    def type_verify(file_name):
        return tarfile.is_tarfile(file_name)


class ComicFolderLoader(ComicLoader):

    def __init__(self, extension):
        super(ComicFolderLoader, self).__init__(extension)

    def load(self, dir_name):

        extension_list = ['.bmp', '.jpg', '.jpeg', '.gif', '.png', '.pbm',
                          '.pgm', '.ppm', '.tiff', '.xbm', '.xpm', '.webp']

        # get files with extension stored in ext
        file_list = []

        for ext in extension_list:
            file_list += glob.glob1(dir_name, '*' + ext)

        # sort list
        file_list.sort()

        aux = 100.0 / len(file_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(file_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                img_file = open(Utility.join_path(dir_name, '', name), 'r')
                self.data.append(Page(img_file.read(), name, page_number))
                page_number += 1
                img_file.close()

            self.progress.emit(idx * aux)

        if not self.data:
            raise NoDataFindException('')

    @staticmethod
    def type_verify(folder_name):
        return Utility.is_dir(folder_name)