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

from PyQt5 import QtCore


class Loader(QtCore.QObject):

    progress = QtCore.pyqtSignal(int)
    done = QtCore.pyqtSignal()

    def __init__(self, extension):
        QtCore.QObject.__init__(self)
        self.extension = extension
        self.data = []

    @staticmethod
    def load(file_name):
        raise NotImplementedError("Must subclass me")

    def type_verify(self, file_name):
        raise NotImplementedError("Must subclass me")
