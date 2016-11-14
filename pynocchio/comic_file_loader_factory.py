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

from .exception import InvalidTypeFileException
from .utility import Utility
from .comic_file_loader import ComicZipLoader
from .comic_file_loader import ComicRarLoader
from .comic_file_loader import ComicTarLoader
from .comic_file_loader import ComicFolderLoader


class ComicLoaderFactory:

    @staticmethod
    def create_loader(filename, data_extension):

        if Utility.is_file(file_name=filename):

            loaders = [ComicZipLoader, ComicRarLoader, ComicTarLoader]

            # Return appropriate loader by with file compact coding
            for loader in loaders:
                if loader.type_verify(file_name=filename):
                    return loader(data_extension)

            raise InvalidTypeFileException('Invalid file extension: %s' %
                                           Utility.get_file_extension(
                                               filename))
        elif Utility.is_dir(filename):
            return ComicFolderLoader(data_extension)
        else:
            raise InvalidTypeFileException('File is not folder: %s' %
                                           Utility.get_file_extension(
                                               filename))
