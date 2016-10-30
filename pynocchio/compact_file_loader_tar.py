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

import logging
import tarfile

from .core.page import Page
from .core.pynocchio_exception import InvalidTypeFileException
from .core.pynocchio_exception import LoadComicsException
from .core.pynocchio_exception import NoDataFindException
from .core.utility import Utility
from .compact_file_loader import Loader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TarLoader(Loader):

    def __init__(self, extension):
        super(TarLoader, self).__init__(extension)

    def load(self, file_name):

        try:
            tar = tarfile.open(file_name, 'r')
        except tarfile.CompressionError as exception:
            raise InvalidTypeFileException(exception.message)
        except IOError as exception:
            raise LoadComicsException(exception.message)

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
                    logger.exception('%20s' % name)
                except tarfile.ReadError as err:
                    logger.exception('%20s' % name)

            self.progress.emit(idx * aux)

        tar.close()

        if not self.data:
            raise NoDataFindException

    @staticmethod
    def type_verify(file_name):
        return tarfile.is_tarfile(file_name)
