# -*- coding: UTF-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *


class Viewer(QScrollArea):

    def __init__(self, parent=None):

        super(Viewer, self).__init__(parent)

        self.model = None
        self.label = None

        self.dragMouse = False
        self.dragPosition = {'x': 0, 'y': 0}

        self.lastScrollPosition = 0

        self.change_cursor()

    def next_page(self):
        self.update_view(self.model.next_page())
        self.lastScrollPosition = self.verticalScrollBar().value()
        self.verticalScrollBar().setValue(0)

    def previous_page(self):
        self.update_view(self.model.previous_page())
        self.verticalScrollBar().setValue(self.lastScrollPosition)

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

        if pix_map is not None:
            self.label.setPixmap(pix_map)

    def change_cursor(self):

        if self.dragMouse:
            self.setCursor(Qt.ClosedHandCursor)
        else:
            self.setCursor(Qt.OpenHandCursor)

    def keyPressEvent(self, *args, **kwargs):

        key = args[0].key()
        modifiers = args[0].modifiers()

        if self.model.comic is None:
            return None

        if key == Qt.Key_Right:

            if modifiers == Qt.ControlModifier:
                self.last_page()
            else:
                self.next_page()

        elif key == Qt.Key_Left:

            if modifiers == Qt.ControlModifier:
                self.first_page()
            else:
                self.previous_page()

        elif key == Qt.Key_R:

            if modifiers == (Qt.ControlModifier | Qt.ShiftModifier):
                self.rotate_left()

            elif modifiers == Qt.ControlModifier:
                self.rotate_right()

        else:
            super(Viewer, self).keyPressEvent(*args, **kwargs)

    def mousePressEvent(self, *args, **kwargs):

        event = args[0]

        self.dragMouse = True
        self.dragPosition['x'] = event.x()
        self.dragPosition['y'] = event.y()

        self.change_cursor()

        super(Viewer, self).mousePressEvent(*args, **kwargs)

    def mouseReleaseEvent(self, *args, **kwargs):

        self.dragMouse = False
        self.change_cursor()

        super(Viewer, self).mouseReleaseEvent(*args, **kwargs)

    def mouseMoveEvent(self, *args, **kwargs):

        event = args[0]

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

    def resizeEvent(self, *args, **kwargs):

        new_size = args[0].size()

        self.model.set_size(new_size)

        if self.model.comic is not None:
            self.label.setPixmap(self.model.get_current_page())

        super(Viewer, self).resizeEvent(*args, **kwargs)
