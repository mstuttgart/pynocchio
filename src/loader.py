# -*- coding:utf-8 -*-
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

from os import path
from PyQt4 import QtCore


class Loader(QtCore.QObject):
    def __init__(self, parent=None):
        super(Loader, self).__init__(parent)
        self.extension = ['.png', '.jpg', '.jpeg', '.gif']

    def load_file(self, file_name):
        pages = []

        path_head, path_tail = path.split(str(file_name))
        self._load_core(pages, file_name)

        if not pages:
            print "Load Comic failed!"

        return pages, path_head, path_tail

    def _load_core(self, pages, file_name):
        pass

