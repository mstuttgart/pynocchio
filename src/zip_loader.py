# -*- coding: UTF-8 -*-
import zipfile
import os.path
from PyQt4 import QtCore

import loader
import progress_dialog
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

        dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0,
                                             len(name_list))
        dlg.setWindowTitle('Loading Comic File')
        dlg.show()

        count_page = 1
        for info in name_list:
            _, file_extension = os.path.splitext(info)

            QtCore.QCoreApplication.instance().processEvents()
            if dlg.wasCanceled():
                raise GeneratorExit
            dlg.setValue(name_list.index(info))

            if file_extension.lower() in self.extension:
                pages.append(Page(zf.read(info), info, count_page))
                count_page += 1

        zf.close()

    @staticmethod
    def is_zip_file(file_name):
        return zipfile.is_zipfile(str(file_name))
