# -*- coding: UTF-8 -*-

import tarfile
import os.path

from loader import Loader


class TarLoader(Loader):
    def __init__(self, parent=None):
        super(TarLoader, self).__init__(parent)

    def _load_core(self, page_data, page_title, file_name):

        try:
            tar = tarfile.open(file_name, 'r')
        except:
            raise tarfile.CompressionError

        name_list = tar.getnames()
        name_list.sort()

        for filename in name_list:

            _, file_extension = os.path.splitext(filename)

            if not tar.getmember(filename).isdir() and file_extension in self.extension:

                try:
                    data = tar.extractfile(filename).read()
                except tarfile.ExtractError, err:
                    print '%20s  %s' % (filename, err)
                except tarfile.ReadError, err:
                    print '%20s  %s' % (filename, err)

                page_data.append(data)
                page_title.append(filename)

        tar.close()

    @staticmethod
    def is_tar_file(file_name):
        return tarfile.is_tarfile(file_name)
