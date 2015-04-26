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

import xml.etree.ElementTree as Xml
from utility import Utility


class SettingsManager(object):

    @staticmethod
    def load(view, controller, xml_file='settings.xml', path=''):

        try:
            root = Xml.ElementTree(file=path.join(xml_file)).getroot()

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
            root = Xml.Element('settings')
            general = Xml.Element('general')
            view_settings = Xml.Element('view_settings')

            root.append(general)
            root.append(view_settings)

            current_directory = Xml.SubElement(general, 'current_directory')
            current_directory.text = controller.model.current_directory

            view_adjust = Xml.SubElement(view_settings, 'view_adjust')
            view_adjust.text = \
                str(view.action_group_view.checkedAction().objectName())

            show_toolbar = Xml.SubElement(view_settings, 'show_toolbar')
            show_toolbar.text = str(view.action_show_toolbar.isChecked())

            show_statusbar = Xml.SubElement(view_settings, 'show_statusbar')
            show_statusbar.text = str(view.action_show_statusbar.isChecked())

            Xml.ElementTree(root).write(path.join(xml_file))

        except IOError as exp:
            print '[ERROR] %s: %s' % (exp.strerror, exp.filename)











