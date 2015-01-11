# -*- coding: UTF-8 -*-

import os.path
import rarfile
import loader
from page import Page


class RarLoader(loader.Loader):
    def __init__(self, parent=None):
        super(RarLoader, self).__init__(parent)

    def _load_core(self, pages, file_name):

        file_name = str(file_name)
        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError, err:
            print '%20s  %s' % (file_name, err)
            return

        name_list = rar.namelist()
        name_list.sort()

        for name in name_list:
            _, file_extension = os.path.splitext(name)

            if not rar.getinfo(name).isdir() and file_extension.lower() in self.extension:
                pages.append(Page(rar.read(name), name, name_list.index(name) + 1))
                # data = rar.read(name)
                # pages.append(data)
                # page_title.append(name)

        rar.close()

    @staticmethod
    def is_rar_file(file_name):
        return rarfile.is_rarfile(str(file_name))
