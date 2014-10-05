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

        self.change_cursor()

    def next_page(self):
        self.update_view(self.model.next_page())

    def previous_page(self):
        self.update_view(self.model.previous_page())

    def first_page(self):
        self.update_view(self.model.first_page())

    def last_page(self):
        self.update_view(self.model.last_page())

    def rotate_left(self):
        self.update_view(self.model.rotate_left())

    def rotate_right(self):
        self.update_view(self.model.rotate_right())

    def update_view(self, pixmap):
        self.label.setPixmap(pixmap)
        self.verticalScrollBar().setValue(0)

    def change_cursor(self):

        if self.dragMouse:
            self.setCursor(Qt.ClosedHandCursor)
        else:
            self.setCursor(Qt.OpenHandCursor)

    def keyPressEvent(self, *args, **kwargs):

        key = args[0].key()
        modifiers = args[0].modifiers()

        if key == Qt.Key_Right:

            if modifiers == Qt.ControlModifier:
                self.last_page()
                print 'passei por aqui last'
            else:
                self.next_page()
                print 'passei por aqui right'

        elif key == Qt.Key_Left:

            if modifiers == Qt.ControlModifier:
                self.first_page()
                print 'passei por aqui first'
            else:
                self.previous_page()
                print 'passei por aqui left'

        elif key == Qt.Key_R:

            if modifiers == (Qt.ControlModifier | Qt.ShiftModifier):
                self.rotate_left()

            elif modifiers == Qt.ControlModifier:
                self.rotate_right()

        else:
            super(Viewer, self).keyPressEvent(*args, **kwargs)

        print 'keypress'

    def mousePressEvent(self, *args, **kwargs):

        event = args[0]

        self.dragMouse = True
        self.dragPosition['x'] = event.x()
        self.dragPosition['y'] = event.y()

        self.change_cursor()

        print 'mouse move'

    def mouseReleaseEvent(self, *args, **kwargs):

        self.dragMouse = False
        self.change_cursor()

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

            print 'mouse move event'

    def resizeEvent(self, *args, **kwargs):

        new_size = args[0].size()

        self.model.set_size(new_size)

        if self.model.comic is not None:
            self.label.setPixmap(self.model.get_current_page())

        print 'resize_event'

        super(Viewer, self).resizeEvent(*args, **kwargs)


