# -*- coding: UTF-8 -*-

import rarfile
from loader import *


class RarLoader(Loader):

    def _load_core(self, page_data, page_title, file_name):

        rar = rarfile.RarFile(file_name, 'r')

        for info in rar.infolist():

            if not info.isdir():

                data = rar.read(info.filename)

                page_data.append(data)
                page_title.append(info.filename)

        rar.close()

    @staticmethod
    def is_rar_file(file_name):
        return rarfile.is_rarfile(file_name)
