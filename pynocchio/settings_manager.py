# -*- coding: utf-8 -*-

from PyQt5 import QtCore

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SettingsManager():

    def __init__(self):
        self.settings = QtCore.QSettings('Pynocchio', 'Pynocchio')

    def save_recent_files(self, recent_files_list):
        logger.info('Saving recent files')

        self.settings.beginWriteArray('recent_file_list')

        for idx, value in enumerate(recent_files_list):
            self.settings.setArrayIndex(idx)
            self.settings.setValue('recent_file', value)

        self.settings.endArray()

    def load_recent_files(self):
        logger.info('Loading recent files')

        recent_files_list = []
        size = self.settings.beginReadArray('recent_file_list')

        for idx in range(size):
            self.settings.setArrayIndex(idx)
            recent_files_list.append(self.settings.value('recent_file'))

        self.settings.endArray()
        return recent_files_list

    def save_view_adjust(self, object_name):
        logger.info('Saving view adjust: %s', object_name)
        self.settings.setValue('view_adjust', object_name)

    def load_view_adjust(self, default_object_name):
        logger.info('Loading view adjust')
        return self.settings.value('view_adjust', default_object_name)

    def save_current_directory(self, current_directory):
        logger.info('Saving current directory %s', current_directory)
        self.settings.setValue('current_directory', current_directory)

    def load_current_directory(self):
        logger.info('Loading current directory')
        return self.settings.value('current_directory', '.')
