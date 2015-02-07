# coding=UTF-8
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

import rarfile
from PyQt4.QtCore import QCoreApplication

from loader import Loader
import progress_dialog
from page import Page
from utility import Utility


class RarLoader(Loader):

    def __init__(self):
        super(RarLoader, self).__init__()

    def load(self, file_name):

        file_name = str(file_name)

        if not self.is_rar_file(file_name):
            return False

        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError, err:
            print '%20s  %s' % (file_name, err)
            return False

        name_list = rar.namelist()
        name_list.sort()

        for name in name_list:
            file_extension = Utility.get_file_extension(name.encode('utf-8'))

            if not rar.getinfo(name).isdir() and file_extension.lower() in\
                    self.extension:
                self.data.append({'data': rar.read(name), 'name': name})

        rar.close()
        return True

    @staticmethod
    def is_rar_file(file_name):
        return rarfile.is_rarfile(str(file_name))
