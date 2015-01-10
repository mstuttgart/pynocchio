# -*- coding:utf-8 -*-

from PySide import QtGui


class AboutDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        import about_dialog_ui
        self.uiAboutDialog = about_dialog_ui.Ui_AboutDialog()
        self.uiAboutDialog.setupUi(self)
