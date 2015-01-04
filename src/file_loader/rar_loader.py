# -*- coding: UTF-8 -*-

import os.path
import rarfile

from file_loader import loader


class RarLoader(loader.Loader):
    def __init__(self, parent=None):
        super(RarLoader, self).__init__(parent)

    def _load_core(self, page_data, page_title, file_name):

        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError, err:
            print '%20s  %s' % (file_name, err)
            return

        name_list = rar.namelist()
        name_list.sort()

        for filename in name_list:

            _, file_extension = os.path.splitext(filename)

            if not rar.getinfo(filename).isdir() and file_extension.lower() in self.extension:
                data = rar.read(filename)
                page_data.append(data)
                page_title.append(filename)

        rar.close()

    @staticmethod
    def is_rar_file(file_name):
        return rarfile.is_rarfile(file_name)
