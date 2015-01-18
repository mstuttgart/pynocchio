# -*- coding: UTF-8 -*-

import os.path
import rarfile
import loader
import progress_dialog
from page import Page
from PyQt4.QtCore import QCoreApplication


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

        dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0, len(name_list))
        dlg.setWindowTitle('Loading Comic File')
        dlg.show()

        for name in name_list:
            _, file_extension = os.path.splitext(name)

            dlg.setValue(name_list.index(name))
            QCoreApplication.instance().processEvents()
            if dlg.wasCanceled():
                raise GeneratorExit

            if not rar.getinfo(name).isdir() and file_extension.lower() in self.extension:
                pages.append(Page(rar.read(name), name, name_list.index(name) + 1))

        rar.close()

    @staticmethod
    def is_rar_file(file_name):
        return rarfile.is_rarfile(str(file_name))
