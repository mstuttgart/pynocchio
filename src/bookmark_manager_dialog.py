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
#
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtSql import QSqlTableModel, QSqlDatabase
import logging

BookmarkManagerDialogForm, BookmarkManagerDialogBase = uic.loadUiType(
    'bookmark_manager_dialog.ui')

log = logging.getLogger(__name__)


class BookmarkManagerDialog(BookmarkManagerDialogForm,
                            BookmarkManagerDialogBase):

    SCALE_RATIO = 0.18

    def __init__(self, parent=None):
        super(BookmarkManagerDialog, self).__init__(parent)
        self.setupUi(self)

        self.main_window = parent
        self.db = QSqlDatabase().addDatabase("QSQLITE")
        self.db.setDatabaseName("bookmark.db")

        if self.db.open():

            self.model = QSqlTableModel(self, self.db)
            self.model.setTable('Bookmark')

            self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
            self.model.select()
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Page")

            self.bookmark_table.setModel(self.model)
            self.bookmark_table.hideColumn(0)
            self.bookmark_table.hideColumn(1)
            self.bookmark_table.hideColumn(4)

            self.bookmark_table.horizontalHeader().setResizeMode(
                2, QtGui.QHeaderView.Stretch)
            self.bookmark_table.horizontalHeader().setResizeMode(
                3, QtGui.QHeaderView.ResizeToContents)

            self.button_remove.clicked.connect(self._remove_table_item)
            self.button_load.clicked.connect(self._get_comic_to_open)

            self.bookmark_table.selectionModel().selectionChanged.connect(
                self.selection_changed)

            self.no_cover_label = self.page_image_label.pixmap().scaledToWidth(
                self.width() * self.SCALE_RATIO, QtCore.Qt.SmoothTransformation)

            self.page_image_label.setPixmap(self.no_cover_label)

        else:
            log.error("[ERROR] Unable to create talkdb file.")

    def selection_changed(self, current, previous):

        model_indexes = current.indexes()

        if model_indexes:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(model_indexes[4].data().toByteArray())
            pixmap = pixmap.scaledToWidth(self.width() * self.SCALE_RATIO,
                                          QtCore.Qt.SmoothTransformation)
            self.page_image_label.setPixmap(pixmap)
            self.line_edit_path.setText(model_indexes[1].data().toString())

        else:
            self.page_image_label.setPixmap(self.no_cover_label)
            self.line_edit_path.setText('')

    def _remove_table_item(self):

        option = QtGui.QMessageBox().warning(
            self, self.tr('Delete bookmarks'),
            self.tr('This action will go delete you bookmarks! Preceed?'),
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
            QtGui.QMessageBox.Ok)

        if option == QtGui.QMessageBox.Ok:
            selected_idx = self.bookmark_table.selectedIndexes()

            if selected_idx:
                for index in selected_idx:
                    self.model.removeRow(index.row())

                self.model.submitAll()

    def _get_comic_to_open(self):
        selection_model = self.bookmark_table.selectionModel()
        path = selection_model.selectedRows(1)[0].data().toString()
        page = selection_model.selectedRows(3)[0].data().toInt()[0]
        self.main_window.load(path, page - 1)
        self.close()

    def close(self):
        self.db.close()
        super(BookmarkManagerDialog, self).close()
