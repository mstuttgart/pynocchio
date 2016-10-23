# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/
#

from PyQt5 import QtCore, QtGui, QtWidgets
from .comic import Comic
from .compact_file_loader_factory import LoaderFactory
from .path_file_filter import PathFileFilter
from .pynocchio_exception import NoDataFindException
from .settings_manager import SettingsManager
from .utility import Utility

from .bookmark_database_manager import BookmarkManager
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MainWindowModel(QtCore.QObject):
    _ORIGINAL_FIT = 'action_original_fit'
    _VERTICAL_FIT = 'action_vertical_fit'
    _HORIZONTAL_FIT = 'action_horizontal_fit'
    _BEST_FIT = 'action_best_fit'

    load_progress = QtCore.pyqtSignal(int)
    load_done = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindowModel, self).__init__()
        self.comic = None
        self.settings_manager = SettingsManager()
        self.rotate_angle = 0
        self.scroll_area_size = None
        self.fit_type = self.load_view_adjust(MainWindowModel._ORIGINAL_FIT)
        self.current_directory = self.load_current_directory()

        ext_list = ["*.cbr", "*.cbz", "*.rar", "*.zip", "*.tar", "*.cbt"]
        self.path_file_filter = PathFileFilter(ext_list)

    def save_recent_files(self, recent_files_list):
        self.settings_manager.save_recent_files(recent_files_list)

    def load_recent_files(self):
        return self.settings_manager.load_recent_files()

    def save_view_adjust(self, object_name):
        self.settings_manager.save_view_adjust(object_name)

    def load_view_adjust(self, default_object_name):
        return self.settings_manager.load_view_adjust(default_object_name)

    def save_current_directory(self, current_directory):
        self.settings_manager.save_current_directory(current_directory)

    def load_current_directory(self):
        return self.settings_manager.load_current_directory()

    def load(self, filename, initial_page=0):

        image_extensions = ['.bmp', '.jpg', '.jpeg', '.gif', '.png', '.pbm',
                            '.pgm', '.ppm', '.tiff', '.xbm', '.xpm', '.webp']

        loader = LoaderFactory.create_loader(
            Utility.get_file_extension(filename), filename, set(image_extensions))

        loader.progress.connect(self.load_progressbar_value)

        try:
            loader.load(filename)
        except NoDataFindException as exc:
            from .page import Page
            logger.exception('Error in load comic')
            q_file = QtCore.QFile(":/icons/notCover.png")
            q_file.open(QtCore.QIODevice.ReadOnly)
            loader.data.append(Page(q_file.readAll(), 'exit_red_1.png', 0))

        self.comic = Comic(Utility.get_base_name(filename),
                           Utility.get_dir_name(filename), initial_page)

        self.comic.pages = loader.data
        self.current_directory = Utility.get_dir_name(filename)

        if Utility.is_file(filename):
            self.path_file_filter.parse(filename)

    def save_current_page_image(self, file_name):
        self.get_current_page().save(file_name)

    def next_page(self):
        if self.comic:
            self.comic.go_next_page()

    def previous_page(self):
        if self.comic:
            self.comic.go_previous_page()

    def first_page(self):
        if self.comic:
            self.comic.go_first_page()

    def last_page(self):
        if self.comic:
            self.comic.go_last_page()

    def next_comic(self):
        return self.path_file_filter.next_path

    def previous_comic(self):
        return self.path_file_filter.previous_path

    def rotate_left(self):
        self.rotate_angle = (self.rotate_angle - 90) % 360

    def rotate_right(self):
        self.rotate_angle = (self.rotate_angle + 90) % 360

    def get_comic_name(self):
        return self.comic.name if self.comic else ''

    def get_comic_path(self):
        return self.comic.get_path() if self.comic else ''

    def get_comic_title(self):
        return self.comic.name + ' - Pynocchio Comic Reader'

    def get_current_page(self):
        if self.comic:
            pix_map = self.comic.get_current_page().pixmap
            pix_map = self._rotate_page(pix_map)
            pix_map = self._resize_page(pix_map)
            return pix_map

        return None

    def get_current_page_title(self):
        return self.comic.get_current_page_title() if self.comic else ''

    def set_current_page_index(self, idx):
        if self.comic:
            self.comic.set_current_page_index(idx)

    def get_current_page_index(self):
        return self.comic.current_page_index if self.comic else -1

    def is_first_page(self):
        if self.comic and self.comic.current_page_index == 0:
            return True
        return False

    def is_last_page(self):
        if self.comic and self.comic.current_page_index + 1 == \
                self.comic.get_number_of_pages():
            return True
        return False

    def is_first_comic(self):
        if self.path_file_filter.current_path:
            return self.path_file_filter.is_first_file()
        else:
            return True

    def is_last_comic(self):
        if self.path_file_filter.current_path:
            return self.path_file_filter.is_last_file()
        else:
            return True

    def _rotate_page(self, pix_map):
        if self.rotate_angle != 0:
            trans = QtGui.QTransform().rotate(self.rotate_angle)
            pix_map = QtGui.QPixmap(pix_map.transformed(trans))
        return pix_map

    def _resize_page(self, pix_map):

        if self.fit_type == MainWindowModel._VERTICAL_FIT:
            pix_map = pix_map.scaledToHeight(
                self.scroll_area_size.height(),
                QtCore.Qt.SmoothTransformation)

        elif self.fit_type == MainWindowModel._HORIZONTAL_FIT:
            pix_map = pix_map.scaledToWidth(
                self.scroll_area_size.width(),
                QtCore.Qt.SmoothTransformation)

        elif self.fit_type == MainWindowModel._BEST_FIT:
            pix_map = pix_map.scaledToWidth(
                self.scroll_area_size.width() * 0.8,
                QtCore.Qt.SmoothTransformation)

        return pix_map

    def original_fit(self):
        self.fit_type = MainWindowModel._ORIGINAL_FIT

    def vertical_fit(self):
        self.fit_type = MainWindowModel._VERTICAL_FIT

    def horizontal_fit(self):
        self.fit_type = MainWindowModel._HORIZONTAL_FIT

    def best_fit(self):
        self.fit_type = MainWindowModel._BEST_FIT

    @QtCore.pyqtSlot(int)
    def load_progressbar_value(self, percent):
        self.load_progress.emit(percent)

    @QtCore.pyqtSlot()
    def load_progressbar_done(self):
        self.load_done.emit()

    def save_settings(self):
        self.save_view_adjust(self.fit_type)
        self.save_current_directory(self.current_directory)

    @staticmethod
    def get_bookmark_list(qty):
        BookmarkManager.connect()
        bookmark_list = BookmarkManager.get_bookmarks(qty)
        BookmarkManager.close()
        return bookmark_list

    def is_bookmark(self):
        BookmarkManager.connect()
        is_bookmark = BookmarkManager.is_bookmark(self.comic.get_path())
        BookmarkManager.close()
        return is_bookmark

    @staticmethod
    def get_bookmark_from_path(path):
        BookmarkManager.connect()
        bookmark = BookmarkManager.get_bookmark_by_path(path)
        BookmarkManager.close()
        return bookmark

    def add_bookmark(self):
        if self.comic:
            BookmarkManager.connect()
            BookmarkManager.add_bookmark(self.comic.name,
                                         self.comic.get_path(),
                                         self.comic.get_current_page_number(),
                                         self.comic.get_current_page().data)
            BookmarkManager.close()

    def remove_bookmark(self, path):
            BookmarkManager.connect()
            BookmarkManager.remove_bookmark(path)
            BookmarkManager.close()
