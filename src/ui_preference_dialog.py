# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preference_dialog.ui'
#
# Created: Sun Oct  5 12:01:51 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PreferenceDialog(object):
    def setupUi(self, PreferenceDialog):
        PreferenceDialog.setObjectName("PreferenceDialog")
        PreferenceDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        PreferenceDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(PreferenceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(PreferenceDialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 1, 1)
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
        self.label_2.setText(QtGui.QApplication.translate("PreferenceDialog", "Background Color: ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("PreferenceDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferenceDialog", "Comic path:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("PreferenceDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

