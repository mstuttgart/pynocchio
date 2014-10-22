# -*- coding: UTF-8 -*-

from loader import *
import tarfile
import os.path


class TarLoader(Loader):

    def __init__(self):
        super(TarLoader, self).__init__()

    def _load_core(self, page_data, page_title, file_name):

        tar = tarfile.open(file_name, 'r')

        name_list = tar.getnames()
        name_list.sort()

        for filename in name_list:

            _, file_extension = os.path.splitext(filename)

            if not tar.getmember(filename).isdir() and file_extension in self.extension:

                data = tar.extractfile(filename).read()
                page_data.append(data)
                page_title.append(filename)

        tar.close()

    @staticmethod
    def is_tar_file(file_name):
        return tarfile.is_tarfile(file_name)
