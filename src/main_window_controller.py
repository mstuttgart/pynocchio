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
import recent_files_manager
import recent_file


class MainWindowController():
    def __init__(self):
        self.view = main_window_view.MainWindowView(self)
        self.model = main_window_model.MainWindowModel(self)

        settings_manager.SettingsManager.load(self.view, self)

        self.recent_file_manager = recent_files_manager.RecentFileManager(
            len(self.view.menu_recent_files.actions()))

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

        if self.model.open(file_name, initial_page):
            self.set_view_content(self.model.get_current_page())
            self.view.setWindowTitle(self.model.comic.name +
                                     ' - Pynocchio Comic Reader')
            self.view.enable_actions()
            self.update_statusbar()

            from utility import Utility
            self.model.current_directory = Utility.get_dir_name(
                Utility.convert_qstring_to_str(file_name))

            self.recent_file_manager.append_left(
                recent_file.RecenteFiles(self.model.comic.name,
                                                  Utility.convert_qstring_to_str(file_name)))
        else:
            print '[ERROR] error load comics'

    def save_image(self):
        print

    def open_online(self):
        from online_comic_chooser import OnlineComicChooser

        online_comic_chooser = OnlineComicChooser(self.view)
        online_comic_chooser.show()
        online_comic_chooser.exec_()

    def next_page(self):
        self.model.next_page()

    def previous_page(self):
        self.model.previous_page()

    def first_page(self):
        self.model.first_page()

    def last_page(self):
        self.model.last_page()

    def go_to_page(self):
        print

    def next_comic(self):
        print

    def previous_comic(self):
        print

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

        for i in range(len(self.recent_file_manager.recent_files_deque)):
            rf_actions[i].setText(self.recent_file_manager.get(i).comic_name)
            rf_actions[i].setStatusTip(
                self.recent_file_manager.get(i).comic_path)
            rf_actions[i].setVisible(True)

    def load_recent_file(self):
        action = self.view.sender()
        if action:

            for rf in self.recent_file_manager.recent_files_deque:
                if rf.comic_path == action.statusTip():
                    self.recent_file_manager.remove(rf)
                    # prevent deque to change lenght erro
                    break

            self.load(QtCore.QString(action.statusTip()))

    def update_bookmarks_menu(self):

        bk_actions = self.view.menu_recent_bookmarks.actions()
        bookmark_list = self.model.get_bookmark_list(len(bk_actions))

        for bk in bk_actions:
            bk.setVisible(False)

        for i in range(len(bookmark_list)):
            bk_text = '%s [%d]' % (bookmark_list[i].comic_name,
                                   bookmark_list[i].comic_page)
            bk_actions[i].setText(bk_text)
            bk_actions[i].setStatusTip(bookmark_list[i].comic_path)
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
        print

    def exit(self):
        print '[INFO] Exiting Pynocchio Comic Reader'
        settings_manager.SettingsManager.save(self.view, self)

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


