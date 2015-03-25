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

from collections import deque
from PyQt4 import QtCore


class RecentFileManager(object):

    def __init__(self, max_items):
        self.recent_files_deque = deque(maxlen=max_items)

    def add(self, recent_file):
        self.recent_files_deque.appendleft(recent_file)

    def remove(self, recent_file):
        try:
            self.recent_files_deque.remove(recent_file)
        except ValueError as exp:
            print exp.message


        # try:
        #     self.recent_files_action_deque.pop()
        # except IndexError as exp:
        #     print exp.message

    # def _load_settings(self):
    #
    #     settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")
    #
    #     settings.beginGroup("recent_file")
    #     section_list = settings.allKeys()
    #
    #     if not section_list.isEmpty():
    #         python_list = list(section_list)
    #         python_list.sort(reverse=True)
    #
    #         for section in python_list:
    #             comic_path = settings.value(section, None, type=str)
    #             if comic_path:
    #                 self.update_recent_file_list(comic_path)
    #
    # def save_settings(self):
    #
    #     settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")
    #
    #     for act_dict in self.recent_files_action_list:
    #
    #         # Sections was added first because to
    #         # preserve order of recent files
    #         if act_dict['action'].isVisible():
    #             section = "recent_file/" + act_dict['action'].objectName()
    #             settings.setValue(section, act_dict['path'])
    # #
    # @staticmethod
    # def _stripped_name(full_file_name):
    #     from PyQt4.QtCore import QFileInfo
    #     return QFileInfo(full_file_name).fileName()



    # def __init__(self, actions):
    #     super(RecentFileManager, self).__init__()
    #
    #     self.MAX_RECENT_FILES = len(actions)
    #     self.recent_files_action_deque = deque()
    #     self.recent_files_action_list = []
    #
    #     for i in actions:
    #         self.recent_files_action_list.append({'action': i, 'path': ''})
    #
    #     self._load_settings()
    #
    # def update_recent_file_list(self, file_path):
    #     self._format_deque(file_path)
    #     self.recent_files_action_deque.appendleft(file_path)
    #     deque_range = range(len(self.recent_files_action_deque))
    #
    #     for i in deque_range:
    #         path = self.recent_files_action_deque.pop()
    #         idx = self.MAX_RECENT_FILES - 1 - i
    #
    #         self.recent_files_action_list[idx]['action'].setText(
    #             self._stripped_name(path))
    #         self.recent_files_action_list[idx]['action'].setVisible(True)
    #         self.recent_files_action_list[idx]['path'] = path
    #         self.recent_files_action_deque.appendleft(path)
    #
    # def _format_deque(self, path):
    #
    #     if self.recent_files_action_deque.count(path) != 0:
    #         self.recent_files_action_deque.remove(path)
    #
    #     if len(self.recent_files_action_deque) >= self.MAX_RECENT_FILES:
    #         self.recent_files_action_deque.pop()
    #
    # def get_action_path(self, object_name):
    #     for act in self.recent_files_action_list:
    #         if object_name == act['action'].objectName():
    #             return act['path']
    #     return None
    #
    # def _load_settings(self):
    #
    #     settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")
    #
    #     settings.beginGroup("recent_file")
    #     section_list = settings.allKeys()
    #
    #     if not section_list.isEmpty():
    #         python_list = list(section_list)
    #         python_list.sort(reverse=True)
    #
    #         for section in python_list:
    #             comic_path = settings.value(section, None, type=str)
    #             if comic_path:
    #                 self.update_recent_file_list(comic_path)
    #
    # def save_settings(self):
    #
    #     settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")
    #
    #     for act_dict in self.recent_files_action_list:
    #
    #         # Sections was added first because to
    #         # preserve order of recent files
    #         if act_dict['action'].isVisible():
    #             section = "recent_file/" + act_dict['action'].objectName()
    #             settings.setValue(section, act_dict['path'])
    #
    # @staticmethod
    # def _stripped_name(full_file_name):
    #     from PyQt4.QtCore import QFileInfo
    #     return QFileInfo(full_file_name).fileName()
