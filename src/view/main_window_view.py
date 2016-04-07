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

from PySide import QtGui, QtCore

from src.pynocchio_exception import InvalidTypeFileException
from src.pynocchio_exception import LoadComicsException

# SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
# print SCRIPT_DIRECTORY

# from qwebimage_widget import QWebImageWidget
# from status_bar import StatusBar
# from utility import Utility

from main_window_view_ui import Ui_MainWindowView


class MainWindowView(QtGui.QMainWindow):

    def __init__(self, model, parent=None):
        super(MainWindowView, self).__init__(parent)
        self.model = model

        self.ui = Ui_MainWindowView()
        self.ui.setupUi(self)

        self.global_shortcuts = []

        self._create_connections()
        self._centralize_window()
        self._define_global_shortcuts()

        self.model.scroll_area_size = self.get_current_view_container_size()

        self.model.load_progress.connect(
            self.ui.statusbar.set_progressbar_value)
        # self.model.load_done.connect(self.ui.statusbar.close_progress_bar)

    @QtCore.Slot()
    def on_action_open_triggered(self):

        filename = QtGui.QFileDialog().getOpenFileName(
            self, self.tr('open_comic_file'),
            self.model.current_directory,
            self.tr(
                'all_supported_files (*.zip *.cbz *.rar *.cbr *.tar *.cbt);; '
                'zip_files (*.zip *.cbz);; rar_files (*.rar *.cbr);; '
                'tar_files (*.tar *.cbt);; all_files (*)'))

        self.open_comics(filename[0])

    @QtCore.Slot()
    def on_action_save_image_triggered(self):

        if self.model.comic:

            path = self.model.current_directory + \
                self.model.comic.get_current_page_title()
            file_path = QtGui.QFileDialog().getSaveFileName(
                self, self.tr('save_current_page'), path,
                self.tr("images (*.png *.xpm *.jpeg *.jpg *.gif)"))

            if file_path:
                self.model.save_current_page_image(file_path[0])

    @QtCore.Slot()
    def on_action_previous_page_triggered(self):
        self.model.previous_page()
        self.update_viewer_content()
        self.update_navegation_actions()

    @QtCore.Slot()
    def on_action_next_page_triggered(self):
        self.model.next_page()
        self.update_viewer_content()
        self.update_navegation_actions()

    @QtCore.Slot()
    def on_action_first_page_triggered(self):
        self.model.first_page()
        self.update_viewer_content()
        self.update_navegation_actions()

    @QtCore.Slot()
    def on_action_last_page_triggered(self):
        self.model.last_page()
        self.update_viewer_content()
        self.update_navegation_actions()

    @QtCore.Slot()
    def on_action_next_comic_triggered(self):
        self.open_comics(self.model.next_comic())
        self.update_navegation_actions()

    @QtCore.Slot()
    def on_action_previous_comic_triggered(self):
        self.open_comics(self.model.previous_comic())
        self.update_navegation_actions()

    @QtCore.Slot()
    def on_action_rotate_left_triggered(self):
        self.model.rotate_left()
        self.update_viewer_content()

    @QtCore.Slot()
    def on_action_rotate_right_triggered(self):
        self.model.rotate_right()
        self.update_viewer_content()

    @QtCore.Slot()
    def on_action_add_bookmark_triggered(self):
        print

    @QtCore.Slot()
    def on_action_remove_bookmark_triggered(self):
        print

    @QtCore.Slot()
    def on_action_bookmark_manager_triggered(self):
        print

    @QtCore.Slot()
    def on_action_preference_dialog_triggered(self):
        print

    @QtCore.Slot()
    def on_action_original_fit_triggered(self):
        self.model.original_fit()
        self.update_viewer_content()

    @QtCore.Slot()
    def on_action_vertical_fit_triggered(self):
        self.model.vertical_fit()
        self.update_viewer_content()

    @QtCore.Slot()
    def on_action_horizontal_fit_triggered(self):
        self.model.horizontal_fit()
        self.update_viewer_content()

    @QtCore.Slot()
    def on_action_best_fit_triggered(self):
        self.model.best_fit()
        self.update_viewer_content()

    @QtCore.Slot()
    def on_action_fullscreen_triggered(self):

        if self.isFullScreen():
            self.ui.menubar.show()
            self.ui.toolbar.show()
            self.ui.statusbar.show()
            self.showMaximized()

            for sc in self.global_shortcuts:
                sc.setEnabled(False)
        else:
            self.ui.menubar.hide()
            self.ui.toolbar.hide()
            self.ui.statusbar.hide()
            self.showFullScreen()
            for sc in self.global_shortcuts:
                sc.setEnabled(True)

    @QtCore.Slot()
    def on_action_about_triggered(self):

        text = '<p><justify><a ' \
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

        # import about_dialog
        # ab_dlg = about_dialog.AboutDialog()
        # ab_dlg.show()
        # ab_dlg.exec_()

    @QtCore.Slot()
    def on_action_about_qt_triggered(self):
        QtGui.QMessageBox().aboutQt(self, self.tr(u'About Qt'))

    @QtCore.Slot()
    def on_action_exit_triggered(self):
        super(MainWindowView, self).close()
        # self.controller.exit()

    def open_comics(self, filename):

        if filename:

            try:
                self.model.load(filename)
                self.update_viewer_content()
                self.setWindowTitle(self.model.get_comic_title())
                self.enable_actions()
                self.update_status_bar()

                #
                # if res:
                #     self.recent_file_manager.append_left(
                #         self.model.comic.name.decode('utf8'),
                # file_name.decode('utf8'))
                #
                # is_last_comic = self.model.is_last_comic()
                # is_first_comic = self.model.is_firts_comic()

                # self._update_navegation_actions()

                self.ui.action_previous_comic.setEnabled(
                    not self.model.is_firts_comic())

                self.ui.action_next_comic.setEnabled(
                    not self.model.is_last_comic())

            except LoadComicsException as excp:
                QtGui.QMessageBox().warning(self,
                                            self.tr('LoadComicsExceptionError'),
                                            self.tr(excp.message),
                                            QtGui.QMessageBox.Close)
            except InvalidTypeFileException as excp:
                QtGui.QMessageBox().warning(self,
                                            self.tr('InvalidTypeFileException'),
                                            self.tr(excp.message),
                                            QtGui.QMessageBox.Close)

    # def show_progress_bar_dialog(self):
    #     from qprogress_bar_dialog import QProgressBarDialog
    #     dlg = QProgressBarDialog(self.model, self)
    #     dlg.show()

        # dlg.exec_()
        # th = QProgressBarDialogThread(self.model)
        # th.start()

    def update_navegation_actions(self):

        is_first_page = self.model.is_first_page()
        is_last_page = self.model.is_last_page()

        self.ui.action_previous_page.setEnabled(not is_first_page)
        self.ui.action_first_page.setEnabled(not is_first_page)

        self.ui.action_next_page.setEnabled(not is_last_page)
        self.ui.action_last_page.setEnabled(not is_last_page)

    def _create_connections(self):

        # self.ui.action_open.triggered.connect(ctrl.open)
        # self.ui.action_save_image.triggered.connect(ctrl.save_image)
        # self.ui.action_open_online.triggered.connect(ctrl.open_online)
        #
        # self.ui.action_next_page.triggered.connect(ctrl.next_page)
        # self.ui.action_previous_page.triggered.connect(ctrl.previous_page)
        #
        # self.ui.action_first_page.triggered.connect(ctrl.first_page)
        # self.ui.action_last_page.triggered.connect(ctrl.last_page)
        # self.ui.action_go_to_page.triggered.connect(ctrl.go_to_page)
        # self.ui.action_next_comic.triggered.connect(ctrl.next_comic)
        # self.ui.action_previous_comic.triggered.connect(ctrl.previous_comic)
        #
        # self.ui.action_rotate_left.triggered.connect(ctrl.rotate_left)
        # self.ui.action_rotate_right.triggered.connect(ctrl.rotate_right)
        #
        # self.ui.action_add_bookmark.triggered.connect(ctrl.add_bookmark)
        # self.ui.action_remove_bookmark.triggered.connect(ctrl.remove_bookmark)
        # self.ui.action_bookmark_manager.triggered.connect(ctrl.bookmark_manager)
        #
        # self.ui.action_preference_dialog.triggered.connect(
        #     ctrl.preference_dialog)
        #
        self.ui.action_group_view = QtGui.QActionGroup(self)

        self.ui.action_group_view.addAction(self.ui.action_original_fit)
        self.ui.action_group_view.addAction(self.ui.action_vertical_fit)
        self.ui.action_group_view.addAction(self.ui.action_horizontal_fit)
        self.ui.action_group_view.addAction(self.ui.action_best_fit)

        # self.ui.action_original_fit.triggered.connect(ctrl.original_fit)
        # self.ui.action_vertical_fit.triggered.connect(ctrl.vertical_fit)
        # self.ui.action_horizontal_fit.triggered.connect(ctrl.horizontal_fit)
        # self.ui.action_best_fit.triggered.connect(ctrl.best_fit)
        #
        # self.ui.menu_recent_files.aboutToShow.connect(
        #     ctrl.update_recent_files_menu)
        # #
        # # actions =
        #
        # for rf in self.ui.menu_recent_files.actions():
        #     rf.triggered.connect(ctrl.load_recent_file)
        #
        # self.ui.menu_recent_bookmarks.aboutToShow.connect(
        #     ctrl.update_bookmarks_menu)
        #
        # for bk in self.ui.menu_recent_bookmarks.actions():
        #     bk.triggered.connect(ctrl.load_bookmark)

    def _define_global_shortcuts(self):

        sequence = {
            'Ctrl+Shift+Left': self.on_action_previous_comic_triggered,
            'Ctrl+Left': self.on_action_first_page_triggered,
            'Left': self.on_action_previous_page_triggered,
            'Right': self.on_action_next_page_triggered,
            'Ctrl+Right': self.on_action_last_page_triggered,
            'Ctrl+Shift+Right': self.on_action_next_comic_triggered,
            'Ctrl+R': self.on_action_rotate_left_triggered,
            'Ctrl+Shift+R': self.on_action_rotate_right_triggered,
        }

        for key, value in sequence.items():
            s = QtGui.QShortcut(QtGui.QKeySequence(key),
                                self.ui.qscroll_area_viewer, value)
            s.setEnabled(False)
            self.global_shortcuts.append(s)

    def enable_actions(self):

        action_list = self.ui.menu_file.actions()
        action_list += self.ui.menu_view.actions()
        action_list += self.ui.menu_navegation.actions()
        action_list += self.ui.menu_bookmarks.actions()

        for action in action_list:
            action.setEnabled(True)

    def update_status_bar(self):

        if self.model.comic:
            page_number = self.model.comic.get_current_page_number()
            total_pages = self.model.comic.get_number_of_pages()
            page_width = self.model.get_current_page().width()
            page_height = self.model.get_current_page().height()
            page_title = self.model.comic.get_current_page_title()

            if self.ui.statusbar.isVisible():
                self.ui.statusbar.set_comic_page(page_number, total_pages)
                self.ui.statusbar.set_page_resolution(page_width, page_height)
                self.ui.statusbar.set_comic_path(page_title)
    #
    # def switch_to_web_view(self):
    #     if self.web_view is None:
    #         self.web_view = QWebImageWidget()
    #
    #     self.current_view_container = self.web_view
    #     self.setCentralWidget(self.web_view)
    #
    # def switch_to_normal_view(self):
    #     self.setCentralWidget(self.qscroll_area_viewer)
    #     self.current_view_container = self.qscroll_area_viewer
    #

    def _centralize_window(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        x_center = (screen.width() - size.width()) / 2
        y_center = (screen.height() - size.height()) / 2
        self.move(x_center, y_center)
        self.setMinimumSize(
            screen.size() * 0.8)
        self.update()

    def update_viewer_content(self):
        content = self.model.get_current_page()
        if content and isinstance(content, QtGui.QPixmap):
            self.ui.label.setPixmap(content)
            self.ui.qscroll_area_viewer.reset_scroll_position()
            self.update_status_bar()
            self.repaint()

    def update_current_view_container_size(self):
        self.model.scroll_area_size = self.get_current_view_container_size()
        self.update_viewer_content()

    def get_current_view_container_size(self):
        return self.ui.qscroll_area_viewer.size()
    #
    # def change_background_color(self, color):
    #     self.current_view_container.change_background_color(color)
    #
    # @QtCore.pyqtSlot()
    # def on_action_show_toolbar_triggered(self):
    #     if self.action_show_toolbar.isChecked():
    #         self.toolbar.show()
    #     else:
    #         self.toolbar.hide()
    #
    # @QtCore.pyqtSlot()
    # def on_action_show_statusbar_triggered(self):
    #     if self.action_show_statusbar.isChecked():
    #         self.statusbar.show()
    #     else:
    #         self.statusbar.hide()
    #

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

    def show(self):
        """
        :doc: Added to set the correct scrool_area_view size in model
        """
        super(MainWindowView, self).show()
        self.update_current_view_container_size()
