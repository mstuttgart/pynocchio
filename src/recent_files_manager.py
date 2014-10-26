# -*- coding: utf-8 -*-

from PySide.QtCore import QObject
from PySide.QtCore import QSettings, QFileInfo
from Queue import Queue


class RecentFileManager(QObject):

    MAX_RECENT_FILES = 5

    def __init__(self, parent=None):
        super(RecentFileManager, self).__init__(parent)
        self.recent_files_action_list = Queue(self.MAX_RECENT_FILES)

    def add_action(self, action):
        self.recent_files_action_list.put((action, action.text()))

    def load_file(self, file_path, comic_name):

        if not self.recent_files_action_list.empty():

            action, text = self.recent_files_action_list.get()
            action.setVisible(True)
            action.setText(comic_name)
            self.recent_files_action_list.put((action, file_path))


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





