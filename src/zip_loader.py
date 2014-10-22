# -*- coding: UTF-8 -*-
__author__ = 'michell'

from loader import *
import zipfile
import os.path


class ZipLoader(Loader):

    def __init__(self):
        super(ZipLoader, self).__init__()

    def _load_core(self, page_data, page_title, file_name):

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

            if file_extension in self.extension:
                data = zf.read(info)
                page_data.append(data)
                page_title.append(info)

        zf.close()

    @staticmethod
    def is_zip_file(file_name):
        return zipfile.is_zipfile(file_name)
