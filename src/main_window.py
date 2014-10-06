# -*- coding:utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from ui_main_window import *
from smartside import *
from model import Model
from go_to_dialog import *
from preference_dialog import *
from about_dialog import *


class MainWindow(QMainWindow, Ui_MainWindow, SmartSide):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.auto_connect()

        self.model = Model(self)

        self.scrollAreaViewer.model = self.model
        self.scrollAreaViewer.label = self.label

        self.actionGroupView = QtGui.QActionGroup(self)

        self.actionGroupView.addAction(self.action_original_fit)
        self.actionGroupView.addAction(self.action_vertical_adjust)
        self.actionGroupView.addAction(self.action_horizontal_adjust)
        self.actionGroupView.addAction(self.action_best_fit)

        checked_action = self.actionGroupView.checkedAction()
        self.model.adjustType = checked_action.text()

        self.actionGroupView.triggered.connect(self._on_action_group_view_adjust)

        self._centralize_window()

        self.goToDialog = None
        self.preference_dialog = PreferenceDialog(self)
        self.aboutDialog = AboutDialog(self)

        # Ajustamos o tamanho minimo que a janela pode assumir
        self.setMinimumSize(QApplication.desktop().screenGeometry().size() * 0.8)

        self._on_action_show_statusbar__triggered()
        self._on_action_show_toolbar__triggered()

    def _centralize_window(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def _on_action_open__triggered(self):

        pix_map, comic_title = self.model.open()
        self.scrollAreaViewer.label.setPixmap(pix_map)
        self.setWindowTitle(comic_title)

        self.goToDialog = GoToDialog(self.model, self.scrollAreaViewer)
        # self.statusbar.showMessage(str(self.model.comic.current_page_index+1))

    def _on_action_preferences__triggered(self):
        self.preference_dialog.show()

    def _on_action_next_page__triggered(self):
        self.scrollAreaViewer.next_page()

    def _on_action_previous_page__triggered(self):
        self.scrollAreaViewer.previous_page()

    def _on_action_first_page__triggered(self):
        self.scrollAreaViewer.first_page()

    def _on_action_last_page__triggered(self):
        self.scrollAreaViewer.last_page()

    def _on_action_go_to_page__triggered(self):
        self.goToDialog.show()

    def _on_action_rotate_left__triggered(self):
        self.scrollAreaViewer.rotate_left()

    def _on_action_rotate_right__triggered(self):
        self.scrollAreaViewer.rotate_right()

    def _on_action_fullscreen__triggered(self):

        if self.isFullScreen():
            self.menubar.show()
            self.showMaximized()
            self._on_action_show_toolbar__triggered()
            self._on_action_show_statusbar__triggered()

        else:
            self.showFullScreen()
            self.toolbar.hide()
            self.menubar.hide()
            self.statusbar.hide()

    def _on_action_group_view_adjust(self):
        checked_action = self.actionGroupView.checkedAction()
        self.model.adjustType = checked_action.text()
        self.scrollAreaViewer.label.setPixmap(self.model.get_current_page())

    def _on_action_show_toolbar__triggered(self):

        if self.action_show_toolbar.isChecked():
            self.toolbar.show()
        else:
            self.toolbar.hide()

    def _on_action_show_statusbar__triggered(self):

        if self.action_show_statusbar.isChecked():
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def _on_action_about__triggered(self):

        # msg = u'<center>' \
        #       u'<h1>Chromics</h1>' \
        #       u'<br>Copyright 2014<br>Michell Stuttgart Faria' \
        #       u'<>'
        #
        #       u'</center>'
        # QMessageBox.about(self, u'About App', msg)

        self.aboutDialog.show()

    def _on_action_about_qt__triggered(self):
        """Handler for the Help/About Qt action"""
        QMessageBox.aboutQt(self, self.tr(u'About Qt'))

    def keyPressEvent(self, event):

        key = event.key()

        if key == Qt.Key_F:
            self._on_action_fullscreen__triggered()

        elif key == Qt.Key_Escape and self.isFullScreen():
            self._on_action_fullscreen__triggered()

        else:
            super(MainWindow, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, *args, **kwargs):

        event = args[0]

        if event.button() == Qt.LeftButton:
            self._on_action_fullscreen__triggered()
        else:
            super(MainWindow, self).mousePressEvent(*args, **kwargs)
