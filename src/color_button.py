# -*- coding:utf-8 -*-
# Copyright (C) 2015  Michell Stuttgart

# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3.0 of the License, or (at
# your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui


class ColorButton(QtGui.QPushButton):

    def __init__(self, parent=None):
        super(ColorButton, self).__init__(parent)
        self.background_color = QtGui.QColor()

    def paintEvent(self, e):
        p = QtGui.QPainter(self)
        p.fillRect(0, 0, self.width(), self.height(), self.background_color)
        p.end()
        e.accept()

    def reset_background_color(self):
        self.background_color = QtGui.QColor()
