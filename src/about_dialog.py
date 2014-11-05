# -*- coding:utf-8 -*-

from PySide import QtGui

import ui_about_dialog


class AboutDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)

        self.uiAboutDialog = ui_about_dialog.Ui_AboutDialog()
        self.uiAboutDialog.setupUi(self)
