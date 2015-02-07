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
import os


class Utility(object):

    @staticmethod
    def get_file_extension(file_name):

        if not isinstance(file_name, str):
            file_name = str(file_name)

        t = os.path.splitext(file_name)
        return t[1]

    @staticmethod
    def get_dir_name(file_path):
        return os.path.dirname(str(file_path))

    @staticmethod
    def get_base_name(file_path):
        return os.path.basename(str(file_path))

    @staticmethod
    def path_exist(file_path):
        return os.path.lexists(file_path)

    @staticmethod
    def is_dir(file_path):
        return os.path.isdir(file_path)

