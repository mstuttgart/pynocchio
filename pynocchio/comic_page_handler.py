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

from PyQt5 import QtGui


class ComicPageHandler:

    def __init__(self, comic, index=0):
        self.comic = comic
        self._current_page_index = index

    def get_current_page(self):
        return self.comic.pages[self.current_page_index]

    def go_next_page(self):
        if self.current_page_index < self.comic.get_number_of_pages() - 1:
            self.current_page_index += 1
            return True
        return False

    def go_previous_page(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1
            return True
        else:
            return False

    def go_first_page(self):
        self.current_page_index = 0

    def go_last_page(self):
        self.current_page_index = self.comic.get_number_of_pages() - 1

    @property
    def current_page_index(self):
        return self._current_page_index

    @current_page_index.setter
    def current_page_index(self, idx):
        if 0 <= idx < self.comic.get_number_of_pages():
            self._current_page_index = idx

    def get_current_page_image(self):
        raise NotImplementedError('Must subclass me!')


class ComicPageHandlerSinglePage(ComicPageHandler):

    def get_current_page_image(self):
        pix_map = QtGui.QPixmap()
        pix_map.loadFromData(self.get_current_page().data)
        return pix_map


class ComicPageHandlerDoublePage(ComicPageHandler):

    def __init__(self, comic, index=0):
        super(ComicPageHandlerDoublePage, self).__init__(comic=comic,
                                                         index=index)
        self.manga_mode = False

    def go_next_page(self):
        if self.current_page_index < self.comic.get_number_of_pages() - 2:
            self.current_page_index += 2
            return True
        else:
            return False

    def go_previous_page(self):
        if self.current_page_index > 1:
            self.current_page_index -= 2
            return True
        else:
            return False

    def get_current_page_image(self):

        pages = []

        page_a = QtGui.QPixmap()
        page_a.loadFromData(self.get_current_page().data)

        try:

            page_b = QtGui.QPixmap()

            direction = -1 if self.get_current_page().number % 2 == 0 else 1

            page_b.loadFromData(
                self.comic.pages[self.current_page_index + direction].data)

        except IndexError:
            width = page_a.width()
            height = page_a.height()
        else:
            height = max(page_a.height(), page_b.height())

            if self.manga_mode or direction == -1:
                page_b, page_a = page_a, page_b

            width = page_a.width() + page_b.width()

            pages.append([page_a.width(), 0, page_b])

        pages.append([0, 0, page_a])

        double_page = QtGui.QPixmap(width, height)
        painter = QtGui.QPainter(double_page)

        for page in pages:
            painter.drawPixmap(page[0], page[1], page[2])

        return double_page
