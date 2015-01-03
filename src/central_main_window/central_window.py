# -*- coding: UTF-8 -*-

from PySide import QtGui


class CentralWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(CentralWindow, self).__init__(parent)
        self._adjust_main_window()

    def _adjust_main_window(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        x_center = (screen.width() - size.width()) / 2
        y_center = (screen.height() - size.height()) / 2
        self.move(x_center, y_center)
        self.setMinimumSize(QtGui.QApplication.desktop().screenGeometry().size() * 0.8)
