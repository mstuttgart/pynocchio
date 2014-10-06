# -*- coding: UTF-8 -*-
from PySide.QtGui import QDialog
from PySide import QtCore

from ui_go_to_page_dialog import Ui_GoPageDialog


class GoToDialog(QDialog, Ui_GoPageDialog):

    def __init__(self, model, viewer, parent=None):

        super(GoToDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = model
        self.viewer = viewer

        current_page_idx = model.get_current_page_index()
        num_page = model.comic.get_number_of_pages()

        self.lineEdit_current_page.setText(str(current_page_idx + 1))
        self.lineEdit_num_page.setText(str(num_page))

        self.spinBox_go_page.setValue(current_page_idx + 1)
        self.spinBox_go_page.setMaximum(num_page)

        self.dialogHeight = self.height()
        self.change_label_image()

    def accept(self, *args, **kwargs):

        super(GoToDialog, self).accept(*args, **kwargs)

        self.model.set_current_page_index(self.spinBox_go_page.value() - 1)
        self.viewer.update_view(self.model.get_current_page())

    def rejected(self, *args, **kwargs):

        super(GoToDialog, self).rejected(*args, **kwargs)
        self.model.set_current_page_index(int(self.lineEdit_current_page.text()))

    def change_label_image(self):

        i = self.spinBox_go_page.value() - 1
        self.model.set_current_page_index(i)

        image_page = self.model.get_current_page()
        image_page = image_page.scaledToHeight(self.dialogHeight * 0.6, QtCore.Qt.SmoothTransformation)

        self.label_icon.setPixmap(image_page)

    def update(self):

        self.change_label_image()
        super(GoToDialog, self).update()

    def show(self):

        current_page_idx = self.model.get_current_page_index()

        self.lineEdit_current_page.setText(str(current_page_idx + 1))
        self.spinBox_go_page.setValue(current_page_idx + 1)

        super(GoToDialog, self).show()
