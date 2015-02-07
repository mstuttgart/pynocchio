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

from PyQt4 import QtCore, uic

GoToDialogDialogForm, GoToDialogBase = uic.loadUiType(
    '../view/go_to_page_dialog.ui')


class GoToDialog(GoToDialogDialogForm, GoToDialogBase):
    def __init__(self, model, viewer, parent=None):
        super(GoToDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = model
        self.viewer = viewer

        # self.height = self.height()
        # self.spinBox_go_page = self.spinBox_go_page
        self.spinBox_go_page.setValue(
            self.model.comic.get_current_page_number())
        self.change_label_image()

    def accept(self, *args, **kwargs):
        self.model.set_current_page_index(self.spinBox_go_page.value() - 1)
        self.viewer.update_view(self.model.get_current_page())

        super(GoToDialog, self).accept(*args, **kwargs)

    def rejected(self, *args, **kwargs):
        self.model.set_current_page_index(
            int(self.lineEdit_current_page.text()))
        super(GoToDialog, self).rejected(*args, **kwargs)

    def change_label_image(self):
        self.model.set_current_page_index(self.spinBox_go_page.value() - 1)
        image_page = self.model.get_current_page()
        image_page = image_page.scaledToHeight(
            self.height() * 0.6, QtCore.Qt.SmoothTransformation)

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
