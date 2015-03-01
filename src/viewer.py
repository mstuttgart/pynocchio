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
from PyQt4 import QtCore, QtGui


class Viewer(QtGui.QScrollArea):
    def __init__(self, parent=None):

        super(Viewer, self).__init__(parent)

        self.model = None
        self.label = None
        self.drag_mouse = False
        self.drag_position = {'x': 0, 'y': 0}
        self.last_scroll_position = 0

        self.setMouseTracking(True)

        self.hide_cursor_timer = QtCore.QTimer()
        self.hide_cursor_timer.setSingleShot(True)
        self.hide_cursor_timer.timeout.connect(self._hide_cursor)

        self.setWidgetResizable(True)
        self._change_cursor()

    def next_page(self):
        self.update_view(self.model.next_page())
        self.last_scroll_position = self.verticalScrollBar().value()

        if not self.model.is_last_page():
            self.verticalScrollBar().setValue(0)

    def previous_page(self):
        self.update_view(self.model.previous_page())
        self.verticalScrollBar().setValue(self.last_scroll_position)

    def first_page(self):
        self.update_view(self.model.first_page())
        self.verticalScrollBar().setValue(0)

    def last_page(self):
        self.update_view(self.model.last_page())
        self.verticalScrollBar().setValue(0)

    def rotate_left(self):
        self.update_view(self.model.rotate_left())
        self.verticalScrollBar().setValue(0)

    def rotate_right(self):
        self.update_view(self.model.rotate_right())
        self.verticalScrollBar().setValue(0)

    def update_view(self, pix_map):
        if pix_map:
            self.label.setPixmap(pix_map)

    def _change_cursor(self):
        if self.drag_mouse:
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

    def change_background_color(self, color):
        style = "QWidget { background-color: %s }" % color.name()
        self.setStyleSheet(style)

    def mousePressEvent(self, *args, **kwargs):
        event = args[0]

        self.drag_mouse = True
        self.drag_position['x'] = event.x()
        self.drag_position['y'] = event.y()
        self._change_cursor()

        super(Viewer, self).mousePressEvent(*args, **kwargs)

    def mouseReleaseEvent(self, *args, **kwargs):
        self.drag_mouse = False
        self._change_cursor()
        self.hide_cursor_timer.start(2500)
        super(Viewer, self).mouseReleaseEvent(*args, **kwargs)

    def mouseMoveEvent(self, *args, **kwargs):
        event = args[0]
        self._change_cursor()

        if self.drag_mouse:
            scroll_position = {
                'x': self.horizontalScrollBar().sliderPosition(),
                'y': self.verticalScrollBar().sliderPosition()
            }

            new_x = scroll_position['x'] + self.drag_position['x'] - event.x()
            new_y = scroll_position['y'] + self.drag_position['y'] - event.y()

            self.horizontalScrollBar().setSliderPosition(new_x)
            self.verticalScrollBar().setSliderPosition(new_y)

            self.drag_position['x'] = event.x()
            self.drag_position['y'] = event.y()

        super(Viewer, self).mouseMoveEvent(*args, **kwargs)

    def resizeEvent(self, *args, **kwargs):
        new_size = args[0].size()

        if self.model:
            self.model.set_size(new_size)

        if self.model.comic:
            self.label.setPixmap(self.model.get_current_page())

        super(Viewer, self).resizeEvent(*args, **kwargs)
