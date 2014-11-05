# -*- coding: UTF-8 -*-
from PySide import QtCore

from PySide.QtGui import QDialog

from ui_go_to_page_dialog import Ui_GoPageDialog


class GoToDialog(QDialog):
    def __init__(self, model, viewer, parent=None):
        super(GoToDialog, self).__init__(parent)

        self.uiGoPageDialog = Ui_GoPageDialog()

        self.uiGoPageDialog.setupUi(self)

        self.model = model
        self.viewer = viewer

        self.dialogHeight = self.height()
        self.change_label_image()

    def accept(self, *args, **kwargs):
        super(GoToDialog, self).accept(*args, **kwargs)

        self.model.set_current_page_index(
            self.uiGoPageDialog.spinBox_go_page.value() - 1)
        self.viewer.update_view(self.model.get_current_page())

    def rejected(self, *args, **kwargs):
        super(GoToDialog, self).rejected(*args, **kwargs)
        self.model.set_current_page_index(
            int(self.uiGoPageDialog.lineEdit_current_page.text()))

    def change_label_image(self):
        i = self.uiGoPageDialog.spinBox_go_page.value() - 1
        self.model.set_current_page_index(i)

        image_page = self.model.get_current_page()
        image_page = image_page.scaledToHeight(
            self.dialogHeight * 0.6, QtCore.Qt.SmoothTransformation)

        self.uiGoPageDialog.label_icon.setPixmap(image_page)

    def update(self):
        self.change_label_image()
        super(GoToDialog, self).update()

    def show(self):
        current_page_idx = self.model.get_current_page_index()
        num_page = self.model.comic.get_number_of_pages()

        self.uiGoPageDialog.lineEdit_current_page.setText(
            str(current_page_idx + 1))
        self.uiGoPageDialog.lineEdit_num_page.setText(str(num_page))

        self.uiGoPageDialog.spinBox_go_page.setValue(current_page_idx + 1)
        self.uiGoPageDialog.spinBox_go_page.setMaximum(num_page)

        super(GoToDialog, self).show()
