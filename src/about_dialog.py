# -*- coding:utf-8 -*-
from PyQt4 import uic

AboutDialogForm, AboutDialogBase = uic.loadUiType('../view/about_dialog.ui')


class AboutDialog(AboutDialogForm, AboutDialogBase):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
