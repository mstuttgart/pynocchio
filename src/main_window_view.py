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


class MainWindowView(MainWindowBase, MainWindowForm):
    def __init__(self, controller):
        super(MainWindowView, self).__init__()
        self.setupUi(self)

        self.controller = controller

        self.action_open.triggered.connect(self.controller.open)
        self.action_save_image.triggered.connect(self.controller.save_image)

        self.action_next_page.triggered.connect(self.controller.next_page)
        self.action_previous_page.triggered.connect(self.controller.previous_page)
        self.action_first_page.triggered.connect(self.controller.first_page)
        self.action_last_page.triggered.connect(self.controller.last_page)
        self.action_go_to_page.triggered.connect(self.controller.go_to_page)
        self.action_next_comic.triggered.connect(self.controller.next_comic)
        self.action_previous_comic.triggered.connect(self.controller.previous_comic)

        self.action_rotate_left.triggered.connect(self.controller.rotate_left)
        self.action_rotate_right.triggered.connect(self.controller.rotate_right)
        self.action_fullscreen.triggered.connect(self.controller.fullscreen)

        self.action_add_bookmark.triggered.connect(self.controller.add_bookmark)
        self.action_remove_bookmark.triggered.connect(self.controller.remove_bookmark)
        self.action_bookmark_manager.triggered.connect(self.controller.bookmark_manager)
        self.action_show_toolbar.triggered.connect(self.controller.show_toolbar)
        self.action_show_statusbar.triggered.connect(self.controller.show_statusbar)
        self.action_show_toolbar.triggered.connect(self.controller.show_toolbar)

        self.action_preference_dialog.triggered.connect(
            self.controller.preference_dialog)

        self.action_about.triggered.connect(self.controller.about)
        self.action_about_qt.triggered.connect(self.controller.about_qt)
        self.action_exit.triggered.connect(self.controller.exit)

        self.action_group_view = QtGui.QActionGroup(self)

        self.action_group_view.addAction(self.action_original_fit)
        self.action_group_view.addAction(self.action_vertical_adjust)
        self.action_group_view.addAction(self.action_horizontal_adjust)
        self.action_group_view.addAction(self.action_best_fit)

        # self.action_original_fit.triggered.connect(
        #     self.controller.group_view_adjust)
        # self.action_vertical_adjust.triggered.connect(
        #     self.controller.group_view_adjust)
        # self.action_horizontal_adjust.triggered.connect(
        #     self.controller.group_view_adjust)
        # self.action_best_fit.triggered.connect(
        #     self.controller.group_view_adjust)

        self._centralize_window()

    def _centralize_window(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        x_center = (screen.width() - size.width()) / 2
        y_center = (screen.height() - size.height()) / 2
        self.move(x_center, y_center)
        self.setMinimumSize(QtGui.QApplication.desktop().screenGeometry().size() * 0.8)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F:
            self.controller.fullscreen()
        elif event.key() == QtCore.Qt.Key_Escape and self.isFullScreen():
            self.controller.fullscreen()
        else:
            super(MainWindowView, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        if args[0].button() == QtCore.Qt.LeftButton:
            self.controller.fullscreen()
        else:
            super(MainWindowView, self).mousePressEvent(*args, **kwargs)
