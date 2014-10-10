# -*- coding: UTF-8 -*-

import fnmatch
from PySide import QtCore
from loader import *


class FolderLoader(Loader):

    def _load_core(self, page_data, page_title, file_name):

        files_list = []

        # Percorremos diretorios e sub-diretorios procurando
        # arquivos com as extensoes abaixo
        for dirpath, dirnames, files in os.walk(file_name):

            for extension in ('*.jpg', '*.jpeg', '*.gif', '*.png'):

                for f in fnmatch.filter(files, extension):
                    files_list.append(os.path.join(dirpath, f))

        for f in files_list:

            qfile = QtCore.QFile(f)

            qfile.open(QtCore.QIODevice.ReadOnly)
            page_data.append(qfile.readAll())
            page_title.append(f)


    @staticmethod
    def is_folder(file_name):
        return os.path.isdir(file_name)
