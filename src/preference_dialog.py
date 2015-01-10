# -*- coding: UTF-8 -*-

from PySide.QtGui import QDialog


class PreferenceDialog(QDialog):
    def __init__(self, parent=None):
        super(PreferenceDialog, self).__init__(parent)
        import preference_dialog_ui
        self.preference_dialog = preference_dialog_ui.Ui_PreferenceDialog()
        self.preference_dialog.setupUi(self)
