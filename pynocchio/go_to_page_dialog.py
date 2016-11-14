# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

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

from PyQt5 import QtCore, QtWidgets

from .uic_files import go_to_page_dialog_ui
from .comic_page_handler_factory import ComicPageHandlerFactory


class GoToDialog(QtWidgets.QDialog):
    def __init__(self, comic_handler, parent=None):
        super(GoToDialog, self).__init__(parent=parent)

        self.ui = go_to_page_dialog_ui.Ui_GoPageDialog()
        self.ui.setupUi(self)

        page_qty = comic_handler.comic.get_number_of_pages()
        page_number = comic_handler.get_current_page().number

        self.model_handler = comic_handler
        self.handler = ComicPageHandlerFactory.create_handler(
            False, comic=comic_handler.comic, index=page_number - 1)

        self.last_page = page_number

        self.ui.total_page_label.setText(self.tr('of %d') % page_qty)

        self.ui.horizontal_slider.setMaximum(page_qty)
        self.ui.spin_box_go_page.setMaximum(page_qty)

        self.ui.spin_box_go_page.setValue(page_number)

    def update(self):

        step_qty = abs(self.ui.horizontal_slider.value() - self.last_page)

        if self.last_page < self.ui.horizontal_slider.value():
            go_action = self.handler.go_next_page
        else:
            go_action = self.handler.go_previous_page

        for go in [go_action] * step_qty:
            go()

        self.last_page = self.ui.spin_box_go_page.value()

        image_page = self.handler.get_current_page_image()
        image_page = image_page.scaledToHeight(self.height() * 0.6,
                                               QtCore.Qt.SmoothTransformation)
        self.ui.page_label.setPixmap(image_page)

        super(GoToDialog, self).update()

    def show(self):
        self.update()
        super(GoToDialog, self).show()
