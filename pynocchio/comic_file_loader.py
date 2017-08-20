# -*- coding: utf-8 -*-

from PyQt5 import QtCore

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ComicLoader(QtCore.QObject):

    progress = QtCore.pyqtSignal(int)
    done = QtCore.pyqtSignal()

    def __init__(self):
        super(ComicLoader, self).__init__()
        self.data = []

    def load(self, file_name):
        raise NotImplementedError('Must subclass me')
