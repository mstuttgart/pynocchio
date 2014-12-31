# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/bookmark_manager_dialog.ui'
#
# Created: Wed Dec 31 02:39:30 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Bookmark_Dialog(object):
    def setupUi(self, Bookmark_Dialog):
        Bookmark_Dialog.setObjectName("Bookmark_Dialog")
        Bookmark_Dialog.resize(761, 329)
        self.verticalLayout = QtGui.QVBoxLayout(Bookmark_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bookmark_table = QtGui.QTableWidget(Bookmark_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmark_table.sizePolicy().hasHeightForWidth())
        self.bookmark_table.setSizePolicy(sizePolicy)
        self.bookmark_table.setAutoFillBackground(False)
        self.bookmark_table.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bookmark_table.setAutoScroll(True)
        self.bookmark_table.setAutoScrollMargin(9)
        self.bookmark_table.setTabKeyNavigation(True)
        self.bookmark_table.setProperty("showDropIndicator", False)
        self.bookmark_table.setDragDropOverwriteMode(False)
        self.bookmark_table.setAlternatingRowColors(True)
        self.bookmark_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.bookmark_table.setShowGrid(True)
        self.bookmark_table.setWordWrap(True)
        self.bookmark_table.setRowCount(5)
        self.bookmark_table.setColumnCount(3)
        self.bookmark_table.setObjectName("bookmark_table")
        self.bookmark_table.setColumnCount(3)
        self.bookmark_table.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.bookmark_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.bookmark_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.bookmark_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bookmark_table.setItem(0, 0, item)
        self.bookmark_table.horizontalHeader().setVisible(True)
        self.bookmark_table.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.bookmark_table)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_remove = QtGui.QPushButton(Bookmark_Dialog)
        self.button_remove.setObjectName("button_remove")
        self.gridLayout_2.addWidget(self.button_remove, 1, 1, 1, 1)
        self.button_exit = QtGui.QPushButton(Bookmark_Dialog)
        self.button_exit.setObjectName("button_exit")
        self.gridLayout_2.addWidget(self.button_exit, 1, 2, 1, 1)
        self.button_selection = QtGui.QPushButton(Bookmark_Dialog)
        self.button_selection.setObjectName("button_selection")
        self.gridLayout_2.addWidget(self.button_selection, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Bookmark_Dialog)
        QtCore.QObject.connect(self.button_exit, QtCore.SIGNAL("clicked()"), Bookmark_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Bookmark_Dialog)

    def retranslateUi(self, Bookmark_Dialog):
        Bookmark_Dialog.setWindowTitle(QtGui.QApplication.translate("Bookmark_Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.bookmark_table.setSortingEnabled(True)
        self.bookmark_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Bookmark_Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.bookmark_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Bookmark_Dialog", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.bookmark_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Bookmark_Dialog", "Page", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.bookmark_table.isSortingEnabled()
        self.bookmark_table.setSortingEnabled(False)
        self.bookmark_table.setSortingEnabled(__sortingEnabled)
        self.button_remove.setText(QtGui.QApplication.translate("Bookmark_Dialog", "Remover", None, QtGui.QApplication.UnicodeUTF8))
        self.button_exit.setText(QtGui.QApplication.translate("Bookmark_Dialog", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.button_selection.setText(QtGui.QApplication.translate("Bookmark_Dialog", "Selecionar tudo", None, QtGui.QApplication.UnicodeUTF8))

import main_window_rc
