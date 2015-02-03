# -*- coding: UTF-8 -*-
from PyQt4 import QtGui


class StatusBar(QtGui.QStatusBar):
    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)

        self.page_number = None
        self.page_resolution = None
        self.comic_path = None

    def add_page_number_label(self):
        if self.page_number is None:
            self.page_number = QtGui.QLabel(self)
            self.page_number.setMinimumWidth(120)
            self.addWidget(self.page_number, 0)

        self.page_number.show()

    def add_page_resolution_label(self):
        if self.page_resolution is None:
            self.page_resolution = QtGui.QLabel(self)
            self.page_resolution.setMinimumWidth(140)
            self.addWidget(self.page_resolution, 1)

        self.page_resolution.show()

    def add_comic_path_label(self):
        if self.comic_path is None:
            self.comic_path = QtGui.QLabel(self)
            self.addWidget(self.comic_path, 2)

        self.comic_path.show()

    def remove_labels(self):

        if self.page_number:
            self.removeWidget(self.page_number)
            self.page_number = None

        if self.page_resolution:
            self.removeWidget(self.page_resolution)
            self.page_resolution = None

        if self.comic_path:
            self.removeWidget(self.comic_path)
            self.comic_path = None

    def set_comic_page(self, current_page, total_pages):
        if not self.page_number:
            self.add_page_number_label()

        self.page_number.setText(
            self.tr('Page: ') + str(current_page) + '/' + str(total_pages))

    def set_page_resolution(self, width, height):
        if not self.page_resolution:
            self.add_page_resolution_label()

        text = self.tr('Resolution: ') + str(width) + 'x' + str(height) + ' px'
        self.page_resolution.setText(text)

    def set_comic_path(self, path):
        if not self.comic_path:
            self.add_comic_path_label()

        self.comic_path.setText(self.tr('Title: ') + path)
