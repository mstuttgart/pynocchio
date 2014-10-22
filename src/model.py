# -*- coding: UTF-8 -*-
from PySide import QtCore, QtGui
from comic import Comic

from rar_loader import *
from zip_loader import *
from tar_loader import *
from folder_loader import *


class Model(QtCore.QObject):

    def __init__(self, parent=None):

        super(Model, self).__init__(parent)

        self.comic = None
        self.original_pixmap = QtGui.QPixmap()

        self.adjustType = '&Horizontal Adjust'
        self.screenSize = 0
        self.rotateAngle = 0

    def load_comic(self, file_name):

        if ZipLoader.is_zip_file(file_name):

            if not self._load_content(ZipLoader(), file_name):
                print self.tr('failed open comic!')

            return True

        elif RarLoader.is_rar_file(file_name):

            if not self._load_content(RarLoader(), file_name):
                print self.tr('failed open comic!')

            return True

        elif TarLoader.is_tar_file(file_name):

            if not self._load_content(TarLoader(), file_name):
                print self.tr('failed open comic!')

            return True

        self.tr('A error ocurred in open comic file!')

        # QMessageBox.information(self, self.tr('Error'), self.tr("File type is not supported!!"))

        return False

    def load_folder(self, folder_name):

        if FolderLoader.is_folder(folder_name):
            return self._load_content(FolderLoader(), folder_name)

        print 'Not is folder'
        return False

    def _load_content(self, loader, file_name):

        pages, titles, path, name = loader.load_file(file_name)

        if len(pages) == 0:
            return False

        self.comic = Comic(name, path, pages, titles)
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

        # return None

    def get_current_page_index(self):

        if self.comic is not None:
            return self.comic.current_page_index

        return -1

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
