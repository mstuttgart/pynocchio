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

from PyQt4 import uic
from PyQt4.QtGui import QColorDialog

PreferenceDialogForm, PreferenceDialogBase = uic.loadUiType(
    '../view/config_dialog.ui')


class PreferenceDialog(PreferenceDialogForm, PreferenceDialogBase):

    def __init__(self, preference):
        super(PreferenceDialog, self).__init__()
        self.setupUi(self)

        self.preference = preference
        self.show_toolbar_in_fullscreen.setChecked(preference.show_toolbar_in_fullscreen)
        self.show_statusbar_in_fullscreen.setChecked(preference.show_statusbar_in_fullscreen)

        self.background_color_button.background_color =  \
            self.preference.background_color

        self.background_color_button.clicked.connect(self._open_color_dialog)

    def _open_color_dialog(self):
        col = QColorDialog().getColor()
        if col.isValid():
            self.preference.background_color = col
            self.background_color_button.background_color = col

    def close(self):
        self.preference.show_statusbar_in_fullscreen =  \
            self.show_statusbar_in_fullscreen.isChecked()

        self.preference.show_toolbar_in_fullscreen =  \
            self.show_toolbar_in_fullscreen.isChecked()

        self.preference.background_color = \
            self.background_color_button.background_color

        print self.preference.show_toolbar_in_fullscreen
        print self.preference.show_statusbar_in_fullscreen

        super(PreferenceDialog, self).close()
