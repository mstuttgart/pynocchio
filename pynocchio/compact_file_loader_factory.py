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

from .compact_file_loader_tar import TarLoader
from .compact_file_loader_zip import ZipLoader
from .compact_file_loader_rar import RarLoader
from .compact_folder_loader import FolderLoader

from .pynocchio_exception import InvalidTypeFileException
from .utility import Utility


class LoaderFactory:

    @staticmethod
    def create_loader(compact_file_extension, filename, data_extension):

        if Utility.is_file(file_name=filename):

            loaders = [ZipLoader, RarLoader, TarLoader]

            # Return appropriate loader by with file compact coding
            for loader in loaders:
                if loader.type_verify(file_name=filename):
                    return loader(data_extension)

            raise InvalidTypeFileException('Invalid file extension: %s' %
                                           compact_file_extension)

        elif Utility.is_dir(filename):
            return FolderLoader(data_extension)
