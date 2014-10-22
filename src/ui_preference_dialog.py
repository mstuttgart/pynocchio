# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/preference_dialog.ui'
#
# Created: Wed Oct 22 07:57:59 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PreferenceDialog(object):
    def setupUi(self, PreferenceDialog):
        PreferenceDialog.setObjectName("PreferenceDialog")
        PreferenceDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        PreferenceDialog.resize(374, 115)
        PreferenceDialog.setSizeGripEnabled(False)
        PreferenceDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(PreferenceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(PreferenceDialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_edit_color = QtGui.QLineEdit(self.widget)
        self.line_edit_color.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_color.setReadOnly(True)
        self.line_edit_color.setObjectName("line_edit_color")
        self.gridLayout_2.addWidget(self.line_edit_color, 2, 1, 1, 1)
        self.button_select_path = QtGui.QPushButton(self.widget)
        self.button_select_path.setObjectName("button_select_path")
        self.gridLayout_2.addWidget(self.button_select_path, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line_edit_path = QtGui.QLineEdit(self.widget)
        self.line_edit_path.setObjectName("line_edit_path")
        self.gridLayout.addWidget(self.line_edit_path, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 2)
        self.button_select_color = QtGui.QPushButton(self.widget)
        self.button_select_color.setObjectName("button_select_color")
        self.gridLayout_2.addWidget(self.button_select_color, 2, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtGui.QDialogButtonBox(PreferenceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PreferenceDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), PreferenceDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), PreferenceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferenceDialog)

    def retranslateUi(self, PreferenceDialog):
        PreferenceDialog.setWindowTitle(QtGui.QApplication.translate("PreferenceDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.button_select_path.setText(QtGui.QApplication.translate("PreferenceDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreferenceDialog", "Background Color: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferenceDialog", "Comic path:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_select_color.setText(QtGui.QApplication.translate("PreferenceDialog", "...", None, QtGui.QApplication.UnicodeUTF8))

