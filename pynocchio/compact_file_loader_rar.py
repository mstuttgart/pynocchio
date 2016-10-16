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
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class RarLoader(Loader):

    def __init__(self, extension):
        Loader.__init__(self, extension)

    def load(self, file_name):
        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError as exception:
            raise InvalidTypeFileException(exception.message)
        except IOError as exception:
            raise LoadComicsException(exception.strerror)

        name_list = rar.namelist()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                try:
                    self.data.append(Page(rar.read(name), name, page_number))
                    page_number += 1
                except rarfile.BadRarFile as exc:
                    logger.exception('Error in read %s file. ' % name)

            self.progress.emit(idx * aux)

        rar.close()

        if not self.data:
            raise NoDataFindException

    @staticmethod
    def type_verify(file_name):
        return rarfile.is_rarfile(file_name)
