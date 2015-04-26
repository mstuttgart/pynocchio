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

import xml.etree.ElementTree as xml
from utility import Utility

# settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")
#
#         settings.setValue("view_adjust",
#                           self.actionGroupView.checkedAction().objectName())
#         settings.setValue("show_toolbar",
#                           self.action_show_toolbar.isChecked())
#         settings.setValue("show_statusbar",
#                           self.action_show_statusbar.isChecked())
#         settings.setValue("directory", self.model.current_directory)
#         settings.setValue("background_color", self.preferences.background_color)
#
#         settings.setValue("recent_file_list_lenght",
#                           len(self.recent_file_manager.recent_files_deque))
#
#         for i in range(len(self.recent_file_manager.recent_files_deque)):
#             settings.setValue("recent_file_%d_comic_name" % i,
#                               self.recent_file_manager.get(i).comic_name)
#             settings.setValue("recent_file_%d_comic_path" % i,
#                               self.recent_file_manager.get(i).comic_path)


# settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")
#         view_adjust = settings.value(
#             'view_adjust', self.actionGroupView.checkedAction().objectName(),
#             type=str)
#
#         for act in self.actionGroupView.actions():
#             if act.objectName() == view_adjust:
#                 act.setChecked(True)
#                 self.model.adjustType = act.objectName()
#
#         show_toolbar = settings.value('show_toolbar',
#                                       self.action_show_toolbar.isChecked(),
#                                       type=bool)
#
#         self.action_show_toolbar.setChecked(show_toolbar)
#
#         show_status_bar = settings.value('show_statusbar',
#                                          self.action_show_statusbar.isChecked(),
#                                          type=bool)
#
#         self.action_show_statusbar.setChecked(show_status_bar)
#
#         self.model.current_directory = settings.value(
#             'directory', self.model.current_directory, type=str)
#
#         color_name = settings.value('background_color',
#                                     self.preferences.background_color,
#                                     type=QtGui.QColor)
#
#         self.preferences.background_color = QtGui.QColor(color_name)
#         self.viewer.change_background_color(self.preferences.background_color)
#
#         num_actions = len(self.menu_recent_files.actions())
#
#         max_len = max(settings.value(
#             'recent_file_list_lenght', num_actions, type=int), num_actions)
#
#         for i in range(max_len):
#             comic_name = settings.value("recent_file_%d_comic_name" % i, None,
#                                         type=str)
#             comic_path = settings.value("recent_file_%d_comic_path" % i, None,
#                                         type=str)
#
#             if comic_path and comic_name:
#                 self.recent_file_manager.append_right(
#                     RecenteFiles(comic_name, comic_path))
#
#         self.on_action_show_toolbar_triggered()
#         self.on_action_show_statusbar_triggered()
# #

class SettingsManager(object):

    @staticmethod
    def load(view, controller, xml_file='settings.xml', path=''):

        try:
            root = xml.ElementTree(file=path.join(xml_file)).getroot()

            general = root.find('general')
            view_settings = root.find('view_settings')

            controller.model.current_directory = general.find(
                'current_directory').text or '.'

            view_adjust = view_settings.find('view_adjust').text

            for act in view.action_group_view.actions():
                if act.objectName() == view_adjust:
                    act.setChecked(True)
                    controller.model.fit_type = act.objectName()

            aux = Utility.convert_string_to_boolean(
                view_settings.find('show_toolbar').text)
            view.action_show_toolbar.setChecked(aux)

            aux = Utility.convert_string_to_boolean(
                view_settings.find('show_statusbar').text)
            view.action_show_statusbar.setChecked(aux)

            view.on_action_show_statusbar_triggered()
            view.on_action_show_toolbar_triggered()

        except IOError as exp:
            print '[ERROR] %s: %s' % (exp.strerror, exp.filename)

    @staticmethod
    def save(view, controller, xml_file='settings.xml', path=''):

        try:
            root = xml.Element('settings')
            general = xml.Element('general')
            view_settings = xml.Element('view_settings')

            root.append(general)
            root.append(view_settings)

            current_directory = xml.SubElement(general, 'current_directory')
            current_directory.text = controller.model.current_directory

            view_adjust = xml.SubElement(view_settings, 'view_adjust')
            view_adjust.text = \
                str(view.action_group_view.checkedAction().objectName())

            show_toolbar = xml.SubElement(view_settings, 'show_toolbar')
            show_toolbar.text = str(view.action_show_toolbar.isChecked())

            show_statusbar = xml.SubElement(view_settings, 'show_statusbar')
            show_statusbar.text = str(view.action_show_statusbar.isChecked())

            xml.ElementTree(root).write(path.join(xml_file))

        except IOError as exp:
            print '[ERROR] %s: %s' % (exp.strerror, exp.filename)











