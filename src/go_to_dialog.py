# -*- coding: UTF-8 -*-
from PyQt4 import QtCore, uic

GoToDialogDialogForm, GoToDialogBase = uic.loadUiType('../view/go_to_page_dialog.ui')


class GoToDialog(GoToDialogDialogForm, GoToDialogBase):
    def __init__(self, model, viewer, parent=None):
        super(GoToDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = model
        self.viewer = viewer

        self.dialogHeight = self.height()
        self.spinBox_go_page = self.spinBox_go_page
        self.spinBox_go_page.setValue(self.model.get_current_page_index() - 1)
        self.change_label_image()

    def accept(self, *args, **kwargs):
        super(GoToDialog, self).accept(*args, **kwargs)

        self.model.set_current_page_index(
            self.spinBox_go_page.value() - 1)
        self.viewer.update_view(self.model.get_current_page())

    def rejected(self, *args, **kwargs):
        super(GoToDialog, self).rejected(*args, **kwargs)
        self.model.set_current_page_index(
            int(self.lineEdit_current_page.text()))

    def change_label_image(self):
        self.model.set_current_page_index(self.spinBox_go_page.value() - 1)

        image_page = self.model.get_current_page()
        image_page = image_page.scaledToHeight(
            self.dialogHeight * 0.6, QtCore.Qt.SmoothTransformation)

        self.label_icon.setPixmap(image_page)

    def update(self):
        self.change_label_image()
        super(GoToDialog, self).update()

    def show(self):
        current_page_idx = self.model.get_current_page_index()
        num_page = self.model.comic.get_number_of_pages()

        self.lineEdit_current_page.setText(str(current_page_idx + 1))
        self.lineEdit_num_page.setText(str(num_page))

        self.spinBox_go_page.setValue(current_page_idx + 1)
        self.spinBox_go_page.setMaximum(num_page)

        super(GoToDialog, self).show()
