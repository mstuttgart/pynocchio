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

from PyQt4.QtGui import QStatusBar, QProgressBar, QLabel
from PyQt4.QtCore import pyqtSlot


class StatusBar(QStatusBar):
    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)

        self.page_number = None
        self.page_resolution = None
        self.comic_path = None
        self.progress_bar = None

    def add_page_number_label(self):
        if self.page_number is None:
            self.remove_progress_bar()
            self.page_number = QLabel(self)
            self.page_number.setMinimumWidth(120)
            self.addWidget(self.page_number, 0)

        self.page_number.show()

    def add_page_resolution_label(self):
        if self.page_resolution is None:
            self.remove_progress_bar()
            self.page_resolution = QLabel(self)
            self.page_resolution.setMinimumWidth(140)
            self.addWidget(self.page_resolution, 1)

        self.page_resolution.show()

    def add_comic_path_label(self):
        if self.comic_path is None:
            self.remove_progress_bar()
            self.comic_path = QLabel(self)
            self.addWidget(self.comic_path, 2)

        self.comic_path.show()

    def add_progress_bar(self, maximum_value=100):

        if self.progress_bar is None:
            self.remove_labels()
            self.progress_bar = QProgressBar()
            self.progress_bar.setFixedHeight(15)
            self.progress_bar.setMaximum(maximum_value)
            self.addWidget(self.progress_bar, 1)
            self.progress_bar.show()

    def remove_progress_bar(self):

        if self.progress_bar:
            self.removeWidget(self.progress_bar)
            self.progress_bar = None

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

    @pyqtSlot(int, int)
    def set_progressbar_value(self, n):
        self.add_progress_bar()
        self.progress_bar.setValue(n)

    @pyqtSlot()
    def close_progress_bar(self):
        self.remove_progress_bar()
        self.add_page_number_label()
        self.add_page_resolution_label()
        self.add_comic_path_label()

