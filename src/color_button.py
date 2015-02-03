# -*- coding: UTF-8 -*-
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
