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
from PyQt4.QtCore import Qt

from qwebimage_widget import QWebImageWidget
from status_bar import StatusBar

MainWindowForm, MainWindowBase = uic.loadUiType('main_window.ui')


class MainWindowView(MainWindowBase, MainWindowForm):
    def __init__(self, controller):
        super(MainWindowView, self).__init__()
        self.setupUi(self)

        self.controller = controller

        self.web_view = None
        self.current_view_container = self.qscroll_area_viewer
        self.current_view_container.main_window_view = self
        self.current_view_container.main_window_controller = controller

        self.global_shortcuts = []

        self.statusbar = StatusBar(self)
        self.setStatusBar(self.statusbar)

        self._create_connections(controller)
        self._centralize_window()
        self._define_global_shortcuts(controller)

    def _create_connections(self, controller):

        self.action_open.triggered.connect(controller.open)
        self.action_save_image.triggered.connect(controller.save_image)
        self.action_online_comics.triggered.connect(controller.online_comics)

        self.action_next_page.triggered.connect(controller.next_page)
        self.action_previous_page.triggered.connect(controller.previous_page)

        self.action_first_page.triggered.connect(controller.first_page)
        self.action_last_page.triggered.connect(controller.last_page)
        self.action_go_to_page.triggered.connect(controller.go_to_page)
        self.action_next_comic.triggered.connect(controller.next_comic)
        self.action_previous_comic.triggered.connect(controller.previous_comic)

        self.action_rotate_left.triggered.connect(controller.rotate_left)
        self.action_rotate_right.triggered.connect(controller.rotate_right)

        self.action_add_bookmark.triggered.connect(controller.add_bookmark)
        self.action_remove_bookmark.triggered.connect(controller.remove_bookmark)
        self.action_bookmark_manager.triggered.connect(controller.bookmark_manager)
        self.action_show_toolbar.triggered.connect(controller.show_toolbar)
        self.action_show_statusbar.triggered.connect(controller.show_statusbar)
        self.action_show_toolbar.triggered.connect(controller.show_toolbar)

        self.action_preference_dialog.triggered.connect(
            controller.preference_dialog)

        self.action_group_view = QtGui.QActionGroup(self)

        self.action_group_view.addAction(self.action_original_fit)
        self.action_group_view.addAction(self.action_vertical_fit)
        self.action_group_view.addAction(self.action_horizontal_fit)
        self.action_group_view.addAction(self.action_best_fit)

        self.action_original_fit.triggered.connect(controller.original_fit)
        self.action_vertical_fit.triggered.connect(controller.vertical_fit)
        self.action_horizontal_fit.triggered.connect(controller.horizontal_fit)
        self.action_best_fit.triggered.connect(controller.best_fit)

    def _define_global_shortcuts(self, controller):

        sequence = {
            'Ctrl+Shift+Left': controller.previous_comic,
            'Ctrl+Left': controller.first_page,
            'Left': controller.previous_page,
            'Right': controller.next_page,
            'Ctrl+Right': controller.last_page,
            'Ctrl+Shift+Right': controller.next_comic,
            'Ctrl+R': controller.rotate_right,
            'Ctrl+Shift+R': controller.rotate_left,
        }

        for key, value in sequence.items():
            s = QtGui.QShortcut(QtGui.QKeySequence(key),
                                self.current_view_container, value)
            s.setEnabled(False)
            self.global_shortcuts.append(s)

    def enable_actions(self):

        self.action_save_image.setEnabled(True)

        self.action_fullscreen.setEnabled(True)
        self.action_original_fit.setEnabled(True)
        self.action_best_fit.setEnabled(True)
        self.action_horizontal_fit.setEnabled(True)
        self.action_vertical_fit.setEnabled(True)
        self.action_rotate_left.setEnabled(True)
        self.action_rotate_right.setEnabled(True)

        self.action_next_page.setEnabled(True)
        self.action_previous_page.setEnabled(True)
        self.action_first_page.setEnabled(True)
        self.action_last_page.setEnabled(True)
        self.action_go_to_page.setEnabled(True)
        self.action_next_comic.setEnabled(True)
        self.action_previous_comic.setEnabled(True)

        self.action_add_bookmark.setEnabled(True)
        self.action_remove_bookmark.setEnabled(True)

    def on_action_fullscreen_triggered(self):

        if self.isFullScreen():
            self.menubar.show()
            self.toolbar.show()
            self.statusbar.show()
            self.showMaximized()
            self.set_focus_on_toolbar()

            for sc in self.global_shortcuts:
                sc.setEnabled(False)
        else:
            self.menubar.hide()
            self.toolbar.hide()
            self.statusbar.hide()
            self.showFullScreen()
            for sc in self.global_shortcuts:
                sc.setEnabled(True)

    def _set_focus_on_viewer(self):
        # self.current_view_container.activateWindow()
        # self.current_view_container.setWindowState(QtCore.Qt.WindowActive)
        # self.current_view_container.setFocus(QtCore.Qt.ActiveWindowFocusReason)
        print

    def set_focus_on_toolbar(self):
        # self.toolbar.activateWindow()
        # self.toolbar.setWindowState(QtCore.Qt.WindowActive)
        # self.toolbar.setFocus(QtCore.Qt.ActiveWindowFocusReason)
        print

    def switch_to_web_view(self):
        if self.web_view is None:
            self.web_view = QWebImageWidget()

        self.current_view_container = self.web_view
        self.setCentralWidget(self.web_view)

    def switch_to_normal_view(self):
        self.setCentralWidget(self.qscroll_area_viewer)
        self.current_view_container = self.qscroll_area_viewer

    def _centralize_window(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        x_center = (screen.width() - size.width()) / 2
        y_center = (screen.height() - size.height()) / 2
        self.move(x_center, y_center)
        self.setMinimumSize(
            QtGui.QApplication.desktop().screenGeometry().size() * 0.8)

    def set_viewer_content(self, content):
        self.current_view_container.set_content(content)
        # self.set_focus_on_toolbar()
        # self._set_focus_on_viewer()

    def update_current_view_container_size(self, new_size):
        self.controller.update_current_view_container_size(new_size)

    def get_current_view_container_size(self):
        return self.current_view_container.size()

    @QtCore.pyqtSlot()
    def on_action_about_triggered(self):

        text = '<p><justify>The <a ' \
               'href=https://github.com/pynocchio>Pynocchio Comic ' \
               'Reader</a> is an image viewer <br>' \
               'specifically designed  to ' \
               'handle comic books is licensed <br>under the ' \
               'GPLv3.<justify></p>'\
               '<br>Copyright (C) 2014-2015 ' \
               '<a href=https://github.com/mstuttgart>' \
               'Michell Stuttgart Faria</a>'\
               '<br>Pynocchio use <a href=http://freeiconmaker.com>Free Icon ' \
               'Maker</a> to build icon set and <br>'\
               '<a href=https://github.com/mstuttgart/elementary3-icon-theme ' \
               '>Elementary OS 3.1 icons</a>.</p></justify>'

        QtGui.QMessageBox().about(self, self.tr('About Pynocchio Comic Reader'),
                                  self.tr(text))

    @QtCore.pyqtSlot()
    def on_action_about_qt_triggered(self):
        QtGui.QMessageBox().aboutQt(self, self.tr(u'About Qt'))

    @QtCore.pyqtSlot()
    def on_action_exit_triggered(self):
        super(MainWindowView, self).close()
        self.controller.exit()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F:
            self.on_action_fullscreen_triggered()
        else:
            super(MainWindowView, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        if args[0].button() == QtCore.Qt.LeftButton:
            self.on_action_fullscreen_triggered()
        else:
            super(MainWindowView, self).mousePressEvent(*args, **kwargs)
