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


class PathComicFilter:

    def __init__(self, extension_list):
        self.file_list = []
        self.current_path = None
        self.extension_list = extension_list

    def parse(self, path):

        self.current_path = path
        self.file_list = []

        for ext in self.extension_list:
            self.file_list += glob.glob1(path, ext)

        # sort list
        self.file_list.sort()

    def is_first_comic(self, filename):
        return True if self.file_list[0] == filename else False

    def is_last_comic(self, filename):
        return True if self.file_list[-1] == filename else False

    def get_previous_comic(self, filename):
        name = self.file_list[self.file_list.index(filename) - 1]
        return Utility.join_path(self.current_path, '', name)

    def get_next_comic(self, filename):
        name = self.file_list[self.file_list.index(filename) + 1]
        return Utility.join_path(self.current_path, '', name)
