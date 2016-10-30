# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

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

import glob

from .core.page import Page
from .core.pynocchio_exception import NoDataFindException
from .core.utility import Utility
from .compact_file_loader import Loader


class FolderLoader(Loader):

    def __init__(self, extension):
        super(FolderLoader, self).__init__(extension)

    def load(self, dir_name):

        extension_list = ['.bmp', '.jpg', '.jpeg', '.gif', '.png', '.pbm',
                          '.pgm', '.ppm', '.tiff', '.xbm', '.xpm', '.webp']

        # get files with extension stored in ext
        file_list = []

        for ext in extension_list:
            file_list += glob.glob1(dir_name, '*' + ext)

        # sort list
        file_list.sort()

        aux = 100.0 / len(file_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(file_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                img_file = open(Utility.join_path(dir_name, '', name), 'r')
                self.data.append(Page(img_file.read(), name, page_number))
                page_number += 1
                img_file.close()

            self.progress.emit(idx * aux)

        if not self.data:
            raise NoDataFindException('')

    @staticmethod
    def type_verify(folder_name):
        return Utility.is_dir(folder_name)
