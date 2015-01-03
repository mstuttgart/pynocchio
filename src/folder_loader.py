# -*- coding: UTF-8 -*-

import fnmatch
from PySide import QtCore
import os.path

from src.file_loader.loader import Loader


class FolderLoader(Loader):

    def _load_core(self, page_data, page_title, file_name):

        files_list = []

        for dir_path, dir_names, files in os.walk(file_name):

            for extension in ('*.jpg', '*.jpeg', '*.gif', '*.png'):

                for f in fnmatch.filter(files, extension):
                    files_list.append(os.path.join(dir_path, f))

        for f in files_list:
            qfile = QtCore.QFile(f)

            qfile.open(QtCore.QIODevice.ReadOnly)
            page_data.append(qfile.readAll())
            page_title.append(f)

    @staticmethod
    def is_folder(file_name):
        return os.path.isdir(file_name)
