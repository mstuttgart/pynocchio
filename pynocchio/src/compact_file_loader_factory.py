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

import pynocchio.src.compact_file_loader_zip as compact_file_loader_zip
import pynocchio.src.compact_file_loader_rar as compact_file_loader_rar
import pynocchio.src.compact_file_loader_tar as compact_file_loader_tar

PRODUCT = {
    '.zip': compact_file_loader_zip.ZipLoader,
    '.cbz': compact_file_loader_zip.CbzLoader,
    '.rar': compact_file_loader_rar.RarLoader,
    '.cbr': compact_file_loader_rar.CbrLoader,
    '.tar': compact_file_loader_tar.TarLoader,
    '.cbt': compact_file_loader_tar.CbtLoader,
}


class LoaderFactory(object):

    @staticmethod
    def create_loader(compact_file_extension, data_extension):
        if compact_file_extension in PRODUCT:
            return PRODUCT[compact_file_extension](data_extension)

        return None
