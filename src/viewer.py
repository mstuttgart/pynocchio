# -*- coding:utf-8 -*-
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

from PyQt4 import QtCore
from PyQt4 import QtGui


class Viewer(QtGui.QScrollArea):
    def __init__(self, parent=None):

        super(Viewer, self).__init__(parent)

        self._model = None
        self._label = None
        self.dragMouse = False
        self.dragPosition = {'x': 0, 'y': 0}
        self.lastScrollPosition = 0

        self.setMouseTracking(True)

        self.hideCursorTimer = QtCore.QTimer()
        self.hideCursorTimer.setSingleShot(True)
        self.hideCursorTimer.timeout.connect(self._hide_cursor)
        # self.hideCursorTimer.start(2500)
        # self._change_cursor()

        self.setWidgetResizable(True)

    def next_page(self):
        self.update_view(self._model.next_page())
        self.lastScrollPosition = self.verticalScrollBar().value()

        if not self._model.is_last_page():
            self.verticalScrollBar().setValue(0)

    def previous_page(self):
        self.update_view(self._model.previous_page())
        self.verticalScrollBar().setValue(self.lastScrollPosition)

    def first_page(self):
        self.update_view(self._model.first_page())
        self.verticalScrollBar().setValue(0)

    def last_page(self):
        self.update_view(self._model.last_page())
        self.verticalScrollBar().setValue(0)

    def rotate_left(self):
        self.update_view(self._model.rotate_left())
        self.verticalScrollBar().setValue(0)

    def rotate_right(self):
        self.update_view(self._model.rotate_right())
        self.verticalScrollBar().setValue(0)

    def update_view(self, pix_map):
        if pix_map:
            self._label.setPixmap(pix_map)

    def _change_cursor(self):
        if self.dragMouse:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
        else:
            self.setCursor(QtCore.Qt.OpenHandCursor)

    def _hide_cursor(self):
        self.setCursor(QtCore.Qt.BlankCursor)

    def load_comic_cursor(self, loading):
        if loading:
            self.setCursor(QtCore.Qt.WaitCursor)
        else:
            self._change_cursor()

    def mousePressEvent(self, *args, **kwargs):
        event = args[0]

        self.dragMouse = True
        self.dragPosition['x'] = event.x()
        self.dragPosition['y'] = event.y()
        self._change_cursor()

        super(Viewer, self).mousePressEvent(*args, **kwargs)

    def mouseReleaseEvent(self, *args, **kwargs):
        self.dragMouse = False
        self._change_cursor()
        self.hideCursorTimer.start(2500)
        super(Viewer, self).mouseReleaseEvent(*args, **kwargs)

    def mouseMoveEvent(self, *args, **kwargs):
        event = args[0]
        self._change_cursor()

        if self.dragMouse:
            scroll_position = {
                'x': self.horizontalScrollBar().sliderPosition(),
                'y': self.verticalScrollBar().sliderPosition()
            }

            new_x = scroll_position['x'] + self.dragPosition['x'] - event.x()
            new_y = scroll_position['y'] + self.dragPosition['y'] - event.y()

            self.horizontalScrollBar().setSliderPosition(new_x)
            self.verticalScrollBar().setSliderPosition(new_y)

            self.dragPosition['x'] = event.x()
            self.dragPosition['y'] = event.y()

        super(Viewer, self).mouseMoveEvent(*args, **kwargs)

    # def resizeEvent(self, *args, **kwargs):
    # new_size = args[0].size()
    #
    #     # new_size = self.size()
    #                # + QtCore.QSize(self.horizontalScrollBar().height(), self.verticalScrollBar().width())
    #     if self._model:
    #         self._model.set_size(new_size)
    #
    #     if self._model.comic:
    #         self._label.setPixmap(self._model.get_current_page())
    #
    #     super(Viewer, self).resizeEvent(*args, **kwargs)

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def set_label(self, label):
        self._label = label
        # self.setMouseTracking(True)

    def get_label(self):
        return self._label

    model = property(fget=get_model, fset=set_model)
    label = property(fget=get_label, fset=set_label)
