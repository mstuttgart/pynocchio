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
#

import glob
from .utility import Utility
from .exception import NoDataFindException


class PathComicFilter:

    def __init__(self, extension_list):
        self.file_list = []
        self.current_path = None
        self.extension_list = extension_list
        self.current_index = None

    def parse(self, path):

        self.current_path = path
        self.file_list = []

        for ext in self.extension_list:
            self.file_list.extend(glob.glob1(path, ext))

        # sort list
        self.file_list.sort()
        # self.current_index = self.file_list.index()

    def is_first_comic(self, filename):
        try:
            return True if self.file_list[0] == filename else False
        except IndexError as exc:
            raise NoDataFindException(
                'PathComicFilter file list is empty!') from exc

    def is_last_comic(self, filename):
        try:
            return True if self.file_list[-1] == filename else False
        except IndexError as exc:
            raise NoDataFindException(
                'PathComicFilter file list is empty!') from exc

    def get_previous_comic(self, filename):

        if not self.is_first_comic(filename):
            name = self.file_list[self.file_list.index(filename) - 1]
            return Utility.join_path(self.current_path, '', name)
        else:
            raise NoDataFindException('PathComicFilter reach first file!')

    def get_next_comic(self, filename):

        if not self.is_last_comic(filename):
            name = self.file_list[self.file_list.index(filename) + 1]
            return Utility.join_path(self.current_path, '', name)
        else:
            raise NoDataFindException('PathComicFilter reach last file!')
