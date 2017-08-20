# -*- coding: utf-8 -*-

from PyQt5 import QtCore

import glob
import logging

from .utility import get_file_extension, join_path, get_dir_name
from .utility import IMAGE_FILE_FORMATS
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

    def load(self, file_name):
        raise NotImplementedError('Must subclass me')

    @staticmethod
    def type_verify(file_name):
        pass


class ComicImageLoader(ComicLoader):

    def __init__(self):
        super(ComicImageLoader, self).__init__()

    def load(self, file_name):

        # get files with extension stored in ext
        file_list = []

        dir_name = get_dir_name(file_name)

        for ext in IMAGE_FILE_FORMATS:
            file_list += glob.glob1(dir_name, '*' + ext)

        # sort list
        file_list.sort()

        aux = 100.0 / len(file_list)
        page = 1
        self.data = []

        for idx, name in enumerate(file_list):

            if get_file_extension(name).lower() in IMAGE_FILE_FORMATS:

                with open(join_path('', dir_name, name), 'rb') as img:
                    self.data.append(Page(img.read(), name, page))
                    page += 1

            self.progress.emit(idx * aux)

        if not self.data:
            raise NoDataFindException('Image file not loaded!')
