# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

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
#

from PySide import QtCore
from PySide import QtGui
from PySide import QtSql
from utility import Utility

from uic_files.bookmark_manager_dialog_ui \
    import Ui_Bookmark_Dialog


class BookmarkManagerDialog(QtGui.QDialog):

    SCALE_RATIO = 0.18

    def __init__(self, controller):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_Bookmark_Dialog()
        self.ui.setupUi(self)

        self.controller = controller
        path = Utility.get_dir_name(
            controller.model.settings_manager.settings.fileName())

        self.db = QtSql.QSqlDatabase().addDatabase("QSQLITE")
        self.db.setDatabaseName(path + u'/bookmark.db')

        if self.db.open():

            self.model = QtSql.QSqlTableModel(self, self.db)
            self.model.setTable('Bookmark')

            self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
            self.model.select()
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Page")

            self.ui.bookmark_table.setModel(self.model)
            self.ui.bookmark_table.hideColumn(0)
            self.ui.bookmark_table.hideColumn(1)
            self.ui.bookmark_table.hideColumn(4)

            self.ui.bookmark_table.horizontalHeader().setResizeMode(
                2, QtGui.QHeaderView.Stretch)
            self.ui.bookmark_table.horizontalHeader().setResizeMode(
                3, QtGui.QHeaderView.ResizeToContents)

            self.ui.button_remove.clicked.connect(self._remove_table_item)
            self.ui.button_load.clicked.connect(self._get_comic_to_open)

            selection = self.ui.bookmark_table.selectionModel()
            selection.selectionChanged.connect(self.selection_changed)

            self.no_cover_label = self.ui.page_image_label.pixmap(
            ).scaledToWidth(self.width() * self.SCALE_RATIO,
                            QtCore.Qt.SmoothTransformation)

            self.ui.page_image_label.setPixmap(self.no_cover_label)
            print '[INFO] Database load!'

        else:
            print "[ERROR] Unable to create db file."

    def selection_changed(self, selected):

        model_indexes = selected.indexes()

        if model_indexes:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(model_indexes[4].data())
            pixmap = pixmap.scaledToWidth(self.width() * self.SCALE_RATIO,
                                          QtCore.Qt.SmoothTransformation)
            self.ui.page_image_label.setPixmap(pixmap)
            self.ui.line_edit_path.setText(model_indexes[1].data())

        else:
            self.ui.page_image_label.setPixmap(self.no_cover_label)
            self.ui.line_edit_path.setText('')

    def _remove_table_item(self):

        option = QtGui.QMessageBox().warning(
            self, self.tr('Delete bookmarks'),
            self.tr('This action will go delete you bookmarks! Preceed?'),
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
            QtGui.QMessageBox.Ok)

        if option == QtGui.QMessageBox.Ok:
            selected_idx = self.ui.bookmark_table.selectedIndexes()

            if selected_idx:
                for index in selected_idx:
                    self.model.removeRow(index.row())

                self.model.submitAll()

    def _get_comic_to_open(self):
        selection_model = self.ui.bookmark_table.selectionModel()
        path = selection_model.selectedRows(1)[0].data()
        page = selection_model.selectedRows(3)[0].data()
        self.controller.open_comics(path, page - 1)
        self.close()

    def close(self):
        self.db.close()
        QtGui.QDialog.close(self)
