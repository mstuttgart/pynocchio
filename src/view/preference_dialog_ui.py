# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_files/preference_dialog.ui'
#
# Created: Wed Apr  6 14:25:04 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_config_dialog(object):
    def setupUi(self, config_dialog):
        config_dialog.setObjectName("config_dialog")
        config_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        config_dialog.resize(400, 213)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pynocchio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        config_dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(config_dialog)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtGui.QTabWidget(config_dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_edit_color = ColorLine(self.groupBox)
        self.line_edit_color.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_color.sizePolicy().hasHeightForWidth())
        self.line_edit_color.setSizePolicy(sizePolicy)
        self.line_edit_color.setAutoFillBackground(True)
        self.line_edit_color.setFrame(False)
        self.line_edit_color.setReadOnly(True)
        self.line_edit_color.setObjectName("line_edit_color")
        self.horizontalLayout.addWidget(self.line_edit_color)
        self.background_color_button = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/categories/48/applications-painting.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.background_color_button.setIcon(icon1)
        self.background_color_button.setObjectName("background_color_button")
        self.horizontalLayout.addWidget(self.background_color_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.close_button = QtGui.QPushButton(config_dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(config_dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.close_button, QtCore.SIGNAL("clicked()"), config_dialog.close)
        QtCore.QMetaObject.connectSlotsByName(config_dialog)

    def retranslateUi(self, config_dialog):
        config_dialog.setWindowTitle(QtGui.QApplication.translate("config_dialog", "Pynocchio Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("config_dialog", "<html><head/><body><p>Background color: </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("config_dialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.close_button.setText(QtGui.QApplication.translate("config_dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from lib.color_line import ColorLine
import main_window_view_rc
