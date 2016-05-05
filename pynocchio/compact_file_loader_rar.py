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

from pynocchio_exception import DependenceNotFoundException

try:
    import rarfile
except ImportError as err:
    msg = 'rarfile module not installed.\n' \
          'you not can load .rar and .cbr files.' \
          'Please install it using: sudo pip install rarfile\n'
    raise DependenceNotFoundException(msg)

from compact_file_loader import Loader
from utility import Utility
from page import Page
from pynocchio_exception import LoadComicsException
from pynocchio_exception import InvalidTypeFileException
from pynocchio_exception import NoDataFindException


class RarLoader(Loader):

    def __init__(self, extension):
        Loader.__init__(self, extension)

    def load(self, file_name):
        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError as excp:
            raise InvalidTypeFileException(excp.message)
        except IOError as excp:
            raise LoadComicsException(excp.strerror)

        name_list = rar.namelist()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                self.data.append(Page(rar.read(name), name, page_number))
                page_number += 1

            self.progress.emit(idx * aux)

        rar.close()

        if not self.data:
            raise NoDataFindException


class CbrLoader(RarLoader):

    def __init__(self, extension):
        RarLoader.__init__(self, extension)
