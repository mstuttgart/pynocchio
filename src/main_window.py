# -*- coding:utf-8 -*-

from PySide import QtGui
from PySide import QtCore

import smartside

import ui_main_window
import model
import go_to_dialog
import about_dialog
import recent_files_manager


class MainWindow(QtGui.QMainWindow, ui_main_window.Ui_MainWindow, smartside.SmartSide):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.auto_connect()

        self.model = model.Model()
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

        self.recentFileManager = recent_files_manager.RecentFileManager(actions)
        self._load_settings()

    def _adjust_main_window(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        x_center = (screen.width() - size.width()) / 2
        y_center = (screen.height() - size.height()) / 2
        self.move(x_center, y_center)

        self.setMinimumSize(QtGui.QApplication.desktop().screenGeometry().size() * 0.8)

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

                self.goToDialog = go_to_dialog.GoToDialog(self.model, self.scroll_area_viewer)
                self.scroll_area_viewer.label.setPixmap(pix_map)
                self.setWindowTitle(self.model.comic.name)
                self._update_status_bar()
                self._enable_actions()
                self.recentFileManager.update_recent_file_list(path)

            else:
                QtGui.QMessageBox.information(self.tr('Error'), self.tr("Comic file is not loaded!!"))
        else:
            QtGui.QMessageBox.information(self.tr('Error'), self.tr("Error to load file ") + path)

            self._update_view_actions()

    def _on_action_open__triggered(self):

        fname, filt = QtGui.QFileDialog.getOpenFileName(
            self.parent(), self.tr('Open comic file'), self.model.last_comic_path,
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
                self.goToDialog = go_to_dialog.GoToDialog(self.model, self.scroll_area_viewer)

                self._update_status_bar()
                self._enable_actions()

            else:
                QtGui.QMessageBox.information(self.tr('Error'), self.tr("Folder don't have image files!!"))
        else:
            QtGui.QMessageBox.information(self.tr('Error'), self.tr("Error to load folder!!") + path)

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

        # if self.aboutDialog is None:
        #     self.aboutDialog = about_dialog.AboutDialog(self)
        #
        # self.aboutDialog.show()

        msg = "<p align=\"left\"> The <b>Pynocchio Comic Reader</b> </p>" \
              "<p align=\"left\"> is an image viewer specifically designed to handle comic books.</p>" + \
              "<p align=\"left\">It reads ZIP, RAR and tar archives, as well as plain image files." +\
              "implemented with Qt4 framework.</p>" + \
              "<p align=\"left\">Pynocchio Comic Reader is licensed under the GNU General Public License." + \
              "<p align=\"left\">Copyright © 2014 Michell Stuttgart Faria</p>" + \
              "<p align=\"left\">Pynocchio use http://freeiconmaker.com to build icon set." + \
              "Icons pack by Icon Sweets 2 and Streamline icon set free pack.</p>"

        QtGui.QMessageBox.about(self, self.tr("About Pynocchio Comic Reader"), msg)


    def _on_action_about_qt__triggered(self):
        QtGui.QMessageBox.aboutQt(self, self.tr(u'About Qt'))

    def _on_action_exit__triggered(self):
        self._save_settings()
        self.recentFileManager.save_settings()
        super(MainWindow, self).close()

    def _update_view_actions(self):

        if self.model.is_last_page():
            self.action_next_page.setEnabled(False)
            self.action_last_page.setEnabled(False)
            self.action_previous_page.setEnabled(True)
            self.action_first_page.setEnabled(True)

        elif self.model.is_first_page():
            self.action_previous_page.setEnabled(False)
            self.action_first_page.setEnabled(False)
            self.action_next_page.setEnabled(True)
            self.action_last_page.setEnabled(True)

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

    def _save_settings(self):

        import settings_manager

        sett = {'view': {}, 'settings': {}}

        sett['view']['view_adjust'] = self.actionGroupView.checkedAction().text()
        sett['settings']['show_toolbar'] = self.action_show_toolbar.isChecked()
        sett['settings']['show_statusbar'] = self.action_show_statusbar.isChecked()
        sett['settings']['last_comic_path'] = self.model.last_comic_path

        settings_manager.SettingsManager.save_settings(sett, 'settings.ini')

    def _load_settings(self):

        import settings_manager
        from distutils import util

        sett = settings_manager.SettingsManager.load_settings('settings.ini')

        try:
            checked = util.strtobool(sett['settings']['show_toolbar'])
            self.action_show_toolbar.setChecked(checked)

            checked = util.strtobool(sett['settings']['show_statusbar'])
            self.action_show_statusbar.setChecked(checked)

            for act in self.actionGroupView.actions():
                if act.text() == sett['view']['view_adjust']:
                    act.setChecked(True)
                    self.model.adjustType = act.text()

            self.model.last_comic_path = sett['settings']['last_comic_path']

        except KeyError, err:
            print err

        self._on_action_show_toolbar__triggered()
        self._on_action_show_statusbar__triggered()

    def keyPressEvent(self, event):

        key = event.key()

        if key == QtCore.Qt.Key_F:
            self._on_action_fullscreen__triggered()

        elif key == QtCore.Qt.Key_Escape and self.isFullScreen():
            self._on_action_fullscreen__triggered()

        else:
            super(MainWindow, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, *args, **kwargs):

        event = args[0]

        if event.button() == QtCore.Qt.LeftButton:
            self._on_action_fullscreen__triggered()
        else:
            super(MainWindow, self).mousePressEvent(*args, **kwargs)




