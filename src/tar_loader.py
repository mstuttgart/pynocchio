# -*- coding: UTF-8 -*-

import tarfile
from loader import *


class TarLoader(Loader):

    def _load_core(self, page_data, page_title, file_name):

        tar = tarfile.open(file_name, 'r')

        name_list = tar.getnames()
        name_list.sort()

        for filename in name_list:

            if not tar.getmember(filename).isdir():

                data = tar.extractfile(filename).read()

                page_data.append(data)
                page_title.append(filename)

        tar.close()

    @staticmethod
    def is_tar_file(file_name):
        return tarfile.is_tarfile(file_name)
