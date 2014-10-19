# -*- coding: UTF-8 -*-

import rarfile
from loader import *


class RarLoader(Loader):

    def _load_core(self, page_data, page_title, file_name):

        rar = rarfile.RarFile(file_name, 'r')

        name_list = rar.namelist()
        name_list.sort()

        for filename in name_list:

            if not rar.getinfo(filename).isdir():

                data = rar.read(filename)

                page_data.append(data)
                page_title.append(filename)

        rar.close()

    @staticmethod
    def is_rar_file(file_name):
        return rarfile.is_rarfile(file_name)
