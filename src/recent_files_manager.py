# -*- coding: utf-8 -*-

from collections import deque


class RecentFileManager(object):

    SETTING_FILE_NAME = "recent_files.ini"

    def __init__(self, actions):
        super(RecentFileManager, self).__init__()

        self.MAX_RECENT_FILES = len(actions)
        self.recent_files_action_deque = deque()
        self.recent_files_action_list = []

        for i in actions:
            self.recent_files_action_list.append({'action': i, 'path': ''})

        self._load_settings()

    def load_file(self, file_path):

        if self.recent_files_action_deque.count(file_path) != 0:
            self.recent_files_action_deque.remove(file_path)

        self.recent_files_action_deque.appendleft(file_path)

        if len(self.recent_files_action_deque) > self.MAX_RECENT_FILES:
            self.recent_files_action_deque.pop()

        deque_range = range(0, len(self.recent_files_action_deque))

        for i in deque_range:

            path = self.recent_files_action_deque.pop()
            idx = self.MAX_RECENT_FILES - 1 - i

            self.recent_files_action_list[idx]['action'].setText(self._stripped_name(path))
            self.recent_files_action_list[idx]['action'].setVisible(True)
            self.recent_files_action_list[idx]['path'] = path

            self.recent_files_action_deque.appendleft(path)

    def get_action_path(self, object_name):

        for act in self.recent_files_action_list:
            if object_name == act['action'].objectName():
                return act['path']

        return None

    def _load_settings(self):

        from settings_manager import SettingsManager

        ret = SettingsManager.load_settings(self.SETTING_FILE_NAME)
        section_list = ret.keys()
        section_list.sort(reverse=True)

        for section in section_list:
            comic_path = ret[section]['path']
            self.load_file(comic_path)

    def save_settings(self):

        from settings_manager import SettingsManager
        rf_dict = {}

        for act_dict in self.recent_files_action_list:

            # Sections was added first because to preserve order of recent files
            if act_dict['action'].isVisible():

                section = "RECENT_FILE_" + act_dict['action'].objectName()
                rf_dict[section] = {}
                rf_dict[section]['path'] = act_dict['path']

        SettingsManager.save_settings(rf_dict, self.SETTING_FILE_NAME)

    @staticmethod
    def _stripped_name(full_file_name):
        from PySide.QtCore import QFileInfo
        return QFileInfo(full_file_name).fileName()





