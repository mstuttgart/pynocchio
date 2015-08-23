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

from PyQt4 import QtGui, QtCore

import main_window_view
import main_window_model
import settings_manager
from recent_files_manager import RecentFileManager
from preference import Preference
from utility import Utility
from pynocchio_exception import LoadComicsException
from pynocchio_exception import InvalidTypeFileException


class MainWindowController(object):

    def __init__(self):
        self.view = main_window_view.MainWindowView(self)
        self.model = main_window_model.MainWindowModel(self)

        self.recent_file_manager = RecentFileManager(
            len(self.view.menu_recent_files.actions()))

        self.preferences = Preference()
        settings_manager.SettingsManager.load_settings(self.view, self)

    @QtCore.pyqtSlot()
    def open(self):

        file_path = QtGui.QFileDialog().getOpenFileName(
            self.view, self.view.tr('Open comic file'),
            self.model.current_directory,
            self.view.tr(
                'All supported files (*.zip *.cbz *.rar *.cbr *.tar *.cbt);; '
                'Zip Files (*.zip *.cbz);; Rar Files (*.rar *.cbr);; '
                'Tar Files (*.tar *.cbt);; All files (*)'))

        if file_path:
            self.load(file_path)

    def load(self, file_name, initial_page=0):

        file_name = Utility.convert_qstring_to_str(file_name)

        try:
            res = self.model.open(file_name, initial_page)
            self.set_view_content(self.model.get_current_page())
            self.view.setWindowTitle(self.model.comic.name.decode('utf8') +
                                     ' - Pynocchio Comic Reader')
            self.view.enable_actions()
            self.update_statusbar()

            self.model.current_directory = Utility.get_dir_name(file_name)

            if res:
                self.recent_file_manager.append_left(
                    self.model.comic.name.decode('utf8'), file_name.decode('utf8'))

            is_last_comic = self.model.is_last_comic()
            is_first_comic = self.model.is_firts_comic()

            self._update_navegation_actions()

            self.view.action_previous_comic.setEnabled(not is_first_comic)
            self.view.action_next_comic.setEnabled(not is_last_comic)

            return res

        except LoadComicsException as excp:
            message = excp.message
        except InvalidTypeFileException as excp:
            message = excp.message

        QtGui.QMessageBox().warning(self.view,
                                    self.view.tr('Error!'),
                                    self.view.tr(message),
                                    QtGui.QMessageBox.Close)
        return False

    def save_image(self):

        if self.model.comic:

            path = self.model.current_directory + \
                self.model.comic.get_current_page_title()

            file_path = QtGui.QFileDialog().getSaveFileName(
                self.view, self.view.tr('Save current page'), path,
                self.view.tr("Images (*.png *.xpm *.jpeg *.jpg *.gif)"))

            self.model.save_content(file_path)

    def open_online(self):
        from online_comic_chooser_dialog import OnlineComicChooserDialog

        online_comic_chooser = OnlineComicChooserDialog(self.view)
        online_comic_chooser.show()
        online_comic_chooser.exec_()

    def next_page(self):
        self.model.next_page()
        self._update_navegation_actions()

    def previous_page(self):
        self.model.previous_page()
        self._update_navegation_actions()

    def first_page(self):
        self.model.first_page()
        self._update_navegation_actions()

    def last_page(self):
        self.model.last_page()
        self._update_navegation_actions()

    def go_to_page(self):
        import go_to_page_dialog
        go_to_dlg = go_to_page_dialog.GoToDialog(self, self.view)
        go_to_dlg.show()
        go_to_dlg.exec_()
        self._update_navegation_actions()

    def next_comic(self):
        ret = self.model.next_comic()
        if ret:
            self.load(QtCore.QString(ret))
            self._update_navegation_actions()

    def previous_comic(self):
        ret = self.model.previous_comic()
        if ret:
            self.load(QtCore.QString(ret))
            self._update_navegation_actions()

    def _update_navegation_actions(self):

        is_first_page = self.model.is_first_page()
        is_last_page = self.model.is_last_page()

        self.view.action_previous_page.setEnabled(not is_first_page)
        self.view.action_first_page.setEnabled(not is_first_page)

        self.view.action_next_page.setEnabled(not is_last_page)
        self.view.action_last_page.setEnabled(not is_last_page)

    def rotate_left(self):
        self.model.rotate_left()

    def rotate_right(self):
        self.model.rotate_right()

    def original_fit(self):
        self.model.original_fit()

    def vertical_fit(self):
        self.model.vertical_fit()

    def horizontal_fit(self):
        self.model.horizontal_fit()

    def best_fit(self):
        self.model.best_fit()

    def update_recent_files_menu(self):
        rf_actions = self.view.menu_recent_files.actions()

        for rf in rf_actions:
            rf.setVisible(False)

        for i, r_file in enumerate(self.recent_file_manager.recent_files_deque):
            rf_actions[i].setText(r_file.file_name)
            rf_actions[i].setStatusTip(r_file.path)
            rf_actions[i].setVisible(True)

    def load_recent_file(self):
        action = self.view.sender()

        if action:
            self.load(QtCore.QString(action.statusTip()))

    def update_bookmarks_menu(self):

        bk_actions = self.view.menu_recent_bookmarks.actions()
        bookmark_list = self.model.get_bookmark_list(len(bk_actions))

        for bk in bk_actions:
            bk.setVisible(False)

        for i, bk in enumerate(bookmark_list):
            bk_text = '%s [%d]' % (bk.comic_name, bk.comic_page)
            bk_actions[i].setText(bk_text)
            bk_actions[i].setStatusTip(bk.comic_path)
            bk_actions[i].setVisible(True)

    def load_bookmark(self):
        action = self.view.sender()
        if action:
            bk = self.model.get_bookmark_from_path(action.statusTip())
            if bk:
                self.load(QtCore.QString(bk.comic_path), bk.comic_page - 1)

    def add_bookmark(self):
        self.model.add_bookmark()

    def remove_bookmark(self):
        self.model.remove_bookmark()

    def bookmark_manager(self):
        import bookmark_manager_dialog
        bookmark_dialog = bookmark_manager_dialog.BookmarkManagerDialog(
            self.view, self)
        bookmark_dialog.show()
        bookmark_dialog.exec_()

    def preference_dialog(self):
        self.preferences.show_preference_dialog(self.view)
        self.view.change_background_color(self.preferences.background_color)

    def exit(self):
        print '[INFO] Exiting Pynocchio Comic Reader'
        settings_manager.SettingsManager.save_settings(self.view, self)

    def show(self):
        self.view.show()

    def set_view_content(self, content):
        self.view.set_viewer_content(content)
        self.update_statusbar()

    def get_current_view_container_size(self):
        return self.view.get_current_view_container_size()

    def update_statusbar(self):

        if self.model.comic:
            n_page = self.model.comic.get_current_page_number()
            pages_size = self.model.comic.get_number_of_pages()
            page_width = self.model.get_current_page().width()
            page_height = self.model.get_current_page().height()
            page_title = self.model.comic.get_current_page_title()

            self.view.update_status_bar(n_page, pages_size, page_title,
                                        page_width, page_height)
