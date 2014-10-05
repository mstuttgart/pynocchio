# -*- coding: UTF-8 -*-

from PySide.QtGui import QDialog
from ui_preference_dialog import *


class PreferenceDialog(QDialog, Ui_PreferenceDialog):

    def __init__(self, parent=None):
        super(PreferenceDialog, self).__init__(parent)
        self.setupUi(self)

