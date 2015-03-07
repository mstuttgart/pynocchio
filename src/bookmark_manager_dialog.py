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
from PyQt4.QtSql import QSqlQueryModel, QSqlTableModel, QSqlDatabase, QSqlQuery
import logging

BookmarkManagerDialogForm, BookmarkManagerDialogBase = uic.loadUiType(
    'bookmark_manager_dialog.ui')

log = logging.getLogger(__name__)


class BookmarkManagerDialog(BookmarkManagerDialogForm,
                            BookmarkManagerDialogBase):
    def __init__(self, mdl, parent=None):
        super(BookmarkManagerDialog, self).__init__(parent)
        self.setupUi(self)

        # self.model = mdl
        # self.table = self.bookmark_table
        # self._update_table_content()
        # self.item_to_open = False

        self.db = QSqlDatabase().addDatabase("QSQLITE")
        self.db.setDatabaseName("bookmark.db")

        if self.db.open():

            self.model = QSqlTableModel(self, self.db)
            self.model.setTable('Bookmark')
            # self.model.setQuery("select comic_name, comic_path, comic_page, "
            #                     "page_data from Bookmark", self.db)

            self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
            self.model.select()
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Path")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Page")

            # project_view = self.bookmark_table
            self.bookmark_table.setModel(self.model)
            #
            self._format_table()
            #
            # # project_view.show()
            #
            # self.button_selection.clicked.connect(self._select_all_table_items)
            self.button_remove.clicked.connect(self._remove_table_item)
            # self.button_load.clicked.connect(self._get_comic_to_open)

        else:
            log.error("Unable to create talkdb file.")

        # sql = "DELETE FROM Bookmarks WHERE Path='%s';" % path
        # self.db.execute(sql)

    # def _update_table_content(self):
    #     record_list = self.model.get_bookmark_list()
    #     record_list_len = len(record_list)
    #     self.table.setRowCount(record_list_len)
    #
    #     for i in range(record_list_len):
    #         self.table.setItem(i, 0, QtGui.QTableWidgetItem(record_list[i][0]))
    #         self.table.setItem(i, 1, QtGui.QTableWidgetItem(record_list[i][1]))
    #         self.table.setItem(i, 2, QtGui.QTableWidgetItem(str(
    #             record_list[i][2])))
    #
    #     self.table.horizontalHeader().setResizeMode(
    #         0, QtGui.QHeaderView.ResizeToContents)
    #     self.table.horizontalHeader().setResizeMode(
    #         1, QtGui.QHeaderView.Stretch)
    #     self.table.horizontalHeader().setResizeMode(
    #         2, QtGui.QHeaderView.ResizeToContents)
    #
    #     if record_list:
    #         pix = QtGui.QPixmap()
    #         pix.loadFromData(record_list[3])
    #         self.label_page.setPixmpa(pix)
    #
    # def _update_table(self):
    #     self.model.setQuery("select comic_name, comic_path, comic_page, "
    #                         "page_data from Bookmark", self.db)

    def _format_table(self):
        self.bookmark_table.hideColumn(0)
        self.bookmark_table.hideColumn(4)

        self.bookmark_table.horizontalHeader().setResizeMode(
            0, QtGui.QHeaderView.ResizeToContents)
        self.bookmark_table.horizontalHeader().setResizeMode(
            1, QtGui.QHeaderView.Stretch)
        self.bookmark_table.horizontalHeader().setResizeMode(
            2, QtGui.QHeaderView.ResizeToContents)

    def _remove_table_item(self):

        option = QtGui.QMessageBox().warning(
            self, self.tr('Delete bookmarks'),
            self.tr('This action will go delete you bookmarks! Preceed?'),
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
            QtGui.QMessageBox.Ok)

        if option == QtGui.QMessageBox.Ok:
            selected_idx = self.bookmark_table.selectedIndexes()

            if selected_idx:
                for i in range(len(selected_idx)):
                    self.model.removeRow(selected_idx[i].row())

                self.model.submitAll()


        # self.model.select()

        # if option == QtGui.QMessageBox.Ok:
        #     # project_model = QSqlQueryModel()
        #     selected_list = self.bookmark_table.selectionModel().selectedRows()
        #
        #     for i in range(len(selected_list)):
        #         query = "DELETE FROM Bookmark WHERE comic_id=%d" % \
        #                 selected_list[i].row()
        #         self.model.QSqlQuery(query, self.db)
        #         # self.model.removeRows()
        #         # self.bookmark_table.setModel(self.model)
        #
        #     self._update_table()

        # sql = "DELETE FROM Bookmarks WHERE Path='%s';" % path
        # self.db.execute(sql)



    #
    #     selected_items = self.table.selectedItems()
    #
    #     if not selected_items:
    #         return
    #
    #     option = QtGui.QMessageBox().warning(
    #         self, self.tr('Delete bookmarks'),
    #         self.tr('This action will go delete you bookmarks! Preceed?'),
    #         QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
    #         QtGui.QMessageBox.Ok)
    #
    #     if option == QtGui.QMessageBox.Ok:
    #
    #         selected_items_len = len(selected_items)
    #         selected_items_i = selected_items_len / 3
    #         selected_items_f = selected_items_len - selected_items_i
    #
    #         paths = []
    #
    #         for i in range(selected_items_i, selected_items_f):
    #             path = selected_items[i].text()
    #             paths.append(path)
    #             self.table.removeRow(selected_items[i].row())
    #
    #         self.model.remove_bookmarks(paths)
    #
    # def _select_all_table_items(self):
    #
    #     self.bookmark_table.setRangeSelected(
    #         QtGui.QTableWidgetSelectionRange(
    #             0, 0, self.bookmark_table.rowCount() - 1, 2), True)

    # def _get_comic_to_open(self):
    #     items = self.table.selectedItems()
    #     if items:
    #         self.item_to_open = items[1].text()
    #     self.close()
