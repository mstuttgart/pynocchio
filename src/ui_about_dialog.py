# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/about_dialog.ui'
#
# Created: Thu Oct 30 12:39:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(441, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_2 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        AboutDialog.setAutoFillBackground(False)
        AboutDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(AboutDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_widget = QtGui.QTabWidget(AboutDialog)
        self.tab_widget.setTabPosition(QtGui.QTabWidget.North)
        self.tab_widget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widge_about = QtGui.QWidget()
        self.tab_widge_about.setObjectName("tab_widge_about")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_widge_about)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtGui.QTextBrowser(self.tab_widge_about)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.tab_widget.addTab(self.tab_widge_about, "")
        self.horizontalLayout.addWidget(self.tab_widget)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About Pynocchio Comic Reader", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#302f2d;\">General Information</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pynocchio Comic Reader - version beta<br />by Michell Stuttgart Faria</p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; color:#302f2d;\">Contact: </span></p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: <a href=\"michellstut@gmail.com\"><span style=\" text-decoration: underline; color:#0057ae;\">michellstut</span></a></p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">github: <a href=\"https://github.com/MStuttgart\"><span style=\" text-decoration: underline; color:#0057ae;\">MStuttgart</span></a></p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#302f2d;\">License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Published under <a href=\"http://www.gnu.org/copyleft/gpl.html\"><span style=\" text-decoration: underline; color:#0057ae;\">GPL v3</span></a> license. </p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#302f2d;\">Third-party software and resources</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pynocchio use <a href=\"http://freeiconmaker.com/\"><span style=\" text-decoration: underline; color:#0057ae;\">FREE Icon Maker</span></a> to build icon set.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Icons pack by <a href=\"http://iconsweets2.com/\"><span style=\" text-decoration: underline; color:#0057ae;\">Icon Sweets 2 </span></a>and <a href=\"https://www.iconfinder.com/iconsets/streamline-icon-set-free-pack\"><span style=\" text-decoration: underline; color:#0057ae;\">Streamline icon set free pack.</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#0057ae;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_widge_about), QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))

import main_window_rc
