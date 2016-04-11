# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_files/progress_dialog.ui'
#
# Created: Mon Apr 11 19:10:09 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QProgressDialog(object):
    def setupUi(self, QProgressDialog):
        QProgressDialog.setObjectName("QProgressDialog")
        QProgressDialog.setWindowModality(QtCore.Qt.WindowModal)
        QProgressDialog.resize(400, 48)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QProgressDialog.sizePolicy().hasHeightForWidth())
        QProgressDialog.setSizePolicy(sizePolicy)
        QProgressDialog.setMaximumSize(QtCore.QSize(400, 116))
        self.progress_bar = QtGui.QProgressBar(QProgressDialog)
        self.progress_bar.setGeometry(QtCore.QRect(10, 10, 381, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        self.progress_bar.setMaximumSize(QtCore.QSize(381, 16777215))
        self.progress_bar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.progress_bar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progress_bar.setStatusTip("")
        self.progress_bar.setAutoFillBackground(True)
        self.progress_bar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progress_bar.setObjectName("progress_bar")

        self.retranslateUi(QProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(QProgressDialog)

    def retranslateUi(self, QProgressDialog):
        QProgressDialog.setWindowTitle(QtGui.QApplication.translate("QProgressDialog", "loading_comic", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_bar.setFormat(QtGui.QApplication.translate("QProgressDialog", "%p%", None, QtGui.QApplication.UnicodeUTF8))

