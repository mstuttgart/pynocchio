# -*- coding: utf-8 -*-

from collections import deque


class RecentFileManager(object):

    MAX_RECENT_FILES = 3

    def __init__(self, actions):
        super(RecentFileManager, self).__init__()

        self.MAX_RECENT_FILES = len(actions)
        self.recent_files_action_deque = deque()
        self.recent_files_action_list = []

        for i in actions:
            self.recent_files_action_list.append({'action': i, 'path': ''})

        self._load_settings()

    def load_file(self, file_path, comic_name):

        # if len(self.recent_files_action_deque) >= self.MAX_RECENT_FILES:
        #     self.recent_files_action_deque.pop()

        deque_size = len(self.recent_files_action_deque)

        for i in range(0, deque_size):

            elem = self.recent_files_action_deque.pop()

            if elem[0] != comic_name and elem[1] != file_path:
                self.recent_files_action_deque.appendleft(elem)

        # if self.recent_files_action_deque.count((comic_name, file_path)) != 0:
        #     try:
        #         self.recent_files_action_deque.remove((comic_name, file_path))
        #     except ValueError, err:
        #         print err

        self.recent_files_action_deque.appendleft((comic_name, file_path))

        deque_size = len(self.recent_files_action_deque)

        for i in range(0, deque_size):

            text, path = self.recent_files_action_deque.pop()
            idx = self.MAX_RECENT_FILES - 1 - i

            self.recent_files_action_list[idx]['action'].setText(text)
            self.recent_files_action_list[idx]['action'].setVisible(True)
            self.recent_files_action_list[idx]['path'] = path

            self.recent_files_action_deque.appendleft((text, path))

    def get_action_path(self, object_name):

        for act in self.recent_files_action_list:
            if object_name == act['action'].objectName():
                return act['path']

        return None

    def _load_settings(self):

        # import ConfigParser
        #
        # config = ConfigParser.ConfigParser()
        # config.read("recent_files.ini")
        #
        # section_list = config.sections()
        # section_list.reverse()
        #
        # for sec in section_list:
        #     comic_name = config.get(sec, 'name')
        #     comic_path = config.get(sec, 'path')
        #     self.load_file(comic_path, comic_name)

        import settings_manager

        ret = settings_manager.SettingsManager.load_settings("recent_files_2.ini")

        section_list = ret.keys()
        section_list.sort(reverse=True)

        for section in section_list:
            comic_name = ret[section]['name']
            comic_path = ret[section]['path']
            self.load_file(comic_path, comic_name)

    def save_settings(self):

        # import ConfigParser
        #
        # config = ConfigParser.ConfigParser()
        # file_settings = open("recent_files.ini", "w")
        #
        # for i in range(0, len(self.recent_files_action_list)):
        #
        #     if self.recent_files_action_list[i]['action'].isVisible():
        #
        #         section = "RECENT_FILE_" + str(i)
        #
        #         config.add_section(section)
        #
        #         comic_name = self.recent_files_action_list[i]['action'].text()
        #         comic_path = self.recent_files_action_list[i]['path']
        #
        #         config.set(section, "name", comic_name)
        #         config.set(section, "path", comic_path)
        #
        # config.write(file_settings)
        # file_settings.close()

        import settings_manager

        rf_dict = {}
        # aux_list = {}

        for act_dict in self.recent_files_action_list:

            # Sections was added first because to preserve order of recent files
            if act_dict['action'].isVisible():

                section = "RECENT_FILE_" + act_dict['action'].objectName()

                # aux_list[section] = self.recent_files_action_list[i]
                rf_dict[section] = {}

                # comic name and comic path
                rf_dict[section]['name'] = act_dict['action'].text()
                rf_dict[section]['path'] = act_dict['path']

        # for sec in rf_dict:

        settings_manager.SettingsManager.save_settings(rf_dict, "recent_files_2.ini")





