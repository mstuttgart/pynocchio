from PySide import QtGui


class StatusBar(QtGui.QStatusBar):

    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)

        self.page_number = None
        self.page_resolution = None
        self.comic_path = None
        self.progress_bar = None

    def add_labels(self):

        if self.page_number is None:
            self.page_number = QtGui.QLabel(self)
            self.page_number.setMinimumWidth(120)
            self.addWidget(self.page_number, 0)

        if self.page_resolution is None:
            self.page_resolution = QtGui.QLabel(self)
            self.page_resolution.setMinimumWidth(140)
            self.addWidget(self.page_resolution, 1)

        if self.comic_path is None:
            self.comic_path = QtGui.QLabel(self)
            self.addWidget(self.comic_path, 2)

        self.page_number.show()
        self.page_resolution.show()
        self.comic_path.show()

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

    def add_progress_bar(self):

        if self.progress_bar is None:
            self.progress_bar = QtGui.QProgressBar(self)
            self.progress_bar.setFixedHeight(12)
            self.addWidget(self.progress_bar, 1)
            self.progress_bar.show()

    def remove_progress_bar(self):

        if self.progress_bar:
            self.removeWidget(self.progress_bar)
            self.progress_bar = None

    def set_comic_page(self, current_page, total_pages):

        if self.page_number is None:
            self.remove_progress_bar()
            self.add_labels()

        self.page_number.setText(self.tr('Page: ') + str(current_page) + '/' + str(total_pages))

    def set_page_resolution(self, width, height):

        if self.page_resolution is None:
            self.remove_progress_bar()
            self.add_labels()

        text = self.tr('Width: ') + str(width) + " "
        text += self.tr('Height: ') + str(height)
        self.page_resolution.setText(text)

    def set_comic_path(self, path):

        if self.comic_path is None:
            self.remove_progress_bar()
            self.add_labels()

        self.comic_path.setText(path)

    def set_progress_bar(self, n, total):

        if n > total:

            if self.progress_bar:
                self.remove_progress_bar()
                self.add_labels()

        else:

            if self.progress_bar is None:
                self.remove_labels()
                self.add_progress_bar()

            self.progress_bar.setMaximun(total)
            self.progress_bar.setValue(n)