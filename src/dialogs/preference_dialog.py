# -*- coding: UTF-8 -*-

from PySide.QtGui import QDialog

from ui_python_files.ui_preference_dialog import *


class PreferenceDialog(QDialog):
    def __init__(self, parent=None):
        super(PreferenceDialog, self).__init__(parent)

        self.preference_dialog = Ui_PreferenceDialog()
        self.preference_dialog.setupUi(self)
