# -*- coding: UTF-8 -*-

from PyQt4 import QtCore
import fnmatch
import os.path

import loader
from page import Page


class FolderLoader(loader.Loader):
    def _load_core(self, pages, file_name):

        files_list = []

        for dir_path, dir_names, files in os.walk(file_name):
            for extension in ('*.jpg', '*.jpeg', '*.gif', '*.png'):
                for f in fnmatch.filter(files, extension):
                    files_list.append(os.path.join(dir_path, f))

        for f in files_list:
            q_file = QtCore.QFile(f)
            q_file.open(QtCore.QIODevice.ReadOnly)
            pages.append(Page(q_file.readAll(), f, files_list.index(f) + 1))

    @staticmethod
    def is_folder(file_name):
        return os.path.isdir(file_name)
