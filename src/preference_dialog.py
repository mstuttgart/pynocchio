# -*- coding:utf-8 -*-
# Copyright (C) 2015  Michell Stuttgart

# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3.0 of the License, or (at
# your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui
from PyQt4 import uic

PreferenceDialogForm, PreferenceDialogBase = uic.loadUiType(
    '../view/config_dialog.ui')


class PreferenceDialog(PreferenceDialogForm, PreferenceDialogBase):
    def __init__(self, model, viewer, parent=None):
        super(PreferenceDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = model
        self.viewer = viewer
        self.background_color_button.background_color = self.model.background_color
        self.background_color_button.clicked.connect(self._open_color_dialog)

    def _open_color_dialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.background_color_button.background_color = col

    def accept(self, *args, **kwargs):
        self.model.background_color = self.background_color_button.background_color
        self.viewer.setStyleSheet("QWidget { background-color: %s }" %
                                  self.model.background_color.name())
        super(PreferenceDialog, self).accept(*args, **kwargs)

    def rejected(self, *args, **kwargs):
        self.background_color_button.reset_background_color()
        super(PreferenceDialog, self).rejected(*args, **kwargs)