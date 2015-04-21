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
import main_window_view
import main_window_model


class MainWindowController():
    def __init__(self):
        self.main_window_view = main_window_view.MainWindowView(self)
        self.main_window_model = main_window_model.MainWindowModel(self)

    @QtCore.pyqtSlot()
    def open(self):
        print

    @QtCore.pyqtSlot()
    def save_image(self):
        print

    @QtCore.pyqtSlot()
    def online_comics(self):
        self.main_window_view.setCentralWidget(self.web_view)
        print

    @QtCore.pyqtSlot()
    def next_page(self):
        print

    @QtCore.pyqtSlot()
    def previous_page(self):
        print

    @QtCore.pyqtSlot()
    def first_page(self):
        print

    @QtCore.pyqtSlot()
    def last_page(self):
        print

    @QtCore.pyqtSlot()
    def go_to_page(self):
        print

    @QtCore.pyqtSlot()
    def next_comic(self):
        print

    @QtCore.pyqtSlot()
    def previous_comic(self):
        print

    @QtCore.pyqtSlot()
    def rotate_left(self):
        print

    @QtCore.pyqtSlot()
    def rotate_right(self):
        print

    @QtCore.pyqtSlot()
    def fullscreen(self):
        print

    @QtCore.pyqtSlot()
    def add_bookmark(self):
        print

    @QtCore.pyqtSlot()
    def remove_bookmark(self):
        print

    @QtCore.pyqtSlot()
    def bookmark_manager(self):
        print

    @QtCore.pyqtSlot()
    def show_toolbar(self):
        print

    @QtCore.pyqtSlot()
    def show_statusbar(self):
        print

    @QtCore.pyqtSlot()
    def preference_dialog(self):
        print

    @QtCore.pyqtSlot()
    def about(self):
        # import about_dialog
        #
        # about_dlg = about_dialog.AboutDialog(self)
        # about_dlg.show()
        # about_dlg.exec_()

        text = '<p><justify>The <a ' \
               'href=https://github.com/pynocchio>Pynocchio Comic ' \
               'Reader</a> is an image viewer <br>' \
               'specifically designed  to ' \
               'handle comic books is licensed <br>under the ' \
               'GPLv3.<justify></p>'\
               '<br>Copyright (C) 2014-2015 ' \
               '<a href=https://github.com/mstuttgart>' \
               'Michell Stuttgart Faria</a>'\
               '<br>Pynocchio use <a href=http://freeiconmaker.com>Free Icon ' \
               'Maker</a> to build icon set and <br>'\
               '<a href=https://github.com/mstuttgart/elementary3-icon-theme ' \
               '>Elementary OS 3.1 icons</a>.</p></justify>'

        QtGui.QMessageBox().about(self.main_window_view,
                                  self.main_window_view.tr(
                                      'About Pynocchio Comic Reader'),
                                  self.main_window_view.tr(text))

    @QtCore.pyqtSlot()
    def about_qt(self):
        QtGui.QMessageBox().aboutQt(self.main_window_view,
                                    self.main_window_view.tr(u'About Qt'))

    @QtCore.pyqtSlot()
    def exit(self):
        self.main_window_view.close()

    def show(self):
        self.main_window_view.show()
