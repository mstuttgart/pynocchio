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


class LoaderFactory(object):

    def __init__(self):
        super(LoaderFactory, self).__init__()

    @staticmethod
    def create_loader(extension):

        if extension == '.zip' or extension == '.cbz':
            import zip_loader
            return zip_loader.ZipLoader()
        elif extension == '.rar' or extension == '.cbr':
            import rar_loader
            return rar_loader.RarLoader()
        elif extension == '.tar' or extension == '.cbt':
            import tar_loader
            return tar_loader.TarLoader()
