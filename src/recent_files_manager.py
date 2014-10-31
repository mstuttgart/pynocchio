# -*- coding: utf-8 -*-

from PySide.QtCore import QObject
from PySide.QtCore import QSettings, QFileInfo
from Queue import Queue


class RecentFileManager(QObject):

    MAX_RECENT_FILES = 3

    def __init__(self, actions, parent=None):
        super(RecentFileManager, self).__init__(parent)

        self.MAX_RECENT_FILES = len(actions)
        self.recent_files_action_queue = Queue(len(actions))
        self.recent_files_action_list = []

        for i in actions:
            self.recent_files_action_list.append({'action': i, 'path': ''})

        self._load_settings()

    def load_file(self, file_path, comic_name):

        if self.recent_files_action_queue.qsize() >= self.MAX_RECENT_FILES:
            self.recent_files_action_queue.get()

        self.recent_files_action_queue.put((comic_name, file_path))

        for i in range(0, self.recent_files_action_queue.qsize()):

            text, path = self.recent_files_action_queue.get()
            idx = self.MAX_RECENT_FILES - 1 - i

            self.recent_files_action_list[idx]['action'].setText(text)
            self.recent_files_action_list[idx]['action'].setVisible(True)
            self.recent_files_action_list[idx]['path'] = path

            self.recent_files_action_queue.put((text, path))

    def get_action_path(self, object_name):

        for i in range(0, self.MAX_RECENT_FILES):

            if object_name == self.recent_files_action_list[i]['action'].objectName():
                return self.recent_files_action_list[i]['path']

        return None

    def _load_settings(self):

        import ConfigParser

        config = ConfigParser.ConfigParser()
        config.read("recent_files.ini")

        section_list = config.sections()
        section_list.reverse()

        for sec in section_list:
            comic_name = config.get(sec, 'name')
            comic_path = config.get(sec, 'path')
            self.load_file(comic_path, comic_name)

    def save_settings(self):

        import ConfigParser

        config = ConfigParser.ConfigParser()
        file_settings = open("recent_files.ini", "w")

        for i in range(0, len(self.recent_files_action_list)):

            if self.recent_files_action_list[i]['action'].isVisible():

                section = "RECENT_FILE_" + str(i)

                config.add_section(section)

                comic_name = self.recent_files_action_list[i]['action'].text()
                comic_path = self.recent_files_action_list[i]['path']

                config.set(section, "name", comic_name)
                config.set(section, "path", comic_path)

        config.write(file_settings)
        file_settings.close()




