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


class QScrollAreaViewer(QtGui.QScrollArea):
    def __init__(self, parent=None):

        super(QScrollAreaViewer, self).__init__(parent)

        self.main_window_view = None
        self.main_window_controller = None
        self.drag_mouse = False
        self.drag_position = {'x': 0, 'y': 0}
        # self.last_scroll_position = 0
        #
        self.setMouseTracking(True)
        #
        # # self.hide_cursor_timer = QtCore.QTimer()
        # # self.hide_cursor_timer.setSingleShot(True)
        # # self.hide_cursor_timer.timeout.connect(self._hide_cursor)
        #
        self.setCursor(QtCore.Qt.OpenHandCursor)

    def set_content(self, content):
        if content is not None:
            self.main_window_view.label.setPixmap(content)

    # def next_page(self):
    #     self.update_view(self.model.next_page())
    #     self.last_scroll_position = self.verticalScrollBar().value()
    #
    #     if not self.model.is_last_page():
    #         self.verticalScrollBar().setValue(0)
    #
    # def previous_page(self):
    #     self.update_view(self.model.previous_page())
    #     self.verticalScrollBar().setValue(self.last_scroll_position)
    #
    # def first_page(self):
    #     self.update_view(self.model.first_page())
    #     self.verticalScrollBar().setValue(0)
    #
    # def last_page(self):
    #     self.update_view(self.model.last_page())
    #     self.verticalScrollBar().setValue(0)
    #
    # def rotate_left(self):
    #     self.update_view(self.model.rotate_left())
    #     self.verticalScrollBar().setValue(0)
    #
    # def rotate_right(self):
    #     self.update_view(self.model.rotate_right())
    #     self.verticalScrollBar().setValue(0)
    #

    def change_background_color(self, color):
        style = "QWidget { background-color: %s }" % color.name()
        self.setStyleSheet(style)

    def mousePressEvent(self, *args, **kwargs):
        self.drag_mouse = True
        self.drag_position['x'] = args[0].x()
        self.drag_position['y'] = args[0].y()
        self.setCursor(QtCore.Qt.ClosedHandCursor)
        super(QScrollAreaViewer, self).mousePressEvent(*args, **kwargs)

    def mouseReleaseEvent(self, *args, **kwargs):
        self.drag_mouse = False
        self.setCursor(QtCore.Qt.OpenHandCursor)
        super(QScrollAreaViewer, self).mouseReleaseEvent(*args, **kwargs)

    def mouseMoveEvent(self, *args, **kwargs):

        if self.drag_mouse:
            scroll_position = {
                'x': self.horizontalScrollBar().sliderPosition(),
                'y': self.verticalScrollBar().sliderPosition()
            }

            new_x = scroll_position['x'] + self.drag_position['x'] - args[0].x()
            new_y = scroll_position['y'] + self.drag_position['y'] - args[0].y()

            self.horizontalScrollBar().setSliderPosition(new_x)
            self.verticalScrollBar().setSliderPosition(new_y)

            self.drag_position['x'] = args[0].x()
            self.drag_position['y'] = args[0].y()

        super(QScrollAreaViewer, self).mouseMoveEvent(*args, **kwargs)

    def resizeEvent(self, *args, **kwargs):
        self.main_window_view.update_current_view_container_size(args[0].size())
        super(QScrollAreaViewer, self).resizeEvent(*args, **kwargs)
