from PySide6.QtCore import Signal
from PySide6.QtGui import QColor, QCursor, QResizeEvent, Qt
from PySide6.QtWidgets import QScrollArea, QWidget


class QScrollAreaViewer(QScrollArea):
    """
    A custom QScrollArea with additional functionality for mouse dragging and resizing.
    """

    resizedSignal = Signal()

    def __init__(self, parent: QWidget) -> None:
        """
        Initializes the QScrollAreaViewer.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)

        self._dragMouse: bool = False
        self._dragPosition: dict[str, int] = {
            "x": 0,
            "y": 0,
        }

        self._cursor: QCursor = QCursor(Qt.OpenHandCursor)
        self.setCursor(self._cursor)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def resetScrollPosition(self) -> None:
        """
        Resets the vertical scroll bar position to the top.
        """
        self.verticalScrollBar().setValue(0)

    def changeBackgroundColor(self, color: QColor) -> None:
        """
        Changes the background color of the widget.

        Args:
            color (QColor): The new background color.
        """
        style = "QWidget { background-color: %s }" % color.name()
        self.setStyleSheet(style)

    def mousePressEvent(self, *args, **kwargs) -> None:
        """
        Handles the mouse press event to enable dragging.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self._dragMouse = True
        self._dragPosition["x"] = args[0].x()
        self._dragPosition["y"] = args[0].y()
        self._cursor = QCursor(Qt.ClosedHandCursor)
        self.setCursor(self._cursor)

        super().mousePressEvent(*args, **kwargs)

    def mouseReleaseEvent(self, *args, **kwargs) -> None:
        """
        Handles the mouse release event to disable dragging.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self._dragMouse = False
        self._cursor = QCursor(Qt.OpenHandCursor)
        self.setCursor(self._cursor)

        super().mouseReleaseEvent(*args, **kwargs)

    def mouseMoveEvent(self, *args, **kwargs) -> None:
        """
        Handles the mouse move event to implement dragging behavior.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if self._dragMouse:
            pos = args[0]

            scroll_position = {
                "x": self.horizontalScrollBar().sliderPosition(),
                "y": self.verticalScrollBar().sliderPosition(),
            }

            new_x = scroll_position["x"] + self._dragPosition["x"] - pos.x()
            new_y = scroll_position["y"] + self._dragPosition["y"] - pos.y()

            self.horizontalScrollBar().setSliderPosition(new_x)
            self.verticalScrollBar().setSliderPosition(new_y)

            self._dragPosition["x"] = pos.x()
            self._dragPosition["y"] = pos.y()

        super().mouseMoveEvent(*args, **kwargs)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """
        Handles the resize event and emits the resized signal.

        Args:
            event (QResizeEvent): The resize event.
        """
        super().resizeEvent(event)
        self.resizedSignal.emit()
