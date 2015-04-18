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

from PyQt4 import QtGui, QtCore, uic


MainWindowForm, MainWindowBase = uic.loadUiType('main_window.ui')


class MainWindow(MainWindowBase, MainWindowForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    @QtCore.pyqtSlot()
    def on_action_open_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_save_image_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_next_page_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_previous_page_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_first_page_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_last_page_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_go_to_page_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_next_comic_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_previous_comic_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_rotate_left_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_rotate_right_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_fullscreen_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_add_bookmark_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_remove_bookmark_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_bookmark_manager_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_show_toolbar_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_show_statusbar_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_preference_dialog_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_about_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_about_qt_triggered(self):
        print

    @QtCore.pyqtSlot()
    def on_action_exit_triggered(self):
        print

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F:
            self.on_action_fullscreen_triggered()
        elif event.key() == QtCore.Qt.Key_Escape and self.isFullScreen():
            self.on_action_fullscreen_triggered()
        else:
            super(MainWindow, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        if args[0].button() == QtCore.Qt.LeftButton:
            self.on_action_fullscreen_triggered()
        else:
            super(MainWindow, self).mousePressEvent(*args, **kwargs)
