# -*- coding:utf-8 -*-
# Copyright (C) 2015  Michell Stuttgart

# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3.0 of the License, or (at
# your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
from PyQt4 import QtGui
from PyQt4 import QtCore

import comic
import bookmarks


class Model(QtCore.QObject):
    NUM_BOOKMARK = 5

    def __init__(self, parent=None):

        super(Model, self).__init__(parent)

        self.comic = None
        self.original_pixmap = QtGui.QPixmap()
        self.adjustType = 'action_original_fit'
        self.screenSize = QtCore.QSize(0, 0)
        self.rotateAngle = 0
        self.current_directory = ''
        self.next_comic_path = ''
        self.previous_comic_path = ''
        self.current_language = ''
        self.background_color = QtGui.QColor(255, 255, 200)

    def load_comic(self, file_name, initial_page=0):

        if file_name == '':
            return

        try:
            import rar_loader
            import tar_loader
            import zip_loader

            if zip_loader.ZipLoader.is_zip_file(file_name):
                return self._load_content(zip_loader.ZipLoader(self), file_name,
                                          initial_page)

            elif rar_loader.RarLoader.is_rar_file(file_name):
                return self._load_content(rar_loader.RarLoader(self), file_name,
                                          initial_page)

            elif tar_loader.TarLoader.is_tar_file(file_name):
                return self._load_content(tar_loader.TarLoader(self), file_name,
                                          initial_page)

        except IOError, err:
            print '%20s  %s' % (file_name, err)

        return False

    # def load_folder(self, folder_name, initial_page=0):
    # import folder_loader
    #
    #     if folder_loader.FolderLoader.is_folder(folder_name):
    #         return self._load_content(folder_loader.FolderLoader(), folder_name, initial_page)
    #     print 'Not is folder'
    #     return False

    def _load_content(self, loader, file_name, initial_page=0):
        pages, path, name = loader.load_file(file_name)

        res = True
        self.comic = comic.Comic(name, path, initial_page)

        if not pages:
            import page

            q_file = QtCore.QFile(":/icons/icons/exit_red_1.png")
            q_file.open(QtCore.QIODevice.ReadOnly)
            pages.append(page.Page(q_file.readAll(), 'exit_red_1.png', 1))
            res = True
            self.current_directory = path

        for p in pages:
            self.comic.add_page(p)

        return res

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

    def verify_comics_in_path(self, action_next_comic, action_previous_comic):

        from PyQt4.QtCore import QDir

        d = QDir(self.comic.directory)
        d.setFilter(QDir.Files | QDir.NoDotAndDotDot)
        # d.setNameFilters(["*.cbr", "*.cbz", "*.rar", "*.zip", "*.tar", "*.7z", "*.cb7", "*.arj", "*.cbt"])
        d.setNameFilters(["*.cbr", "*.cbz", "*.rar", "*.zip", "*.tar", "*.cbt"])
        d.setSorting(QDir.Name | QDir.IgnoreCase | QDir.LocaleAware)

        str_list = d.entryList()
        str_list.sort()
        index = str_list.indexOf(self.comic.name)

        if index == -1:
            return

        if index > 0:
            self.previous_comic_path = self.comic.directory + "/" + str_list[
                index - 1]
            action_previous_comic.setEnabled(True)
        else:
            self.previous_comic_path = ''
            action_previous_comic.setEnabled(False)

        if (index + 1) < len(str_list):
            self.next_comic_path = self.comic.directory + "/" + str_list[
                index + 1]
            action_next_comic.setEnabled(True)
        else:
            self.next_comic_path = ''
            action_next_comic.setEnabled(False)

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
        if self.comic and self.comic.current_page_index + 1 == self.comic.get_number_of_pages():
            return True
        return False

    def is_first_page(self):
        if self.comic and self.comic.current_page_index == 0:
            return True
        return False

    def _load_pixmap_from_data(self):
        page = None
        if self.comic:
            page = self.comic.get_current_page()
        if page:
            self.original_pixmap.loadFromData(page)

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
                    self.screenSize.height(), QtCore.Qt.SmoothTransformation)

            elif self.adjustType == 'action_horizontal_adjust':
                pix_map = pix_map.scaledToWidth(
                    self.screenSize.width(), QtCore.Qt.SmoothTransformation)

            elif self.adjustType == 'action_best_fit':
                pix_map = pix_map.scaledToWidth(
                    self.screenSize.width() * 0.8,
                    QtCore.Qt.SmoothTransformation)

            return pix_map

        return None

    def set_size(self, new_size):
        self.screenSize = new_size

    def set_adjust_type(self, adjust_type):
        self.adjustType = adjust_type

    @staticmethod
    def get_bookmark_list(n=0):
        bk = bookmarks.Bookmarks()
        book_list = bk.get_records(n)
        bk.close()
        return book_list

    @staticmethod
    def find_bookmark(path):
        bk = bookmarks.Bookmarks()
        bookmark = bk.find_bookmark(path)
        bk.close()
        return bookmark

    def add_bookmark(self, comic_name=None, comic_path=None, comic_page=None):

        if not comic_name:
            comic_name = self.get_comic_name()
        if not comic_path:
            comic_path = self.comic.directory + '/' + comic_name
        if not comic_page:
            comic_page = self.comic.get_current_page_number()

        bk = bookmarks.Bookmarks()
        bk.add_bookmark(comic_path, comic_name, comic_page)
        book_list = bk.get_records(self.NUM_BOOKMARK)
        bk.close()
        return book_list

    def remove_bookmark(self, comic_path=None, comic_name=None):

        if not comic_name:
            comic_name = self.get_comic_name()
        if not comic_path:
            comic_path = self.current_directory + '/' + comic_name

        bk = bookmarks.Bookmarks()
        bk.delete_bookmark(comic_path)
        book_list = bk.get_records(self.NUM_BOOKMARK)
        bk.close()
        return book_list

    def remove_bookmarks(self, comic_paths=None):
        bk = bookmarks.Bookmarks()
        for path in comic_paths:
            bk.delete_bookmark(path)

        book_list = bk.get_records(self.NUM_BOOKMARK)
        bk.close()
        return book_list

