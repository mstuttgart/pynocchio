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

import zipfile

from compact_file_loader import Loader
from utility import Utility
from page import Page
from pynocchio_exception import InvalidTypeFileException
from pynocchio_exception import LoadComicsException
from pynocchio_exception import NoDataFindException


class ZipLoader(Loader):

    def __init__(self, extension):
        super(ZipLoader, self).__init__(extension)

    def load(self, file_name):

        try:
            zf = zipfile.ZipFile(file_name, 'r')
        except zipfile.BadZipfile as excp:
            raise InvalidTypeFileException(excp.message)
        except zipfile.LargeZipFile as excp:
            raise LoadComicsException(excp.message)
        except IOError as excp:
            raise LoadComicsException(excp.message)

        name_list = zf.namelist()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                self.data.append(Page(zf.read(name), name, page_number))
                page_number += 1

            self.progress.emit(idx * aux)

        zf.close()

        if not self.data:
            raise NoDataFindException('No one file is loaded!')


class CbzLoader(ZipLoader):

    def __init__(self, extension):
        super(CbzLoader, self).__init__(extension)
