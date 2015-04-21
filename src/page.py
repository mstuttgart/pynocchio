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

from PyQt4 import QtGui
from base_parser import *


class Page(object):

    def __init__(self, data, title, number):
        self._pixmap = False
        self.data = data
        self.title = title
        self.number = number

    @property
    def pixmap(self):
        if not self._pixmap:
            self._pixmap = QtGui.QPixmap()
            self._pixmap.loadFromData(self.data)
        return self._pixmap


class OnlinePage(object):

    def __init__(self, url, title, number, parser):

        if not isinstance(parser, BaseParser):
            raise TypeError

        self.url = url
        self.title = title
        self.number = number
        self.parser = parser
        self._image_url = False

    @property
    def image_url(self):
        if not self._image_url:
            try:
                self._image_url = self.parser.update_image_url(self.url)[0]
            except IndexError as excp:
                print '[ERROR] image_url is empty. ', excp.message
                self._image_url = False

        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self.url = value
        self._image_url = False
