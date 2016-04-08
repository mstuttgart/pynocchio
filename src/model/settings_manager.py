# -*- coding: utf-8 -*-
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

from PySide import QtCore


class SettingsManager(object):

    def __init__(self):
        self.settings = QtCore.QSettings('Pynocchio Comic Reader', 'Pynocchio')

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

    # @staticmethod
    # def save_settings(view, controller):
    #
    #     settings = QtCore.QSettings("pynocchio-comic-reader",
    #                                 "pynocchio-interface")
    #
    #     settings.setValue("view_adjust",
    #                       view.action_group_view.checkedAction().objectName())
    #     settings.setValue("show_toolbar",
    #                       view.action_show_toolbar.isChecked())
    #     settings.setValue("show_statusbar",
    #                       view.action_show_statusbar.isChecked())
    #     settings.setValue("directory", controller.model.current_directory)
    #     settings.setValue("background_color",
    #                       controller.preferences.background_color)
    #
    #     recent_files_deque = controller.recent_file_manager.recent_files_deque
    #
    #     invalid_paths = 0
    #     for i, value in enumerate(list(reversed(recent_files_deque))):
    #         if Utility.file_exist(value.path):
    #             settings.setValue("recent_file_%d_comic_name" % i,
    #                               value.file_name)
    #             settings.setValue("recent_file_%d_comic_path" % i, value.path)
    #         else:
    #             invalid_paths += 1
    #
    #     settings.setValue("recent_file_list_lenght",
    #                       len(recent_files_deque) - invalid_paths)
    #
    # @staticmethod
    # def load_settings(view, controller):
    #
    #     settings = QtCore.QSettings("pynocchio-comic-reader",
    #                                 "pynocchio-interface")
    #
    #     view_adjust = settings.value(
    #         'view_adjust', view.action_group_view.checkedAction().objectName(),
    #         type=str)
    #
    #     for act in view.action_group_view.actions():
    #         if act.objectName() == view_adjust:
    #             act.setChecked(True)
    #             controller.model.fit_type = act.objectName()
    #
    #     show_toolbar = settings.value('show_toolbar',
    #                                   view.action_show_toolbar.isChecked(),
    #                                   type=bool)
    #
    #     view.action_show_toolbar.setChecked(show_toolbar)
    #
    #     show_status_bar = settings.value('show_statusbar',
    #                                      view.action_show_statusbar.isChecked(),
    #                                      type=bool)
    #
    #     view.action_show_statusbar.setChecked(show_status_bar)
    #
    #     controller.model.current_directory = settings.value(
    #         'directory', controller.model.current_directory, type=str)
    #
    #     color_name = settings.value('background_color',
    #                                 controller.preferences.background_color,
    #                                 type=QtGui.QColor)
    #
    #     controller.preferences.background_color = QtGui.QColor(color_name)
    #     view.change_background_color(controller.preferences.background_color)
    #
    #     max_len = settings.value('recent_file_list_lenght', 0, type=int)
    #
    #     for i in range(max_len):
    #         comic_name = settings.value("recent_file_%d_comic_name" % i, False,
    #                                     type=str)
    #         comic_path = settings.value("recent_file_%d_comic_path" % i, False,
    #                                     type=str)
    #
    #         if comic_path and comic_name and Utility.file_exist(
    #                 Utility.convert_qstring_to_str(comic_path)):
    #             controller.recent_file_manager.append_left(comic_name,
    #                                                        comic_path)
    #
    #     view.on_action_show_toolbar_triggered()
    #     view.on_action_show_statusbar_triggered()
