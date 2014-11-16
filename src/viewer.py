# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide import QtGui


class Viewer(QtGui.QScrollArea):
    def __init__(self, parent=None):

        super(Viewer, self).__init__(parent)

        self._model = None
        self._label = None
        self.dragMouse = False
        self.dragPosition = {'x': 0, 'y': 0}
        self.lastScrollPosition = 0

        # self._label.setMouseTracking(True)
        self.setMouseTracking(True)

        self.hideCursorTimer = QtCore.QTimer()
        self.hideCursorTimer.setSingleShot(True)
        self.hideCursorTimer.timeout.connect(self._hide_cursor)
        self.hideCursorTimer.start(2500)

        # self._change_cursor()

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
        if pix_map is not None:
            self._label.setPixmap(pix_map)

    def _change_cursor(self):
        if self.dragMouse:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
        else:
            self.setCursor(QtCore.Qt.OpenHandCursor)

    def _hide_cursor(self):
        self.setCursor(QtCore.Qt.BlankCursor)

    def load_comic_cursor(self, loading):
        if loading is True:
            self.setCursor(QtCore.Qt.WaitCursor)
        else:
            self._change_cursor()

    def keyPressEvent(self, *args, **kwargs):

        key = args[0].key()
        modifiers = args[0].modifiers()

        if self._model.comic is None:
            return None

        if key == QtCore.Qt.Key_Right:

            if modifiers == QtCore.Qt.ControlModifier:
                self.last_page()
            else:
                self.next_page()

        elif key == QtCore.Qt.Key_Left:

            if modifiers == QtCore.Qt.ControlModifier:
                self.first_page()
            else:
                self.previous_page()

        elif key == QtCore.Qt.Key_R:

            if modifiers == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
                self.rotate_left()
            elif modifiers == QtCore.Qt.ControlModifier:
                self.rotate_right()
        else:
            super(Viewer, self).keyPressEvent(*args, **kwargs)

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
        self.hideCursorTimer.start(2500)

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
        self._model.set_size(new_size)

        if self._model.comic is not None:
            self._label.setPixmap(self._model.get_current_page())

        super(Viewer, self).resizeEvent(*args, **kwargs)

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def set_label(self, label):
        self._label = label
        self._label.setMouseTracking(True)

    def get_label(self):
        return self._label

    model = property(fget=get_model, fset=set_model)
    label = property(fget=get_label, fset=set_label)
