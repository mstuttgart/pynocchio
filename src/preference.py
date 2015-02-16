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

from preference_dialog import PreferenceDialog
from PyQt4.QtGui import QColor


class Preference(object):

    def __init__(self):
        self.background_color = QColor()
        self.show_statusbar_in_fullscreen = False
        self.show_toolbar_in_fullscreen = False
        
    def show_preference_dialog(self, main_window):
        preference_dialog = PreferenceDialog(preference=self, parent=main_window)
        preference_dialog.show()
        preference_dialog.exec_()



