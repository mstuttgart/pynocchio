# -*- coding: utf-8 -*-

from PySide.QtCore import QObject
from PySide.QtCore import QSettings, QFileInfo
from Queue import Queue


class RecentFileManager(QObject):

    MAX_RECENT_FILES = 3

    def __init__(self, parent=None):
        super(RecentFileManager, self).__init__(parent)
        self.recent_files_action_queue = Queue(self.MAX_RECENT_FILES)
        self.recent_files_action_list = []

    def add_action(self, action):
        self.recent_files_action_list.append({'action': action, 'path': ''})

    def load_file(self, file_path, comic_name):

        if self.recent_files_action_queue.qsize() >= self.MAX_RECENT_FILES:
            self.recent_files_action_queue.get()

        self.recent_files_action_queue.put((comic_name, file_path))

        for i in range(0, self.recent_files_action_queue.qsize()):

            text, path = self.recent_files_action_queue.get()

            self.recent_files_action_list[self.MAX_RECENT_FILES - 1 - i]['action'].setText(text)
            self.recent_files_action_list[self.MAX_RECENT_FILES - 1 - i]['action'].setVisible(True)
            self.recent_files_action_list[self.MAX_RECENT_FILES - 1 - i]['path'] = path

            self.recent_files_action_queue.put((text, path))

    def _load_settings(self):

        from PySide.QtCore import QSettings




    # def adjust_for_current_file(self, file_path):
    #     print 'teste'
    #
    #     self.current_file_path = file_path
    #
    #     settings = QSettings()
    #     recent_file_paths = settings.value("recentFiles").toStringList()
    #     recent_file_paths.removeAll(file_path)
    #     recent_file_paths.prepend(file_path)
    #
    #     while recent_file_paths.size() > self.MAX_RECENT_FILES:
    #         recent_file_paths.removeLast()
    #         settings.setValue("recentFiles", recent_file_paths)
    #
    #     self.update_recent_action_list()

    # def update_recent_action_list(self):
    #     print 'teste'
    #
    #
    #     settings = QSettings()
    #     recent_file_paths = settings.value("recentFiles")
    #
    #     if len(recent_file_paths) <= self.MAX_RECENT_FILES:
    #         it_end = recent_file_paths.size()
    #     else:
    #         it_end = self.MAX_RECENT_FILES
    #
    #     for i in range(0, it_end):
    #         stripped_name = QFileInfo(recent_file_paths.at(i)).fileName()
    #         self.recent_files_action_list[i].setText(stripped_name)
    #         self.recent_files_action_list[i].setData(recent_file_paths.at(i))
    #         self.recent_files_action_list[i].setVisible(True)
    #
    #     for i in range(it_end, self.MAX_RECENT_FILES):
    #         self.recent_files_action_list[i].setVisible(False)





