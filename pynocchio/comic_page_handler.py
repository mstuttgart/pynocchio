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

from PyQt5 import QtCore, QtGui

from .comic import Comic
from .page import Page


class ComicPageHandler:
    def __init__(self, comic, initial_page=0):
        self.comic = comic
        self.current_page_index = initial_page

    def get_current_page(self):
        return self.comic.pages[self.current_page_index]

    def go_next_page(self):
        if self.current_page_index < self.comic.get_number_of_pages() - 1:
            self.current_page_index += 1

    def go_previous_page(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1

    def go_first_page(self):
        self.current_page_index = 0

    def go_last_page(self):
        self.current_page_index = self.comic.get_number_of_pages() - 1

    def set_current_page_index(self, idx):
        if idx in range(self.comic.get_number_of_pages()):
            self.current_page_index = idx

    def get_current_page_image(self):
        raise NotImplementedError('Must subclass me!')


class ComicPageHandlerSinglePage(ComicPageHandler):
    def get_current_page_image(self):
        pix_map = QtGui.QPixmap()
        pix_map.loadFromData(self.get_current_page().data)
        return pix_map


class ComicPageHandlerDoublePage(ComicPageHandler):
    def go_next_page(self):
        if self.current_page_index < self.comic.get_number_of_pages() - 2:
            self.current_page_index += 2

    def go_previous_page(self):
        if self.current_page_index > 1:
            self.current_page_index -= 2

    def get_current_page_image(self):

        pages = []

        page_left = QtGui.QPixmap()
        page_left.loadFromData(self.get_current_page().data)

        try:

            page_right = QtGui.QPixmap()
            page_right.loadFromData(
                self.comic.pages[self.current_page_index + 1].data)

            if page_left.height() < page_right.height():
                height = page_right.height()
            else:
                height = page_left.height()

            width = page_left.width() + page_right.width()

            pages.append([page_left.width(), 0, page_right])

        except IndexError:
            width = page_left.width()
            height = page_left.height()

        pages.append([0, 0, page_left])

        double_page = QtGui.QPixmap(width, height)
        painter = QtGui.QPainter(double_page)

        for page in pages:
            painter.drawPixmap(page[0], page[1], page[2])

        return double_page


class ComicPageHandlerFactory:
    read_mode = {
        False: ComicPageHandlerSinglePage,
        True: ComicPageHandlerDoublePage,
    }

    @staticmethod
    def create_handler(page_read_mode, comic, initial_page=0):
        return ComicPageHandlerFactory.read_mode[page_read_mode](
            comic, initial_page=initial_page)
