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

from PyQt4 import QtCore


class Loader(object):
    
    progress = QtCore.pyqtSignal(int)
    done = QtCore.pyqtSignal()

    def __init__(self, extension):

        if not isinstance(extension, list):
            raise TypeError

        self.extension = extension
        self.data = []

    def load(self, file_name):
        raise NotImplementedError("Must subclass me")

    def length_data(self):
        return len(self.data)

    def _clear_data(self):
        self.data = []
