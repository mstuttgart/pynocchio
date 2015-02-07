# -*- coding:utf-8 -*-
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import zipfile
from PyQt4 import QtCore

from loader import Loader
from progress_dialog import ProgressDialog
from utility import Utility
from page import Page


class ZipLoader(Loader):

    def __init__(self):
        super(ZipLoader, self).__init__()

    def load(self, file_name):

        if not self.is_zip_file(file_name):
            return False

        file_name = str(file_name)

        try:
            zf = zipfile.ZipFile(file_name, 'r')
        except zipfile.BadZipfile, err:
            print '%20s  %s' % (file_name, err)
            return False
        except zipfile.LargeZipFile, err:
            print '%20s  %s' % (file_name, err)
            return False

        self._clear_data()
        name_list = zf.namelist()
        name_list.sort()

        # dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0,
        #                                      len(name_list))
        # dlg.setWindowTitle('Loading Comic File')
        # dlg.show()
        #
        # count_page = 1

        for info in name_list:
            # file_extension = Utility.get_file_extension(info)

            # QtCore.QCoreApplication.instance().processEvents()
            # if dlg.wasCanceled():
            #     raise GeneratorExit
            # dlg.setValue(name_list.index(info))

            if Utility.get_file_extension(info).lower() in self.extension:
                self.data.append({'data': zf.read(info), 'name': info})
                # count_page += 1

        zf.close()

        return True

    # def _load_core(self, pages, file_name):
    #
    #     zf = None
    #     file_name = str(file_name)
    #
    #     try:
    #         zf = zipfile.ZipFile(file_name, 'r')
    #     except zipfile.BadZipfile, err:
    #         print '%20s  %s' % (file_name, err)
    #     except zipfile.LargeZipFile, err:
    #         print '%20s  %s' % (file_name, err)
    #
    #     name_list = zf.namelist()
    #     name_list.sort()
    #
    #     # dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0,
    #     #                                      len(name_list))
    #     # dlg.setWindowTitle('Loading Comic File')
    #     # dlg.show()
    #     #
    #     count_page = 1
    #     for info in name_list:
    #         _, file_extension = os.path.splitext(info)
    #
    #         # QtCore.QCoreApplication.instance().processEvents()
    #         # if dlg.wasCanceled():
    #         #     raise GeneratorExit
    #         # dlg.setValue(name_list.index(info))
    #
    #         if file_extension.lower() in self.extension:
    #             pages.append(Page(zf.read(info), info, count_page))
    #             count_page += 1
    #
    #     zf.close()

    @staticmethod
    def is_zip_file(file_name):
        return zipfile.is_zipfile(str(file_name))
