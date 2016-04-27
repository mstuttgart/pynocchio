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

import tarfile

from compact_file_loader import Loader
from src.lib.utility import Utility
from page import Page
from pynocchio_exception import InvalidTypeFileException
from pynocchio_exception import LoadComicsException
from pynocchio_exception import NoDataFindException


class TarLoader(Loader):

    def __init__(self, extension):
        Loader.__init__(self, extension)

    def load(self, file_name):

        try:
            tar = tarfile.open(file_name, 'r')
        except tarfile.CompressionError as excp:
            raise InvalidTypeFileException(excp.message)
        except IOError as excp:
            raise LoadComicsException(excp.message)

        name_list = tar.getnames()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                try:
                    data = tar.extractfile(name).read()
                    self.data.append(Page(data, name, page_number))
                    page_number += 1
                except tarfile.ExtractError as err:
                    print '%20s  %s' % (name, err.message)
                except tarfile.ReadError as err:
                    print '%20s  %s' % (name, err.message)

            self.progress.emit(idx * aux)

        tar.close()

        if not self.data:
            raise NoDataFindException


class CbtLoader(TarLoader):

    def __init__(self, extension):
        TarLoader.__init__(self, extension)
