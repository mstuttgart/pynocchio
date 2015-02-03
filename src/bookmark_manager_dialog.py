# -*- coding:utf-8 -*-
from PyQt4 import QtGui, uic

BookmarkManagerDialogForm, BookmarkManagerDialogBase = uic.loadUiType(
    '../view/bookmark_manager_dialog.ui')


class BookmarkManagerDialog(BookmarkManagerDialogForm,
                            BookmarkManagerDialogBase):
    def __init__(self, mdl, parent=None):
        super(BookmarkManagerDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = mdl
        self.table = self.bookmark_table
        self._update_table_content()
        self.item_to_open = False

        self.button_selection.clicked.connect(self._select_all_table_items)
        self.button_remove.clicked.connect(self._remove_table_item)
        self.button_load.clicked.connect(self._get_comic_to_open)

    def _update_table_content(self):
        record_list = self.model.get_bookmark_list()
        record_list_len = len(record_list)
        self.table.setRowCount(record_list_len)

        for i in range(0, record_list_len):
            self.table.setItem(i, 0, QtGui.QTableWidgetItem(record_list[i][0]))
            self.table.setItem(i, 1, QtGui.QTableWidgetItem(record_list[i][1]))
            self.table.setItem(i, 2,
                               QtGui.QTableWidgetItem(str(record_list[i][2])))

        self.table.horizontalHeader().setResizeMode(0,
                                                    QtGui.QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setResizeMode(1,
                                                    QtGui.QHeaderView.Stretch)
        self.table.horizontalHeader().setResizeMode(2,
                                                    QtGui.QHeaderView.ResizeToContents)

    def _remove_table_item(self):
        selected_items = self.table.selectedItems()
        selected_items_len = len(selected_items)
        selected_items_i = selected_items_len / 3
        selected_items_f = selected_items_len - selected_items_i

        paths = []

        for i in range(selected_items_i, selected_items_f):
            path = selected_items[i].text()
            paths.append(path)
            self.table.removeRow(selected_items[i].row())

        self.model.remove_bookmarks(paths)

    def _select_all_table_items(self):
        self.table.setRangeSelected(
            QtGui.QTableWidgetSelectionRange(0, 0, self.table.rowCount() - 1,
                                             2), True)

    def _get_comic_to_open(self):
        items = self.table.selectedItems()
        if items:
            self.item_to_open = items[1].text()
        self.close()



