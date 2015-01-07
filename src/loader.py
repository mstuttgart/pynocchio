# -*- coding: UTF-8 -*-

from os import path
from PySide import QtCore
from PySide import QtGui


class Loader(QtCore.QObject):

    def __init__(self, parent=None):
        super(Loader, self).__init__(parent)
        self.extension = ['.png', '.jpg', '.jpeg', '.gif']

    def load_file(self, file_name):
        data_pages = []
        page_titles = []

        path_head, path_tail = path.split(file_name)
        self._load_core(data_pages, page_titles, file_name)

        if len(data_pages) == 0:
            QtGui.QMessageBox.information(self, self.tr('Error'), self.tr("Load Comic failed!"))
            print "Load Comic failed!"

        return data_pages, page_titles, path_head, path_tail

    def _load_core(self, page_data, page_title, file_name):
        pass

