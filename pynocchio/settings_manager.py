# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class SettingsManager:

    def __init__(self):
        self.settings = QtCore.QSettings('Pynocchio', 'Pynocchio')

    def save_recent_files(self, recent_files_list):
        self.settings.beginWriteArray('recent_file_list')

        for idx, value in enumerate(recent_files_list):
            self.settings.setArrayIndex(idx)
            self.settings.setValue('recent_file', value)

        self.settings.endArray()

    def load_recent_files(self):
        recent_files_list = []
        size = self.settings.beginReadArray('recent_file_list')

        for idx in range(size):
            self.settings.setArrayIndex(idx)
            recent_files_list.append(self.settings.value('recent_file'))

        self.settings.endArray()
        return recent_files_list

    def save_view_adjust(self, object_name):
        self.settings.setValue('view_adjust', object_name)

    def load_view_adjust(self, default_object_name):
        return self.settings.value('view_adjust', default_object_name)

    def save_current_directory(self, current_directory):
        self.settings.setValue('current_directory', current_directory)

    def load_current_directory(self):
        return self.settings.value('current_directory', '.')

