# -*- coding: UTF-8 -*-

import os
from PySide.QtGui import QMessageBox


class Loader(object):

    def __init__(self):
        super(Loader, self).__init__()

        self.extension = ['.png', '.jpg', '.jpeg', '.gif']

    def load_file(self, file_name):

        data_pages = []
        page_titles = []

        path_head, path_tail = os.path.split(file_name)
        self._load_core(data_pages, page_titles, file_name)

        if len(data_pages) == 0:
            # QMessageBox.information(self, self.tr('Error'), self.tr("Load Comic failed!"))
            print "Load Comic failed!"

        return data_pages, page_titles, path_head, path_tail

    def _load_core(self, page_data, page_title, file_name):
        pass
