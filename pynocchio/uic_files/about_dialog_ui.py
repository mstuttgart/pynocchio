# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './forms/about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutDialog.resize(506, 363)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/others/pynocchio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        AboutDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        AboutDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(AboutDialog)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.about)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.about_text_browser = QtWidgets.QTextBrowser(self.about)
        self.about_text_browser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.about_text_browser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.about_text_browser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.about_text_browser.setSource(QtCore.QUrl("qrc:/others/others/about.html"))
        self.about_text_browser.setSearchPaths([''])
        self.about_text_browser.setOpenExternalLinks(True)
        self.about_text_browser.setObjectName("about_text_browser")
        self.horizontalLayout_2.addWidget(self.about_text_browser)
        self.tabWidget.addTab(self.about, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_close = QtWidgets.QPushButton(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/edit-delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_close.setIcon(icon1)
        self.button_close.setDefault(True)
        self.button_close.setFlat(False)
        self.button_close.setObjectName("button_close")
        self.horizontalLayout.addWidget(self.button_close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AboutDialog)
        self.tabWidget.setCurrentIndex(0)
        self.button_close.clicked.connect(AboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About Pynocchio"))
        self.about_text_browser.setHtml(_translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/others/pynocchio.png\" /> </p>\n"
"<p align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; color:#9bca22;\">Pynocchio 1.0.3</span> </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pynocchio is a image viewer specialized in comic book reading. </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Support a several comic formats like .ZIP, .RAR, .TAR, .CBT, .CBR, .CBZ and <br />has a elegant visual, free and easy to use. </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pynocchio is licensed under the <a href=\"https://github.com/pynocchio/pynocchio/raw/develop/LICENSE\"><span style=\" text-decoration: underline; color:#9bca3b;\">GNU General Public License</span></a>. </p>\n"
"<p align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; color:#9bca22;\">Web site</span> </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://pynocchio.github.io\"><span style=\" text-decoration: underline; color:#9bca3b;\">Pynocchio Website</span></a> <br /><a href=\"https://github.com/pynocchio/pynocchio\"><span style=\" text-decoration: underline; color:#9bca3b;\">Pynocchio Github Repository</span></a> </p>\n"
"<p align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; color:#9bca22;\">Third-party resources</span> </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pynocchio use some icons from <a href=\"https://store.kde.org/content/show.php/elementary+USU?content=148128\"><span style=\" text-decoration: underline; color:#9bca3b;\">Elementary USU Icon Theme</span></a>. </p>\n"
"<p align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; color:#9bca22;\">Credits</span> </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright(C) 2014-2016 by <a href=\"https://github.com/mstuttgart/\"><span style=\" text-decoration: underline; color:#9bca3b;\">Michell Stuttgart Faria</span></a> </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("AboutDialog", "About"))
        self.button_close.setText(_translate("AboutDialog", "Close"))

from . import main_window_view_rc
