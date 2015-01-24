# -*- coding: UTF-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

PreferenceDialogForm, PreferenceDialogBase = uic.loadUiType('../view/config_dialog.ui')


class PreferenceDialog(PreferenceDialogForm, PreferenceDialogBase):

    def __init__(self, model, viewer, parent=None):
        super(PreferenceDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = model
        self.viewer = viewer
        self.background_color_button.background_color = self.model.background_color
        self.background_color_button.clicked.connect(self._open_color_dialog)

    def _open_color_dialog(self):
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.background_color_button.background_color = col

    def accept(self, *args, **kwargs):
        self.model.background_color = self.background_color_button.background_color
        self.viewer.setStyleSheet("QWidget { background-color: %s }" %
                                              self.model.background_color.name())
        super(PreferenceDialog, self).accept(*args, **kwargs)

    def rejected(self, *args, **kwargs):
        self.background_color_button.reset_background_color()
        super(PreferenceDialog, self).rejected(*args, **kwargs)