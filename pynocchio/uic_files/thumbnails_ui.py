# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/thumbnails.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Thumbnails(object):
    def setupUi(self, Thumbnails):
        Thumbnails.setObjectName("Thumbnails")
        Thumbnails.resize(183, 195)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Thumbnails.sizePolicy().hasHeightForWidth())
        Thumbnails.setSizePolicy(sizePolicy)
        Thumbnails.setFloating(False)
        Thumbnails.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        Thumbnails.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QScrollArea()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dockWidgetContents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dockWidgetContents.setWidgetResizable(False)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dockWidgetContents.setWidget(self.widget)
        Thumbnails.setWidget(self.dockWidgetContents)

        self.retranslateUi(Thumbnails)
        QtCore.QMetaObject.connectSlotsByName(Thumbnails)

    def retranslateUi(self, Thumbnails):
        _translate = QtCore.QCoreApplication.translate
        Thumbnails.setWindowTitle(_translate("Thumbnails", "Thumbnails"))

