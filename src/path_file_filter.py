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
#

import os
import glob
from utility import Utility


class PathFileFilter(object):

    def __init__(self, extension_list):
        self._current_path = None
        self._previous_path = None
        self._next_path = None
        self.extension_list = extension_list
        self.file_list = None

    def _parse_dir(self):

        dir_name = Utility.get_dir_name(self.current_path)
        file_name = Utility.get_base_name(self.current_path)

        # get files with extension stored in ext
        file_list = []
        for ext in self.extension_list:
            file_list += glob.glob1(dir_name, ext)

        # sort list
        file_list = [f.decode('utf-8') for f in file_list]
        file_list.sort()

        # current file index list
        current_index = file_list.index(file_name.decode('utf-8'))

        # find the next file path
        if current_index + 1 < len(file_list):
            self._next_path = dir_name + '/' + file_list[current_index + 1]
        else:
            self._next_path = None

        # find the previous file path
        if current_index > 0:
            self._previous_path = dir_name + '/' + file_list[current_index - 1]
        else:
            self._previous_path = None

        return file_list

    def parse(self, path):
        self._current_path = path
        self._previous_path = None
        self._next_path = None
        self.file_list = self._parse_dir()

    def is_first_file(self):
        file_name = Utility.get_base_name(self.current_path)
        index = self.file_list.index(file_name.decode('utf-8'))
        return True if index == 0 else False

    def is_last_file(self):
        file_name = Utility.get_base_name(self.current_path)
        index = self.file_list.index(file_name.decode('utf-8'))
        return True if index == len(self.file_list) - 1 else False

    @property
    def current_path(self):
        return self._current_path

    @current_path.setter
    def current_path(self, value):
        self._current_path = value
        self._parse_dir()

    @property
    def previous_path(self):
        return self._previous_path

    @property
    def next_path(self):
        return self._next_path
