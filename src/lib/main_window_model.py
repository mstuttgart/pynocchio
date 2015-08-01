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
# with this program.  If not, see <http://www.gnu.org/licenses/
#
from PyQt4 import QtCore

from utility import Utility
from bookmark_database_manager import BookmarkManager
from compact_file_loader_factory import LoaderFactory
from comic import Comic
from page import *
from path_file_filter import PathFileFilter
from pynocchio_exception import NoDataFindException


class MainWindowModel(object):

    _ORIGINAL_FIT = 'action_original_fit'
    _VERTICAL_FIT = 'action_vertical_fit'
    _HORIZONTAL_FIT = 'action_horizontal_fit'
    _BEST_FIT = 'action_best_fit'

    def __init__(self, controller):
        self.controller = controller
        self.comic = None
        self.fit_type = MainWindowModel._ORIGINAL_FIT
        self.rotateAngle = 0
        self.current_directory = '.'
        ext_list = ["*.cbr", "*.cbz", "*.rar", "*.zip", "*.tar", "*.cbt"]
        self.path_file_filter = PathFileFilter(ext_list)

    def open(self, file_name, initial_page=0):

        image_extensions = ['.bmp', '.jpg', '.jpeg', '.gif', '.png', '.pbm',
                            '.pgm', '.ppm', '.tiff', '.xbm', '.xpm']

        ld = LoaderFactory.create_loader(
            Utility.get_file_extension(file_name), image_extensions)

        ld.progress.connect(self.controller.view.statusbar.set_progressbar_value)
        ld.done.connect(self.controller.view.statusbar.close_progress_bar)

        try:
            ld.load(file_name)
            ret = True
        except NoDataFindException as excp:
            # Caso nao exista nenhuma imagem, carregamos a imagem indicando
            # erro
            print excp.message
            q_file = QtCore.QFile(":/icons/notCover.png")
            q_file.open(QtCore.QIODevice.ReadOnly)
            ld.data.append({
                'data': q_file.readAll(),
                'name': 'exit_red_1.png'
            })

            ret = False

        self.comic = Comic(Utility.get_base_name(file_name),
                           Utility.get_dir_name(file_name), initial_page)

        for index, p in enumerate(ld.data):
            self.comic.add_page(Page(p['data'], p['name'], index + 1))

        self.current_directory = Utility.get_dir_name(file_name)
        self.path_file_filter.parse(file_name)

        return ret

    def save_content(self, file_name):
        self.get_current_page().save(file_name)

    def next_page(self):
        if self.comic:
            self.comic.go_next_page()
            self.controller.set_view_content(self.get_current_page())

    def previous_page(self):
        if self.comic:
            self.comic.go_previous_page()
            self.controller.set_view_content(self.get_current_page())

    def first_page(self):
        if self.comic:
            self.comic.go_first_page()
            self.controller.set_view_content(self.get_current_page())

    def last_page(self):
        if self.comic:
            self.comic.go_last_page()
            self.controller.set_view_content(self.get_current_page())

    def next_comic(self):
        return self.path_file_filter.next_path.decode('utf-8')

    def previous_comic(self):
        return self.path_file_filter.previous_path.decode('utf-8')

    def rotate_left(self):
        self.rotateAngle = (self.rotateAngle - 90) % 360
        self.controller.set_view_content(self.get_current_page())

    def rotate_right(self):
        self.rotateAngle = (self.rotateAngle + 90) % 360
        self.controller.set_view_content(self.get_current_page())

    def get_comic_name(self):
        return self.comic.name if self.comic else ''

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

    def is_firts_comic(self):
        return self.path_file_filter.is_first_file()

    def is_last_comic(self):
        return self.path_file_filter.is_last_file()

    def _rotate_page(self, pix_map):
        if self.rotateAngle != 0:
            trans = QtGui.QTransform().rotate(self.rotateAngle)
            pix_map = QtGui.QPixmap(pix_map.transformed(trans))
        return pix_map

    def _resize_page(self, pix_map):

        if self.fit_type == MainWindowModel._VERTICAL_FIT:
            pix_map = pix_map.scaledToHeight(
                self.controller.get_current_view_container_size().height(),
                QtCore.Qt.SmoothTransformation)

        elif self.fit_type == MainWindowModel._HORIZONTAL_FIT:
            pix_map = pix_map.scaledToWidth(
                self.controller.get_current_view_container_size().width(),
                QtCore.Qt.SmoothTransformation)

        elif self.fit_type == MainWindowModel._BEST_FIT:
            pix_map = pix_map.scaledToWidth(
                self.controller.get_current_view_container_size().width() * 0.8,
                QtCore.Qt.SmoothTransformation)

        return pix_map

    def original_fit(self):
        self.fit_type = MainWindowModel._ORIGINAL_FIT
        self.controller.set_view_content(self.get_current_page())

    def vertical_fit(self):
        self.fit_type = MainWindowModel._VERTICAL_FIT
        self.controller.set_view_content(self.get_current_page())

    def horizontal_fit(self):
        self.fit_type = MainWindowModel._HORIZONTAL_FIT
        self.controller.set_view_content(self.get_current_page())

    def best_fit(self):
        self.fit_type = MainWindowModel._BEST_FIT
        self.controller.set_view_content(self.get_current_page())

    @staticmethod
    def get_bookmark_list(n):
        BookmarkManager.connect()
        bookmark_list = BookmarkManager.get_bookmarks(n)
        BookmarkManager.close()
        return bookmark_list

    @staticmethod
    def get_bookmark_from_path(path):
        BookmarkManager.connect()
        bk = BookmarkManager.get_bookmark_by_path(path)
        BookmarkManager.close()
        return bk

    def add_bookmark(self):
        if self.comic:
            BookmarkManager.connect()
            BookmarkManager.add_bookmark(self.comic.name,
                                         self.comic.get_path(),
                                         self.comic.get_current_page_number(),
                                         self.comic.get_current_page().data)
            BookmarkManager.close()

    def remove_bookmark(self):
        if self.comic:
            BookmarkManager.connect()
            BookmarkManager.remove_bookmark(self.comic.get_path())
            BookmarkManager.close()
