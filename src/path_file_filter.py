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


class PathFileFilter(object):

    def __init__(self, path, extension_list):
        self._current_path = path
        self._previous_path = None
        self._next_path = None
        self.extension_list = extension_list
        self._parse_dir()

    def _parse_dir(self):

        files = os.listdir(self.current_path)
        arquivos = [arq for arq in files if os.path.isfile(arq)]

        file_list = []

        # get files with extension stored in ext
        for ext in self.extension_list:
            file_list += [arq for arq in arquivos if arq.lower().endswith(ext)]

        # current dile index list
        current_index = file_list.index(self.current_path)

        # find the next file path
        if current_index + 1 < len(file_list):
            self._next_path = file_list[current_index + 1]
        else:
            self._next_path = None

        # find the previous file path
        if current_index - 1 > 0:
            self._previous_path = file_list[current_index - 1]
        else:
            self._previous_path = None

    def parse(self, path, extension_list):
        self._current_path = path
        self._previous_path = None
        self._next_path = None
        self.extension_list = extension_list
        self._parse_dir()

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