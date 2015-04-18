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

import tarfile

from loader import Loader
from utility import Utility


class TarLoader(Loader):
    def __init__(self, extension):
        super(TarLoader, self).__init__(extension)

    def load(self, file_name):

        if not tarfile.is_tarfile(file_name) or not isinstance(file_name, str):
            return False

        try:
            tar = tarfile.open(file_name, 'r')
        except tarfile.CompressionError, err:
            print '%20s  %s' % (file_name, err)
            return False

        name_list = tar.getnames()
        name_list.sort()

        list_size = len(name_list)
        count = 1

        for name in name_list:
            file_extension = Utility.get_file_extension(name)

            if not tar.getmember(name).isdir() and file_extension.lower() in \
                    self.extension:
                data = None
                try:
                    data = tar.extractfile(name).read()
                except tarfile.ExtractError, err:
                    print '%20s  %s' % (name, err)
                except tarfile.ReadError, err:
                    print '%20s  %s' % (name, err)

                if data:
                    self.data.append({'data': data, 'name': name})
                    self.progress.emit(count * 100 / list_size)
            count += 1

        self.done.emit()
        tar.close()
        return True
