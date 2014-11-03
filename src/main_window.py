# -*- coding:utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from ui_main_window import *
from smartside import SmartSide
from model import Model
from go_to_dialog import *
# from preference_dialog import *
from about_dialog import *
from recent_files_manager import RecentFileManager


class MainWindow(QMainWindow, Ui_MainWindow, SmartSide):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.auto_connect()

        self.model = Model(self)
        self.goToDialog = None
        # self.preference_dialog = PreferenceDialog(self)
        self.aboutDialog = None

        self.scroll_area_viewer.model = self.model
        self.scroll_area_viewer.label = self.label

        self._adjust_main_window()

        self._on_action_show_statusbar__triggered()
        self._on_action_show_toolbar__triggered()

        self._create_action_group_view()

        self.action_about_qt.setIcon(QtGui.QIcon(':/trolltech/qmessagebox/images/qtlogo-64.png'))

        actions = []

        for i in range(5):
            act = QtGui.QAction(self, visible=False, triggered=self._on_action_recent_files)

            act.setObjectName(str(i))
            actions.append(act)
            self.menu_recent_files.addAction(act)

        self.recentFileManager = RecentFileManager(actions)

    def _adjust_main_window(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        x_center = (screen.width() - size.width()) / 2
        y_center = (screen.height() - size.height()) / 2
        self.move(x_center, y_center)

        self.setMinimumSize(QApplication.desktop().screenGeometry().size() * 0.8)

    def _create_action_group_view(self):

        self.actionGroupView = QtGui.QActionGroup(self)

        self.actionGroupView.addAction(self.action_original_fit)
        self.actionGroupView.addAction(self.action_vertical_adjust)
        self.actionGroupView.addAction(self.action_horizontal_adjust)
        self.actionGroupView.addAction(self.action_best_fit)

        checked_action = self.actionGroupView.checkedAction()
        self.model.adjustType = checked_action.text()

        self.actionGroupView.triggered.connect(
            self._on_action_group_view_adjust)

    def load(self, path):

        if self.model.load_comic(path):

            pix_map = self.model.get_current_page()

            if pix_map is not None:

                self.goToDialog = GoToDialog(self.model, self.scroll_area_viewer)

                self.scroll_area_viewer.label.setPixmap(pix_map)
                self.setWindowTitle(self.model.comic.name)

                self._update_status_bar()
                self._enable_actions()

                self.recentFileManager.update_recente_file_list(path)

            else:
                QMessageBox.information(self.tr('Error'), self.tr("Comic file is not loaded!!"))
        else:
            QMessageBox.information(self.tr('Error'), self.tr("Error to load file ") + path)

            self._update_view_actions()

    def _on_action_open__triggered(self):

        fname, filt = QtGui.QFileDialog.getOpenFileName(
            self.parent(), self.tr('Open comic file'), QtCore.QDir.currentPath(),
            self.tr('All supported files (*.zip *.cbz *.rar *.cbr *.tar *.cbt)\
            ;;Zip Files (*.zip *.cbz);;Rar Files (*.rar *.cbr)\
            ;;Tar Files (*.tar *.cbt);;All files (*)'))

        if len(fname) == 0:
            return

        self.load(fname)

        # self.setCursor(Qt.WaitCursor)

        # self.setCursor(Qt.ArrowCursor)

    def _on_action_open_folder__triggered(self):

        path = QtGui.QFileDialog.getExistingDirectory(
            None, self.tr("Open Directory"), QtCore.QDir.currentPath(),
            QtGui.QFileDialog.ShowDirsOnly)

        if len(path) == 0:
            return

        if self.model.load_folder(path):

            pix_map = self.model.get_current_page()

            if pix_map is not None:
                self.scroll_area_viewer.label.setPixmap(pix_map)
                self.setWindowTitle(self.model.comic.name)
                self.goToDialog = GoToDialog(self.model, self.scroll_area_viewer)

                self._update_status_bar()
                self._enable_actions()

            else:
                QMessageBox.information(self.tr('Error'), self.tr("Folder don't have image files!!"))
        else:
            QMessageBox.information(self.tr('Error'), self.tr("Error to load folder!!") + path)

    def _on_action_recent_files(self):

        action = self.sender()

        if action:
            path = self.recentFileManager.get_action_path(action.objectName())
            self.load(path)

    def _on_action_next_page__triggered(self):
        self.scroll_area_viewer.next_page()
        self._update_status_bar()
        self._update_view_actions()

    def _on_action_previous_page__triggered(self):
        self.scroll_area_viewer.previous_page()
        self._update_status_bar()
        self._update_view_actions()

    def _on_action_first_page__triggered(self):
        self.scroll_area_viewer.first_page()
        self._update_status_bar()
        self._update_view_actions()

    def _on_action_last_page__triggered(self):
        self.scroll_area_viewer.last_page()
        self._update_status_bar()
        self._update_view_actions()

    def _on_action_go_to_page__triggered(self):
        self.goToDialog.show()
        self._update_view_actions()

    def _on_action_rotate_left__triggered(self):
        self.scroll_area_viewer.rotate_left()

    def _on_action_rotate_right__triggered(self):
        self.scroll_area_viewer.rotate_right()

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
        self.scroll_area_viewer.label.setPixmap(self.model.get_current_page())
        self._update_status_bar()

    def _on_action_show_toolbar__triggered(self):

        if self.action_show_toolbar.isChecked():
            self.toolbar.show()
        else:
            self.toolbar.hide()

    def _on_action_show_statusbar__triggered(self):

        if self.action_show_statusbar.isChecked():
            self.statusbar.show()
            self._update_status_bar()
        else:
            self.statusbar.hide()

    def _on_action_about__triggered(self):

        if self.aboutDialog is None:
            self.aboutDialog = AboutDialog(self)

        self.aboutDialog.show()

    def _on_action_about_qt__triggered(self):
        QMessageBox.aboutQt(self, self.tr(u'About Qt'))

    def _on_action_exit__triggered(self):
        self.recentFileManager.save_settings()
        super(MainWindow, self).close()

    def _update_view_actions(self):

        if self.model.is_last_page():
            self.action_next_page.setEnabled(False)
            self.action_last_page.setEnabled(False)

        elif self.model.is_first_page():
            self.action_previous_page.setEnabled(False)
            self.action_first_page.setEnabled(False)

        else:
            self.action_next_page.setEnabled(True)
            self.action_last_page.setEnabled(True)
            self.action_previous_page.setEnabled(True)
            self.action_first_page.setEnabled(True)


    def _update_status_bar(self):

        if self.statusbar.isVisible() and self.model.comic is not None:

            n_page = str(self.model.get_current_page_index() + 1)
            page_width = str(self.model.get_current_page().width())
            page_height = str(self.model.get_current_page().height())
            page_title = self.model.get_current_page_title()

            label = self.tr('Page: ') + n_page + '\t\t\t\t\t' + self.tr('Title: ') \
                + page_title + '\t\t\t\t\t' + self.tr('Width: ') \
                + page_width + ' px' + '\t\t\t\t\t' + self.tr('Height: ') + page_height + ' px'

            self.statusbar.showMessage(label)

    def _update_recent_files_list(self):

        self.menu_recent_files.get

    def _enable_actions(self):

        self.action_fullscreen.setEnabled(True)
        self.action_original_fit.setEnabled(True)
        self.action_best_fit.setEnabled(True)
        self.action_horizontal_adjust.setEnabled(True)
        self.action_vertical_adjust.setEnabled(True)
        self.action_rotate_left.setEnabled(True)
        self.action_rotate_right.setEnabled(True)

        self.action_next_page.setEnabled(True)
        self.action_last_page.setEnabled(True)
        # self.action_first_page.setEnabled(True)
        # self.action_previous_page.setEnabled(True)
        self.action_go_to_page.setEnabled(True)

        self.action_add_bookmark.setEnabled(True)
        self.action_remove_bookmark.setEnabled(True)

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

    def repaint(self, *args, **kwargs):
        self._update_status_bar()
        super(MainWindow, self).repaint(*args, **kwargs)


