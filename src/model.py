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
from PyQt4 import QtCore, QtGui

from comic import Comic
from page import Page
from bookmark_database_manager import BookmarkManager


class Model(object):
    NUM_BOOKMARK = 5

    def __init__(self, main_window):

        super(Model, self).__init__()

        self.main_window = main_window
        self.comic = None
        self.original_pixmap = QtGui.QPixmap()
        self.adjustType = 'action_original_fit'
        self.screenSize = QtCore.QSize(0, 0)
        self.rotateAngle = 0
        self.current_directory = ''
        self.next_comic_path = ''
        self.previous_comic_path = ''
        self.zoom_factor = 1.0

    def load_comic(self, file_name, initial_page=0):

        from loader_factory import LoaderFactory
        from utility import Utility

        try:
            image_extensions = ['.bmp', '.jpg', '.jpeg', '.gif', '.png', '.pbm',
                                '.pgm', '.ppm', '.tiff', '.xbm', '.xpm']

            ld = LoaderFactory.create_loader(Utility.get_file_extension(
                file_name), image_extensions)

        except IOError:
            print self.main_window.tr('File not exist!')
            return False

        ld.progress.connect(self.main_window.statusbar.set_progressbar_value)
        ld.done.connect(self.main_window.statusbar.close_progress_bar)

        if ld.load(file_name):
            self.comic = Comic(Utility.get_base_name(file_name),
                               Utility.get_dir_name(file_name), initial_page)
            if not ld.data:
                # Caso nao exista nenhuma imagem, carregamos a imagem indicando
                # erro
                q_file = QtCore.QFile(":/icons/icons/exit_red_1.png")
                q_file.open(QtCore.QIODevice.ReadOnly)
                ld.data.append(
                    {'data': q_file.readAll(), 'name': 'exit_red_1.png'})
                self.current_directory = Utility.get_dir_name(file_name)

            for p in ld.data:
                page_data = p['data']
                page_name = p['name']
                page_index = ld.data.index(p) + 1
                self.comic.add_page(Page(page_data, page_name, page_index))

            return True

        import pynocchio_exception
        raise pynocchio_exception.OpenComicFileException(comic_name=file_name)

        return False

    def next_page(self):
        if self.comic:
            self.comic.go_next_page()
        return self.get_current_page()

    def previous_page(self):
        if self.comic:
            self.comic.go_previous_page()
        return self.get_current_page()

    def first_page(self):
        if self.comic:
            self.comic.go_first_page()
        return self.get_current_page()

    def last_page(self):
        if self.comic:
            self.comic.go_last_page()
        return self.get_current_page()

    def next_comic(self):
        return self.next_comic_path

    def previous_comic(self):
        return self.previous_comic_path

    def verify_comics_in_path(self):

        from PyQt4.QtCore import QDir

        d = QDir(self.comic.directory)
        d.setFilter(QDir.Files | QDir.NoDotAndDotDot)
        d.setNameFilters(
            ["*.cbr", "*.cbz", "*.rar", "*.zip", "*.tar", "*.cbt"])
        d.setSorting(QDir.Name | QDir.IgnoreCase | QDir.LocaleAware)

        str_list = d.entryList()
        str_list.sort()
        index = str_list.indexOf(self.comic.name)

        if index == -1:
            return

        if index > 0:
            self.previous_comic_path = self.comic.directory + "/" + str_list[
                index - 1]
            self.main_window.action_previous_comic.setEnabled(True)
        else:
            self.previous_comic_path = ''
            self.main_window.action_previous_comic.setEnabled(False)

        if (index + 1) < len(str_list):
            self.next_comic_path = self.comic.directory + "/" + str_list[
                index + 1]
            self.main_window.action_next_comic.setEnabled(True)
        else:
            self.next_comic_path = ''
            self.main_window.action_next_comic.setEnabled(False)

    def rotate_left(self):
        self.rotateAngle = (self.rotateAngle - 90) % 360
        return self.get_current_page()

    def rotate_right(self):
        self.rotateAngle = (self.rotateAngle + 90) % 360
        return self.get_current_page()

    def get_comic_name(self):
        if self.comic:
            return self.comic.name
        return None

    def get_current_page(self):
        return self._load_pixmap_from_data()

    def get_current_page_title(self):
        if self.comic:
            return self.comic.get_current_page_title()
        return None

    def set_current_page_index(self, idx):
        if self.comic:
            self.comic.set_current_page_index(idx)

    def get_current_page_index(self):
        if self.comic:
            return self.comic.current_page_index
        return -1

    def is_last_page(self):
        if self.comic and self.comic.current_page_index + 1 == \
                self.comic.get_number_of_pages():
            return True
        return False

    def is_first_page(self):
        if self.comic and self.comic.current_page_index == 0:
            return True
        return False

    def _load_pixmap_from_data(self):
        if self.comic:
            pg = self.comic.get_current_page()
            if pg:
                self.original_pixmap.loadFromData(pg)

        return self.update_content()

    def update_content(self):
        pix_map = self.original_pixmap
        pix_map = self._rotate_page(pix_map)
        pix_map = self._resize_page(pix_map)
        return pix_map

    def _rotate_page(self, pix_map):
        if self.rotateAngle != 0:
            trans = QtGui.QTransform().rotate(self.rotateAngle)
            pix_map = QtGui.QPixmap(pix_map.transformed(trans))

        return pix_map

    def _resize_page(self, pix_map):

        if self.comic:

            if self.adjustType == 'action_vertical_adjust':
                pix_map = pix_map.scaledToHeight(
                    self.screenSize.height(),
                    QtCore.Qt.SmoothTransformation)

            elif self.adjustType == 'action_horizontal_adjust':
                pix_map = pix_map.scaledToWidth(
                    self.screenSize.width(), QtCore.Qt.SmoothTransformation)

            elif self.adjustType == 'action_best_fit':
                pix_map = pix_map.scaledToWidth(
                    self.screenSize.width() * 0.8,
                    QtCore.Qt.SmoothTransformation)

            pix_map = pix_map.scaled(pix_map.size() * self.zoom_factor,
                                     QtCore.Qt.KeepAspectRatio,
                                     QtCore.Qt.SmoothTransformation)

            return pix_map

        return None

    def set_size(self, new_size):
        self.screenSize = new_size

    def set_adjust_type(self, adjust_type):
        self.adjustType = adjust_type

    # @QtCore.pyqtSlot(int)
    # def set_zoom_factor(self, value):
    #     print 2 * value/100.0
    #     self.zoom_factor = 2 * value/100.0
    #     # self.main_window.repaint()

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
                                         self.comic.get_current_page())
            BookmarkManager.close()

    def remove_bookmark(self):
        if self.comic:
            BookmarkManager.connect()
            BookmarkManager.remove_bookmark(self.comic.get_path())
            BookmarkManager.close()
