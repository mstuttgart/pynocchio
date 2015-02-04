# -*- coding: UTF-8 -*-

from os import path
from PyQt4 import QtCore


class Loader(QtCore.QObject):
    def __init__(self, parent=None):
        super(Loader, self).__init__(parent)
        self.extension = ['.png', '.jpg', '.jpeg', '.gif']

    def load_file(self, file_name):
        pages = []

        path_head, path_tail = path.split(str(file_name))
        self._load_core(pages, file_name)

        if not pages:
            print "Load Comic failed!"

        return pages, path_head, path_tail

    def _load_core(self, pages, file_name):
        pass

