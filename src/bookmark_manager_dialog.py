# -*- coding:utf-8 -*-

from PySide import QtGui

import ui_bookmark_manager_dialog
import model


class BookmarkManagerDialog(QtGui.QDialog):

    def __init__(self, model, parent=None):
        super(BookmarkManagerDialog, self).__init__(parent)
        self.uiBookmarkManagerDialog = ui_bookmark_manager_dialog.Ui_Bookmark_Dialog()
        self.uiBookmarkManagerDialog.setupUi(self)

        self.model = model

        self.table = self.uiBookmarkManagerDialog.bookmark_table
        self._update_table_content()

        self.uiBookmarkManagerDialog.button_selection.clicked.connect(self._select_all_table_items)
        self.uiBookmarkManagerDialog.button_remove.clicked.connect(self._remove_table_item)

    def _update_table_content(self):

        # bk = bookmarks.Bookmarks()
        # record_list = bk.get_all_records()
        # bk.close()

        record_list = self.model.get_bookmark_list()
        record_list_len = len(record_list)
        self.table.setRowCount(record_list_len)

        for i in range(0, record_list_len):
            self.table.setItem(i, 0, QtGui.QTableWidgetItem(record_list[i][0]))
            self.table.setItem(i, 1, QtGui.QTableWidgetItem(record_list[i][1]))
            self.table.setItem(i, 2, QtGui.QTableWidgetItem(str(record_list[i][2])))

        self.table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)
        self.table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)

    def _remove_table_item(self):
        selected_items = self.table.selectedItems()
        selected_items_len = len(selected_items)
        selected_items_i = selected_items_len/3
        selected_items_f = selected_items_len - selected_items_i

        # bk = bookmarks.Bookmarks()
        paths = []

        for i in range(selected_items_i, selected_items_f):
            path = selected_items[i].text()
            paths.append(path)
            # bk.delete_bookmark(path)
            self.table.removeRow(selected_items[i].row())

        self.model.remove_bookmarks(paths)

        # bk.close()

    def _select_all_table_items(self):
        self.table.setRangeSelected(QtGui.QTableWidgetSelectionRange(0, 0, self.table.rowCount()-1, 2), True)

    # def show(self):
    #     super(BookmarkManagerDialog, self).show()

