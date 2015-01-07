# -*- coding: UTF-8 -*-

from PySide.QtGui import QDialog


class PreferenceDialog(QDialog):
    def __init__(self, parent=None):
        super(PreferenceDialog, self).__init__(parent)
        import ui_preference_dialog
        self.preference_dialog = ui_preference_dialog.Ui_PreferenceDialog()
        self.preference_dialog.setupUi(self)
