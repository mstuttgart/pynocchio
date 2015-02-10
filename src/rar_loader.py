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

        if not rarfile.is_rarfile(file_name) or not isinstance(file_name, str):
            return False

        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError, err:
            print '%20s  %s' % (file_name, err)
            return False

        name_list = rar.namelist()
        name_list.sort()

        list_size = len(name_list)
        count = 1

        for name in name_list:
            file_extension = Utility.get_file_extension(name)

            if not rar.getinfo(name).isdir() and file_extension.lower() in\
                    self.extension:
                self.data.append({'data': rar.read(name), 'name': name})
                self.progress.emit(count * 100/list_size)

            count += 1

        self.done.emit()
        rar.close()
        return True

