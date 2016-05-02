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

from PySide import QtCore


class SettingsManager(object):

    def __init__(self):
        self.settings = QtCore.QSettings('Pynocchio', 'Pynocchio')

    def save_recent_files(self, recent_files_list):
        self.settings.beginWriteArray('recent_file_list')

        for idx, value in enumerate(recent_files_list):
            self.settings.setArrayIndex(idx)
            self.settings.setValue("recent_file", value)

        self.settings.endArray()

    def load_recent_files(self):
        recent_files_list = []
        size = self.settings.beginReadArray("recent_file_list")

        for idx in xrange(size):
            self.settings.setArrayIndex(idx)
            recent_files_list.append(self.settings.value("recent_file"))

        self.settings.endArray()
        return recent_files_list

    def save_view_adjust(self, object_name):
        self.settings.setValue("view_adjust", object_name)

    def load_view_adjust(self, default_object_name):
        return self.settings.value('view_adjust', default_object_name)

    def save_current_directory(self, current_directory):
        self.settings.setValue('current_directory', current_directory)

    def load_current_directory(self):
        return self.settings.value('current_directory', '.')
