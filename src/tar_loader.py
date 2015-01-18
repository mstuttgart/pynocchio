# -*- coding: UTF-8 -*-

import tarfile
import os.path
import loader
import progress_dialog
from page import Page
from PyQt4.QtCore import QCoreApplication


class TarLoader(loader.Loader):
    def __init__(self, parent=None):
        super(TarLoader, self).__init__(parent)

    def _load_core(self, pages, file_name):

        file_name = str(file_name)

        try:
            tar = tarfile.open(file_name, 'r')
        except:
            raise tarfile.CompressionError

        name_list = tar.getnames()
        name_list.sort()

        dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0, len(name_list))
        dlg.setWindowTitle('Loading Comic File')
        dlg.show()

        count_page = 1
        for name in name_list:
            _, file_extension = os.path.splitext(name)

            dlg.setValue(name_list.index(name))
            QCoreApplication.instance().processEvents()
            if dlg.wasCanceled():
                raise GeneratorExit

            if not tar.getmember(name).isdir() and file_extension.lower() in self.extension:

                data = None
                try:
                    data = tar.extractfile(name).read()
                except tarfile.ExtractError, err:
                    print '%20s  %s' % (name, err)
                except tarfile.ReadError, err:
                    print '%20s  %s' % (name, err)

                if data:
                    pages.append(Page(data, name, count_page))
                    count_page += 1

        tar.close()

    @staticmethod
    def is_tar_file(file_name):
        return tarfile.is_tarfile(str(file_name))
