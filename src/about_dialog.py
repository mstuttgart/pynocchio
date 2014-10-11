# -*- coding:utf-8 -*-

from PySide.QtGui import QDialog
from ui_about_dialog import *


class AboutDialog(QDialog):

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)

        self.uiAboutDialog = Ui_AboutDialog()
        self.uiAboutDialog.setupUi(self)
