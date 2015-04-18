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

from model import Model
from recent_files_manager import RecentFileManager
from status_bar import StatusBar
from preference import Preference
from recent_file import RecenteFiles


MainWindowForm, MainWindowBase = uic.loadUiType('main_window.ui')


class MainWindow(MainWindowBase, MainWindowForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def _adjust_main_window(self):
        pass

    def _create_action_group_view(self):
        print

    def load(self, path, initial_page=0):
        pass

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

    def _on_action_group_view_adjust(self):
        print

    def _set_focus_on_viewer(self):
        print

    def _init_recent_files_menu(self):
        print

    def _update_recent_files_menu(self):
        print

    def _load_recent_file(self):
        print

    def _init_bookmark_menu(self):
        print

    def _update_bookmarks_menu(self):
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

    def _load_bookmark(self):
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

    def _update_view_actions(self):
        print

    def _update_status_bar(self):
        print

    @QtCore.pyqtSlot(int)
    def _set_zoom_factor(self, value):
        print

    def _enable_actions(self):
        print

    def _save_settings(self):
        print

    def _load_settings(self):
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
