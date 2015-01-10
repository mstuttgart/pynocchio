# -*- coding: UTF-8 -*-

from PySide import QtCore
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
            qfile = QtCore.QFile(f)
            qfile.open(QtCore.QIODevice.ReadOnly)
            pages.append(Page(qfile.readAll(), f, files_list.index(f) + 1))
            # pages.append(qfile.readAll())
            # page_title.append(f)

    @staticmethod
    def is_folder(file_name):
        return os.path.isdir(file_name)
