# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui

import glob
import logging
import zipfile
import rarfile
import tarfile

from .utility import get_file_extension, join_path, is_dir
from .comic import Page
from .exception import NoDataFindException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ComicLoader(QtCore.QObject):

    progress = QtCore.pyqtSignal(int)
    done = QtCore.pyqtSignal()

    def __init__(self):
        super(ComicLoader, self).__init__()
        self.data = []
        self.extension = [str(ext, encoding='utf8') for ext in
                          QtGui.QImageReader.supportedImageFormats()]

    def load(self, file_name):
        raise NotImplementedError("Must subclass me")

    @staticmethod
    def type_verify(file_name):
        raise NotImplementedError("Must subclass me")


class ComicRarLoader(ComicLoader):

    def __init__(self):
        super(ComicRarLoader, self).__init__()

    def load(self, file_name):

        with rarfile.RarFile(file_name, 'r') as rar:

            name_list = rar.namelist()
            name_list.sort()
            aux = 100.0 / len(name_list)
            page = 1
            self.data = []

            for idx, name in enumerate(name_list):

                if get_file_extension(name).lower() in self.extension:
                    try:
                        self.data.append(Page(rar.read(name), name, page))
                        page += 1
                    except rarfile.BadRarFile as exc:
                        logger.exception('Error in read %s file. %s' % (name,
                                                                        exc))

                self.progress.emit(idx * aux)

            if not self.data:
                raise NoDataFindException('No one file is loaded!')

    @staticmethod
    def type_verify(file_name):
        return rarfile.is_rarfile(file_name)


class ComicZipLoader(ComicLoader):

    def __init__(self):
        super(ComicZipLoader, self).__init__()

    def load(self, file_name):

        with zipfile.ZipFile(file_name, 'r') as zf:

            name_list = zf.namelist()
            name_list.sort()
            aux = 100.0 / len(name_list)
            page = 1
            self.data = []

            for idx, name in enumerate(name_list):

                if get_file_extension(name).lower() in self.extension:
                    try:
                        self.data.append(Page(zf.read(name), name, page))
                        page += 1
                    except zipfile.BadZipfile as exc:
                        logger.exception('Error in read %s file. %s' % (name,
                                                                        exc))

                self.progress.emit(idx * aux)

            if not self.data:
                raise NoDataFindException('No one file is loaded!')

    @staticmethod
    def type_verify(file_name):
        return zipfile.is_zipfile(file_name)


class ComicTarLoader(ComicLoader):

    def __init__(self):
        super(ComicTarLoader, self).__init__()

    def load(self, file_name):

        with tarfile.open(file_name, 'r') as tar:

            name_list = tar.getnames()
            name_list.sort()
            aux = 100.0 / len(name_list)
            page = 1
            self.data = []

            for idx, name in enumerate(name_list):

                if get_file_extension(name).lower() in self.extension:
                    try:
                        data = tar.extractfile(name).read()
                        self.data.append(Page(data, name, page))
                        page += 1
                    except tarfile.ExtractError as exc:
                        logger.exception('Error in extract %s file. %s' %
                                         (name, exc))
                    except tarfile.ReadError as exc:
                        logger.exception('Error in read %s file. %s' % (name,
                                                                        exc))

                self.progress.emit(idx * aux)

            if not self.data:
                raise NoDataFindException('No one file is loaded!')

    @staticmethod
    def type_verify(file_name):
        return tarfile.is_tarfile(file_name)


class ComicFolderLoader(ComicLoader):

    def __init__(self):
        super(ComicFolderLoader, self).__init__()

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
        page = 1
        self.data = []

        for idx, name in enumerate(file_list):

            if get_file_extension(name).lower() in self.extension:

                with open(join_path(dir_name, '', name), 'r') as img:
                    self.data.append(Page(img.read(), name, page))
                    page += 1

            self.progress.emit(idx * aux)

        if not self.data:
            raise NoDataFindException('Folder is not loaded!')

    @staticmethod
    def type_verify(folder_name):
        return is_dir(folder_name)
