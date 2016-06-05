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

import compact_file_loader_tar
import compact_file_loader_zip
import compact_file_loader_rar

from pynocchio_exception import InvalidTypeFileException


class LoaderFactory(object):

    @staticmethod
    def create_loader(compact_file_extension, filename, data_extension):

        if compact_file_extension in ['.zip', '.cbz', '.rar', '.cbr', '.tar', '.cbt']:

            loaders = [
                compact_file_loader_zip.ZipLoader,
                compact_file_loader_rar.RarLoader,
                compact_file_loader_tar.TarLoader,
            ]

            for loader in loaders:
                if loader.type_verify(filename):
                    return loader(data_extension)

        raise InvalidTypeFileException('Invalid file extension: %s' % compact_file_extension)
