# -*- coding: UTF-8 -*-
import zipfile
import os.path
import loader
from page import Page


class ZipLoader(loader.Loader):

    def __init__(self, parent=None):
        super(ZipLoader, self).__init__(parent)

    def _load_core(self, pages, file_name):

        zf = None
        file_name = str(file_name)

        try:
            zf = zipfile.ZipFile(file_name, 'r')
        except zipfile.BadZipfile, err:
            print '%20s  %s' % (file_name, err)
        except zipfile.LargeZipFile, err:
            print '%20s  %s' % (file_name, err)

        name_list = zf.namelist()
        name_list.sort()

        for info in name_list:
            _, file_extension = os.path.splitext(info)

            if file_extension.lower() in self.extension:
                pages.append(Page(zf.read(info), info, name_list.index(info) + 1))
                # pages.
                # page_data.append(zf.read(info))
                # page_title.append(info)

        zf.close()

    @staticmethod
    def is_zip_file(file_name):
        return zipfile.is_zipfile(str(file_name))
