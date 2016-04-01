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

from qwebimage_widget import QWebImageWidget
from status_bar import StatusBar
from utility import Utility

root_dir = Utility.get_parent_path(__file__)

MainWindowForm, MainWindowBase = \
    uic.loadUiType(Utility.join_path(root_dir, 'gui', 'main_window_view.ui'))


class MainWindowView(MainWindowBase, MainWindowForm):
    def __init__(self, controller):
        super(MainWindowView, self).__init__()
        self.setupUi(self)

        self.controller = controller

        self.web_view = None
        self.current_view_container = self.qscroll_area_viewer

        self.global_shortcuts = []

        self.statusbar = StatusBar(self)
        self.setStatusBar(self.statusbar)

        self._create_connections(controller)
        self._centralize_window()
        self._define_global_shortcuts(controller)

    def _create_connections(self, controller):

        self.action_open.triggered.connect(controller.open)
        self.action_save_image.triggered.connect(controller.save_image)
        self.action_open_online.triggered.connect(controller.open_online)

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

        self.menu_recent_files.aboutToShow.connect(
            controller.update_recent_files_menu)

        actions = self.menu_recent_files.actions()
        for rf in actions:
            rf.triggered.connect(controller.load_recent_file)

        self.menu_recent_bookmarks.aboutToShow.connect(
            controller.update_bookmarks_menu)

        actions = self.menu_recent_bookmarks.actions()
        for bk in actions:
            bk.triggered.connect(controller.load_bookmark)

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

        action_list = self.menu_file.actions()
        action_list += self.menu_view.actions()
        action_list += self.menu_navegation.actions()
        action_list += self.menu_bookmarks.actions()

        for action in action_list:
            action.setEnabled(True)

    def update_status_bar(self, page_number, total_pages, page_title,
                          page_width, page_height):

        if self.statusbar.isVisible():
            self.statusbar.set_comic_page(page_number, total_pages)
            self.statusbar.set_page_resolution(page_width, page_height)
            self.statusbar.set_comic_path(page_title)

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
        if content and isinstance(content, QtGui.QPixmap):
            self.label.setPixmap(content)
            self.current_view_container.reset_scroll_position()

    def update_current_view_container_size(self):
        self.set_viewer_content(self.controller.model.get_current_page())

    def get_current_view_container_size(self):
        return self.current_view_container.size()

    def change_background_color(self, color):
        self.current_view_container.change_background_color(color)

    @QtCore.pyqtSlot()
    def on_action_show_toolbar_triggered(self):
        if self.action_show_toolbar.isChecked():
            self.toolbar.show()
        else:
            self.toolbar.hide()

    @QtCore.pyqtSlot()
    def on_action_show_statusbar_triggered(self):
        if self.action_show_statusbar.isChecked():
            self.statusbar.show()
        else:
            self.statusbar.hide()

    @QtCore.pyqtSlot()
    def on_action_fullscreen_triggered(self):

        if self.isFullScreen():
            self.menubar.show()
            self.toolbar.show()
            self.statusbar.show()
            self.showMaximized()

            for sc in self.global_shortcuts:
                sc.setEnabled(False)
        else:
            self.menubar.hide()
            self.toolbar.hide()
            self.statusbar.hide()
            self.showFullScreen()
            for sc in self.global_shortcuts:
                sc.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_action_about_triggered(self):

        # text = '<p><justify><a ' \
        #        'href=https://github.com/pynocchio>Pynocchio Comic ' \
        #        'Reader</a> is an image viewer <br>' \
        #        'specifically designed  to ' \
        #        'handle comic books is licensed <br>under the ' \
        #        'GPLv3.<justify></p>'\
        #        '<br>Copyright (C) 2014-2015 ' \
        #        '<a href=https://github.com/mstuttgart>' \
        #        'Michell Stuttgart Faria</a>'\
        #        '<br>Pynocchio use <a href=http://freeiconmaker.com>Free Icon ' \
        #        'Maker</a> to build icon set and <br>'\
        #        '<a href=https://github.com/mstuttgart/elementary3-icon-theme ' \
        #        '>Elementary OS 3.1 icons</a>.</p></justify>'
        #
        # QtGui.QMessageBox().about(self, self.tr('About Pynocchio Comic Reader'),
        #                           self.tr(text))

        import about_dialog
        ab_dlg = about_dialog.AboutDialog()
        ab_dlg.show()
        ab_dlg.exec_()

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
        super(MainWindowView, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        if args[0].button() == QtCore.Qt.LeftButton:
            self.on_action_fullscreen_triggered()
        super(MainWindowView, self).mousePressEvent(*args, **kwargs)

    def resizeEvent(self, *args, **kwargs):
        self.update_current_view_container_size()
        super(MainWindowView, self).resizeEvent(*args, **kwargs)
