# -*- coding: UTF-8 -*-
from PySide import QtGui
from PySide import QtCore

import comic
import bookmarks


class Model(QtCore.QObject):

    NUM_BOOKMARK = 5

    def __init__(self, parent=None):

        super(Model, self).__init__(parent)

        self.comic = None
        self.original_pixmap = QtGui.QPixmap()
        self.adjustType = '&Horizontal Adjust'
        self.screenSize = 0
        self.rotateAngle = 0
        self.last_comic_path = ''
        self.next_comic_path = ''
        self.previous_comic_path = ''

    def load_comic(self, file_name, initial_page=0):

        if file_name == '':
            return

        try:
            import rar_loader
            import tar_loader
            import zip_loader

            if zip_loader.ZipLoader.is_zip_file(file_name):
                return self._load_content(zip_loader.ZipLoader(self), file_name, initial_page)

            elif rar_loader.RarLoader.is_rar_file(file_name):
                return self._load_content(rar_loader.RarLoader(self), file_name, initial_page)

            elif tar_loader.TarLoader.is_tar_file(file_name):
                return self._load_content(tar_loader.TarLoader(self), file_name, initial_page)

        except IOError, err:
            print '%20s  %s' % (file_name, err)

        print 'A error ocurred in open comic file!'
        return False

    def load_folder(self, folder_name, initial_page=0):
        import folder_loader

        if folder_loader.FolderLoader.is_folder(folder_name):
            return self._load_content(folder_loader.FolderLoader(), folder_name, initial_page)
        print 'Not is folder'
        return False

    def _load_content(self, loader, file_name, initial_page=0):
        pages, titles, path, name = loader.load_file(file_name)

        if len(pages) != 0:
            self.comic = comic.Comic(name, path, pages, titles)
            self.set_current_page_index(initial_page)
            self.last_comic_path = path
            return True
        else:
            # self.comic = None
            # self.set_current_page_index(0)
            return False

    def next_page(self):
        if self.comic is not None:
            self.comic.go_next_page()
        return self.get_current_page()

    def previous_page(self):
        if self.comic is not None:
            self.comic.go_previous_page()
        return self.get_current_page()

    def first_page(self):
        if self.comic is not None:
            self.comic.go_first_page()
        return self.get_current_page()

    def last_page(self):
        if self.comic is not None:
            self.comic.go_last_page()
        return self.get_current_page()

    def next_comic(self):
        return self.next_comic_path

    def previous_comic(self):
        return self.previous_comic_path

    def verify_comics_in_path(self, action_next_comic, action_previous_comic):

        from PySide.QtCore import QDir
        d = QDir(self.last_comic_path)
        d.setFilter(QDir.Files | QDir.NoDotAndDotDot)
        # d.setNameFilters(["*.cbr", "*.cbz", "*.rar", "*.zip", "*.tar", "*.7z", "*.cb7", "*.arj", "*.cbt"])
        d.setNameFilters(["*.cbr", "*.cbz", "*.rar", "*.zip", "*.tar", "*.cbt"])
        d.setSorting(QDir.Name | QDir.IgnoreCase | QDir.LocaleAware)

        str_list = d.entryList()
        str_list.sort()
        index = str_list.index(self.comic.name)

        if index == -1:
            return

        if index > 0:
            self.previous_comic_path = self.last_comic_path + "/" + str_list[index-1]
            action_previous_comic.setEnabled(True)
        else:
            self.previous_comic_path = ''
            action_previous_comic.setEnabled(False)

        if len(str_list) >= (index + 1):
            self.next_comic_path = self.last_comic_path + "/" + str_list[index+1]
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

            if self.adjustType == '&Vertical adjust':
                pix_map = pix_map.scaledToHeight(
                    self.screenSize.height(), QtCore.Qt.SmoothTransformation)

            elif self.adjustType == '&Horizontal adjust':
                pix_map = pix_map.scaledToWidth(
                    self.screenSize.width() * 0.8, QtCore.Qt.SmoothTransformation)

            elif self.adjustType == '&Whole page':
                pix_map = pix_map.scaledToWidth(
                    self.screenSize.width(), QtCore.Qt.SmoothTransformation)

            return pix_map

        return None

    def set_size(self, new_size):
        self.screenSize = new_size

    def set_adjust_type(self, adjust_type):
        self.adjustType = adjust_type

    def get_bookmark_list(self, n=0):
        bk = bookmarks.Bookmarks()
        book_list = bk.get_records(n)
        bk.close()
        return book_list

    def find_bookmark(self, path):
        bk = bookmarks.Bookmarks()
        bookmark = bk.find_bookmark(path)
        bk.close()
        return bookmark

    def add_bookmark(self, comic_name=None, comic_path=None, comic_page=None):

        if comic_name is None:
            comic_name = self.get_comic_name()

        if comic_path is None:
            comic_path = self.last_comic_path + '/' + comic_name

        if comic_page is None:
            comic_page = self.get_current_page_index()

        bk = bookmarks.Bookmarks()
        bk.add_bookmark(comic_path, comic_name, comic_page)
        book_list = bk.get_records(self.NUM_BOOKMARK)
        bk.close()
        return book_list

    def remove_bookmark(self, comic_path=None, comic_name=None):

        if comic_name is None:
            comic_name = self.get_comic_name()

        if comic_path is None:
            comic_path = self.last_comic_path + '/' + comic_name

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

