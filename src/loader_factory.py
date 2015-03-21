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
from zip_loader import ZipLoader
from rar_loader import RarLoader
from tar_loader import TarLoader

product = {
    '.zip': ZipLoader,
    '.cbz': ZipLoader,
    '.rar': RarLoader,
    '.cbr': RarLoader,
    '.tar': TarLoader,
    '.cbt': TarLoader,
}


class LoaderFactory(object):

    @staticmethod
    def create_loader(extension):

        image_extensions = ['.bmp', '.jpg', '.jpeg', '.gif', '.png', '.pbm',
                            '.pgm', '.ppm', '.tiff', '.xbm', '.xpm']

        if extension in product:
            return product[extension](image_extensions)
