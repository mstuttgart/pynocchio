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

import zipfile
from .page import Page
from .pynocchio_exception import InvalidTypeFileException
from .pynocchio_exception import LoadComicsException
from .pynocchio_exception import NoDataFindException
from .utility import Utility

from .compact_file_loader import Loader
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ZipLoader(Loader):

    def __init__(self, extension):
        Loader.__init__(self, extension)

    def load(self, file_name):

        try:
            zf = zipfile.ZipFile(file_name, 'r')
        except zipfile.BadZipfile as exception:
            raise InvalidTypeFileException(exception.message)
        except zipfile.LargeZipFile as exception:
            raise LoadComicsException(exception.message)
        except IOError as exception:
            raise LoadComicsException(exception.message)

        name_list = zf.namelist()
        name_list.sort()
        aux = 100.0 / len(name_list)
        page_number = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if Utility.get_file_extension(name).lower() in self.extension:
                try:
                    self.data.append(Page(zf.read(name), name, page_number))
                    page_number += 1
                except zipfile.BadZipfile as exc:
                    logger.exception('Error in read %s file' % name)

            self.progress.emit(idx * aux)

        zf.close()

        if not self.data:
            raise NoDataFindException('No one file is loaded!')

    def type_verify(self, file_name):
        return zipfile.is_zipfile(file_name)
