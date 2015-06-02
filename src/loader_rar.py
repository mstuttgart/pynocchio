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

from pynocchio_exception import DependenceNotFoundException

try:
    import rarfile
except ImportError as err:
    msg = 'rarfile module not installed.\n' \
          'you not can load .rar and .cbr files.' \
          'Please install it using: sudo pip install rarfile\n'
    raise DependenceNotFoundException(msg)

from loader import Loader
from utility import Utility
from pynocchio_exception import LoadComicsException
from pynocchio_exception import InvalidTypeFileException
from pynocchio_exception import NoDataFindException


class RarLoader(Loader):

    EXTENSION = '.rar'

    def __init__(self, extension):
        super(RarLoader, self).__init__(extension)

    def load(self, file_name):

        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError as excp:
            raise InvalidTypeFileException(excp.message)
            # print '[ERROR]', excp.message
            # return False
        except IOError as excp:
            raise LoadComicsException(excp.strerror)
            # print '[ERROR]', excp.strerror
            # return False

        name_list = rar.namelist()
        name_list.sort()

        list_size = len(name_list)
        count = 1

        for name in name_list:
            file_extension = Utility.get_file_extension(name)

            if not rar.getinfo(name).isdir() and file_extension.lower() in \
                    self.extension:
                self.data.append({'data': rar.read(name), 'name': name})
                self.progress.emit(count * 100 / list_size)

            count += 1

        self.done.emit()
        rar.close()

        if not self.data:
            raise NoDataFindException

        # return True if self.data else False


class CbrLoader(RarLoader):

    EXTENSION = '.cbr'

    def __init__(self, extension):
        super(CbrLoader, self).__init__(extension)
