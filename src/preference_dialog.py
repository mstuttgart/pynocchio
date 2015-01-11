# -*- coding: UTF-8 -*-
from PyQt4 import uic

PreferenceDialogForm, PreferenceDialogBase = uic.loadUiType('../view/preference_dialog.ui')


class PreferenceDialog(PreferenceDialogForm, PreferenceDialogBase):
    def __init__(self, parent=None):
        super(PreferenceDialog, self).__init__(parent)
        self.setupUi(self)
