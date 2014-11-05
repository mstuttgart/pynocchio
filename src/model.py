# -*- coding: UTF-8 -*-
from PySide import QtGui
from PySide import QtCore

import comic
import rar_loader
import zip_loader
import tar_loader
import folder_loader


class Model(object):
    def __init__(self):

        super(Model, self).__init__()

        self.comic = None
        self.original_pixmap = QtGui.QPixmap()

        self.adjustType = '&Horizontal Adjust'
        self.screenSize = 0
        self.rotateAngle = 0

    def load_comic(self, file_name):

        try:

            if zip_loader.ZipLoader.is_zip_file(file_name):
                return self._load_content(zip_loader.ZipLoader(), file_name)

            elif rar_loader.RarLoader.is_rar_file(file_name):
                return self._load_content(rar_loader.RarLoader(), file_name)

            elif tar_loader.TarLoader.is_tar_file(file_name):
                return self._load_content(tar_loader.TarLoader(), file_name)

        except IOError, err:
            print '%20s  %s' % (file_name, err)

        print self.tr('A error ocurred in open comic file!')
        return False

    def load_folder(self, folder_name):

        if folder_loader.FolderLoader.is_folder(folder_name):
            return self._load_content(folder_loader.FolderLoader(), folder_name)

        print 'Not is folder'
        return False

    def _load_content(self, loader, file_name):

        pages, titles, path, name = loader.load_file(file_name)
        if len(pages) == 0:
            return False

        self.comic = comic.Comic(name, path, pages, titles)
        self.current_page_index = 0

        return True

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

    def rotate_left(self):
        self.rotateAngle = (self.rotateAngle - 90) % 360
        return self.get_current_page()

    def rotate_right(self):
        self.rotateAngle = (self.rotateAngle + 90) % 360
        return self.get_current_page()

    def get_comic_name(self):

        if self.comic is not None:
            return self.comic.name

        return None

    def get_current_page(self):
        return self._load_pixmap_from_data()

    def get_current_page_title(self):

        if self.comic is not None:
            return self.comic.get_current_page_title()

        return None

    def set_current_page_index(self, idx):

        if self.comic is not None:
            self.comic.set_current_page_index(idx)

    def get_current_page_index(self):

        if self.comic is not None:
            return self.comic.current_page_index

        return -1

    def is_last_page(self):

        if self.comic.current_page_index + 1 == self.comic.get_number_of_pages():
            return True

        return False

    def is_first_page(self):

        if self.comic.current_page_index == 0:
            return True

        return False

    def _load_pixmap_from_data(self):

        page = None

        if self.comic is not None:
            page = self.comic.get_current_page()

        if page is not None:
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

        if self.comic is not None:

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
