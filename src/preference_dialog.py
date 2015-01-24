# -*- coding: UTF-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

PreferenceDialogForm, PreferenceDialogBase = uic.loadUiType('../view/preference_dialog.ui')


class PreferenceDialog(PreferenceDialogForm, PreferenceDialogBase):

    def __init__(self, model, parent=None):
        super(PreferenceDialog, self).__init__(parent)
        self.setupUi(self)

        self.comic_path = ''
        self.model = model

        self.comic_path_button.clicked.connect(self._comic_path_select)

    def _comic_path_select(self):

        path = QtGui.QFileDialog.getExistingDirectory(
            self.parent(), self.tr("Open Directory"), self.model.current_directory,
            QtGui.QFileDialog.ShowDirsOnly)

        if not path:
            return
