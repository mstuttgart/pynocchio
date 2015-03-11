# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui, QtCore, uic

from model import Model
from recent_files_manager import RecentFileManager
from status_bar import StatusBar
from preference import Preference


MainWindowForm, MainWindowBase = uic.loadUiType('main_window.ui')


class MainWindow(MainWindowBase, MainWindowForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.model = Model(self)
        self.viewer.model = self.model
        self.viewer.label = self.label
        self.viewer.main_window = self
        self.viewer.define_global_shortcuts()
        
        self.statusbar = StatusBar(self)
        self.setStatusBar(self.statusbar)

        self.on_action_show_statusbar_triggered()
        self.on_action_show_toolbar_triggered()

        self._create_action_group_view()
        self.action_about_qt.setIcon(
            QtGui.QIcon(':/trolltech/qmessagebox/images/qtlogo-64.png'))

        actions = []

        for i in range(5):
            act = QtGui.QAction(self)
            act.setVisible(False)
            act.triggered.connect(self._on_action_recent_files)
            act.setObjectName(str(i))
            actions.append(act)
            self.menu_recent_files.addAction(act)

        self.recentFileManager = RecentFileManager(actions)
        self.preferences = Preference()
        self._load_settings()
        self._init_bookmark_menu()
        self._adjust_main_window()
        # self._define_global_shortcuts()

    def _adjust_main_window(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        x_center = (screen.width() - size.width()) / 2
        y_center = (screen.height() - size.height()) / 2
        self.move(x_center, y_center)
        self.setMinimumSize(
            QtGui.QApplication.desktop().screenGeometry().size() * 0.8)

    # def _define_global_shortcuts(self):

    #     QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+Left"), self.viewer,
    #                     self.on_action_previous_comic_triggered)
    #     QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Left"), self.viewer,
    #                     self.on_action_first_page_triggered)
    #     QtGui.QShortcut(QtGui.QKeySequence("Left"), self.viewer,
    #                     self.on_action_previous_page_triggered)
    #     QtGui.QShortcut(QtGui.QKeySequence("Right"), self, 
    #         self.on_action_next_page_triggered, context=QtCore.Qt.ApplicationShortcut)
    #     QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Right"), self.viewer,
    #                     self.on_action_last_page_triggered)
    #     QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+Right"), self.viewer,
    #                     self.on_action_next_comic_triggered)

    #     QtGui.QShortcut(QtGui.QKeySequence("Ctrl+R"), self.viewer,
    #                     self.on_action_rotate_right_triggered)
    #     QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+R"), self.viewer,
    #                     self.on_action_rotate_left_triggered)

    def _create_action_group_view(self):
        self.actionGroupView = QtGui.QActionGroup(self)

        self.actionGroupView.addAction(self.action_original_fit)
        self.actionGroupView.addAction(self.action_vertical_adjust)
        self.actionGroupView.addAction(self.action_horizontal_adjust)
        self.actionGroupView.addAction(self.action_best_fit)

        self.model.adjustType = self.actionGroupView.checkedAction().text()

        self.action_original_fit.triggered.connect(
            self._on_action_group_view_adjust)
        self.action_vertical_adjust.triggered.connect(
            self._on_action_group_view_adjust)
        self.action_horizontal_adjust.triggered.connect(
            self._on_action_group_view_adjust)
        self.action_best_fit.triggered.connect(
            self._on_action_group_view_adjust)

    def load(self, path, initial_page=0):

        import utility, pynocchio_exception

        ph = utility.Utility.convert_qstring_to_str(path)
        if ph:
            path = ph

        try:
            self.model.load_comic(path, initial_page)
            self.viewer.label.setPixmap(self.model.get_current_page())
            self.setWindowTitle(self.model.comic.name)
            self._update_status_bar()
            self._enable_actions()
            self.recentFileManager.update_recent_file_list(path)
            self.model.current_directory = path
            self.model.verify_comics_in_path()
        except pynocchio_exception.OpenComicFileException as exc:
            print exc.msg
            QtGui.QMessageBox().information(self, self.tr('Error'), self.tr(
                "Error to load file ") + path)

        self._update_view_actions()

    @QtCore.pyqtSlot()
    def on_action_open_triggered(self):

        file_path = QtGui.QFileDialog().getOpenFileName(
            self, self.tr('Open comic file'), self.model.current_directory,
            self.tr(
                'All supported files (*.zip *.cbz *.rar *.cbr *.tar *.cbt);; '
                'Zip Files (*.zip *.cbz);; Rar Files (*.rar *.cbr);; '
                'Tar Files (*.tar *.cbt);; All files (*)'))

        if file_path:
            self.load(file_path)

    @QtCore.pyqtSlot()
    def on_action_save_image_triggered(self):

        if not self.model.comic:
            return

        import utility
        path = utility.Utility.get_home_dir() + \
               self.model.comic.get_current_page_title()

        file_path = QtGui.QFileDialog().getSaveFileName(
            self, self.tr('Save current page'), path,
            self.tr("Images (*.png *.xpm *.jpeg *.jpg *.gif)"))

        self.model.get_current_page().save(file_path)

    def _on_action_recent_files(self):
        action = self.sender()
        if action:
            path = self.recentFileManager.get_action_path(action.objectName())
            self.load(path)

    @QtCore.pyqtSlot()
    def on_action_next_page_triggered(self):
        self.viewer.next_page()
        self._update_status_bar()
        self._update_view_actions()

    @QtCore.pyqtSlot()
    def on_action_previous_page_triggered(self):
        self.viewer.previous_page()
        self._update_status_bar()
        self._update_view_actions()

    @QtCore.pyqtSlot()
    def on_action_first_page_triggered(self):
        self.viewer.first_page()
        self._update_status_bar()
        self._update_view_actions()

    @QtCore.pyqtSlot()
    def on_action_last_page_triggered(self):
        self.viewer.last_page()
        self._update_status_bar()
        self._update_view_actions()

    @QtCore.pyqtSlot()
    def on_action_go_to_page_triggered(self):
        import go_to_page_dialog

        go_to_dlg = go_to_page_dialog.GoToDialog(self.model, self.viewer)
        go_to_dlg.show()
        go_to_dlg.exec_()
        self._update_view_actions()

    @QtCore.pyqtSlot()
    def on_action_next_comic_triggered(self):
        file_name = self.model.next_comic()
        if file_name:
            self.load(file_name)

    @QtCore.pyqtSlot()
    def on_action_previous_comic_triggered(self):
        file_name = self.model.previous_comic()
        if file_name:
            self.load(file_name)

    @QtCore.pyqtSlot()
    def on_action_rotate_left_triggered(self):
        self.viewer.rotate_left()

    @QtCore.pyqtSlot()
    def on_action_rotate_right_triggered(self):
        self.viewer.rotate_right()

    @QtCore.pyqtSlot()
    def on_action_fullscreen_triggered(self):

        if self.isFullScreen():
            self.menubar.show()
            self._update_view_actions()
            self.showMaximized()
            self.on_action_show_toolbar_triggered()
            self.on_action_show_statusbar_triggered()
            self._update_status_bar()
        else:
            self.menubar.hide()
            if not self.preferences.show_toolbar_in_fullscreen:
                self.toolbar.hide()
            if not self.preferences.show_statusbar_in_fullscreen:
                self.statusbar.hide()
            self.showFullScreen()

    def _on_action_group_view_adjust(self):
        action = self.sender()

        if action:
            self.model.adjustType = action.objectName()
            self.viewer.label.setPixmap(
                self.model.get_current_page())
            self._update_status_bar()

    def _init_bookmark_menu(self):
        self.menu_recent_bookmarks.aboutToShow.connect(
            self._update_bookmarks_menu)

        actions = self.menu_recent_bookmarks.actions()
        for bk in actions:
            bk.triggered.connect(self._load_bookmark)

    def _update_bookmarks_menu(self):

        bk_actions = self.menu_recent_bookmarks.actions()
        bookmark_list = self.model.get_bookmark_list(len(bk_actions))

        for bk in bk_actions:
            bk.setVisible(False)

        for i in range(len(bookmark_list)):
            bk_text = '%s [%d]' % (bookmark_list[i].comic_name,
                                   bookmark_list[i].comic_page)
            bk_actions[i].setText(bk_text)
            bk_actions[i].setStatusTip(bookmark_list[i].comic_path)
            bk_actions[i].setVisible(True)

    @QtCore.pyqtSlot()
    def on_action_add_bookmark_triggered(self):
        self.model.add_bookmark()

    @QtCore.pyqtSlot()
    def on_action_remove_bookmark_triggered(self):
        self.model.remove_bookmark()

    @QtCore.pyqtSlot()
    def on_action_bookmark_manager_triggered(self):
        import bookmark_manager_dialog
        bookmark_dialog = bookmark_manager_dialog.BookmarkManagerDialog(self)
        bookmark_dialog.show()
        bookmark_dialog.exec_()

    def _load_bookmark(self):
        action = self.sender()
        if action:
            bk = self.model.get_bookmark_from_path(action.statusTip())
            if bk:
                self.load(QtCore.QString(bk.comic_path), bk.comic_page - 1)

    @QtCore.pyqtSlot()
    def on_action_show_toolbar_triggered(self):
        if self.action_show_toolbar.isChecked():
            self.toolbar.show()
        else:
            self.toolbar.hide()

    @QtCore.pyqtSlot()
    def on_action_show_statusbar_triggered(self):
        if self.action_show_statusbar.isChecked():
            self._update_status_bar()
            self.statusbar.show()
        else:
            self.statusbar.hide()

    @QtCore.pyqtSlot()
    def on_action_preference_dialog_triggered(self):
        self.preferences.show_preference_dialog(self)
        self.viewer.change_background_color(self.preferences.background_color)

    @QtCore.pyqtSlot()
    def on_action_about_triggered(self):
        # import about_dialog
        #
        # about_dlg = about_dialog.AboutDialog(self)
        # about_dlg.show()
        # about_dlg.exec_()

        text = '<p><justify>The <a ' \
               'href=https://github.com/pynocchio>Pynocchio Comic ' \
               'Reader</a> is an image viewer specifically designed  to ' \
               'handle comic books.<justify></p>'\
               '<justify><a href=https://github.com/pynocchio>Pynocchio Comic ' \
               'Reader</a> is licensed under the GPLv3.'\
               '<br>Copyright (C) 2014-2015 ' \
               '<a href=https://github.com/mstuttgart>' \
               'Michell Stuttgart Faria</a>'\
               '<br>Pynocchio use <a href=http://freeiconmaker.com>Free Icon ' \
               'Maker</a> to build icon set and '\
               '<a href=https://github.com/mstuttgart/elementary3-icon-theme ' \
               '>Elementary OS 3.1 icons</a>.</p></justify>'

        QtGui.QMessageBox().about(self, self.tr('About QChip8 Emulator'),
                                  self.tr(text))


    @QtCore.pyqtSlot()
    def on_action_about_qt_triggered(self):
        QtGui.QMessageBox().aboutQt(self, self.tr(u'About Qt'))

    @QtCore.pyqtSlot()
    def on_action_exit_triggered(self):
        self._save_settings()
        self.recentFileManager.save_settings()
        super(MainWindow, self).close()

    def _update_view_actions(self):

        if not self.model.comic:
            return

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

        if self.statusbar.isVisible() and self.model.comic:
            n_page = self.model.comic.get_current_page_number()
            pages_size = self.model.comic.get_number_of_pages()
            page_width = self.model.get_current_page().width()
            page_height = self.model.get_current_page().height()
            page_title = self.model.comic.get_current_page_title()

            self.statusbar.set_comic_page(n_page, pages_size)
            self.statusbar.set_page_resolution(page_width, page_height)
            self.statusbar.set_comic_path(page_title)

    def _enable_actions(self):

        self.action_save_image.setEnabled(True)

        self.action_fullscreen.setEnabled(True)
        self.action_original_fit.setEnabled(True)
        self.action_best_fit.setEnabled(True)
        self.action_horizontal_adjust.setEnabled(True)
        self.action_vertical_adjust.setEnabled(True)
        self.action_rotate_left.setEnabled(True)
        self.action_rotate_right.setEnabled(True)

        self.action_next_page.setEnabled(True)
        self.action_last_page.setEnabled(True)
        self.action_go_to_page.setEnabled(True)
        self.action_next_comic.setEnabled(True)
        self.action_previous_comic.setEnabled(True)

        self.action_add_bookmark.setEnabled(True)
        self.action_remove_bookmark.setEnabled(True)

    def _save_settings(self):

        settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")

        settings.setValue("view_adjust",
                          self.actionGroupView.checkedAction().objectName())
        settings.setValue("show_toolbar",
                          self.action_show_toolbar.isChecked())
        settings.setValue("show_statusbar",
                          self.action_show_statusbar.isChecked())
        settings.setValue("directory", self.model.current_directory)
        settings.setValue("background_color", self.preferences.background_color)

    def _load_settings(self):

        settings = QtCore.QSettings("Pynocchio", "Pynocchio Comic Reader")

        view_adjust = settings.value(
            'view_adjust', self.actionGroupView.checkedAction().objectName(),
            type=str)

        for act in self.actionGroupView.actions():
            if act.objectName() == view_adjust:
                act.setChecked(True)
                self.model.adjustType = act.objectName()

        show_toolbar = settings.value('show_toolbar',
                                      self.action_show_toolbar.isChecked(),
                                      type=bool)

        self.action_show_toolbar.setChecked(show_toolbar)

        show_status_bar = settings.value('show_statusbar',
                                         self.action_show_statusbar.isChecked(),
                                         type=bool)

        self.action_show_statusbar.setChecked(show_status_bar)

        self.model.current_directory = settings.value(
            'directory', self.model.current_directory, type=str)

        color_name = settings.value('background_color',
                                    self.preferences.background_color,
                                    type=QtGui.QColor)

        self.preferences.background_color = QtGui.QColor(color_name)
        self.viewer.change_background_color(self.preferences.background_color)
        self.on_action_show_toolbar_triggered()
        self.on_action_show_statusbar_triggered()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F:
            self.on_action_fullscreen_triggered()
        elif event.key() == QtCore.Qt.Key_Escape and self.isFullScreen():
            self.on_action_fullscreen_triggered()
        else:
            super(MainWindow, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        if args[0].button() == QtCore.Qt.LeftButton:
            self.on_action_fullscreen_triggered()
        else:
            super(MainWindow, self).mousePressEvent(*args, **kwargs)
