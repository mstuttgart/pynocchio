# -*- coding: UTF-8 -*-

import tarfile
import os.path
import loader
from page import Page


class TarLoader(loader.Loader):
    def __init__(self, parent=None):
        super(TarLoader, self).__init__(parent)

    def _load_core(self, pages, file_name):

        try:
            tar = tarfile.open(file_name, 'r')
        except:
            raise tarfile.CompressionError

        name_list = tar.getnames()
        name_list.sort()

        for name in name_list:
            _, file_extension = os.path.splitext(name)

            if not tar.getmember(name).isdir() and file_extension.lower() in self.extension:

                try:
                    data = tar.extractfile(name).read()
                except tarfile.ExtractError, err:
                    print '%20s  %s' % (name, err)
                except tarfile.ReadError, err:
                    print '%20s  %s' % (name, err)

                pages.append(Page(data, name, name_list.index(name) + 1))
                # pages.append(data)
                # page_title.append(name)

        tar.close()

    @staticmethod
    def is_tar_file(file_name):
        return tarfile.is_tarfile(file_name)
