# -*- coding: utf-8 -*-

from PySide.QtCore import QObject


class RecentFileManager(QObject):

    MaxRecentFiles = 5

    def __init__(self, parent=None):
        super(RecentFileManager, self).__init__(parent)

        self.recent_files_action_list = []
        self.current_file_path = ''

    def load_file(self, file_path):
        pass

    def adjust_for_current_file(self, file_path):
        pass

    def update_recent_action_list(self):
        pass




