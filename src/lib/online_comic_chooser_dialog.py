# -*- coding: utf-8 -*-
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
from threading import Thread

from parser_factory import ParserFactory
from utility import Utility

root_dir = Utility.get_parent_path(__file__)

OnlineComicChooserForm, OnlineComicChooserBase = \
    uic.loadUiType(Utility.join_path(root_dir, 'gui', 'online_comic_chooser_dialog.ui'))


class OnlineComicChooserDialog(OnlineComicChooserForm, OnlineComicChooserBase):

    def __init__(self, parent=None):
        super(OnlineComicChooserDialog, self).__init__(parent)
        self.setupUi(self)

        self.parser = None
        self.url_comic_choose = None
        self.th = Thread(target=self._load_comics)
        self.tree_widget.itemDoubleClicked.connect(self._handle_changed)
        self.host_list_widget.itemClicked.connect(self.item_click)

    def item_click(self, item):
        print item, str(item.text())
        self.parser = ParserFactory.create_loader(str(item.text()))

        if not self.th.isAlive():
            self.th.start()
        # self._load_comics()

    def _add_parent(self, parent, column, title, data, status_tip):
        item = QtGui.QTreeWidgetItem(parent, title)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        item.setStatusTip(column, status_tip)
        item.setIcon(0, QtGui.QIcon(
            ':icons/elementary3-icon-theme/actions/48/dialog-apply.svg'))

    def _add_child(self, parent, column, title, data, status_tip):
        item = QtGui.QTreeWidgetItem(parent, title)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setStatusTip(column, status_tip)

    def _handle_changed(self, item, column):
        if item.parent() is None:
            self._load_chapter(item, column)

    def _load_comics(self):
        for name, url in self.parser.updated_comic_list().items():
            self._add_parent(
                self.tree_widget.invisibleRootItem(), 0, name, name, url)

    def _load_chapter(self, item, column):
        chapter_names = self.parser.update_chapters_list(str(item.text(column)))

        for name, url in chapter_names.items():
            self._add_child(item, column, name, name, url)

    def close(self):
        self.url_comic_choose = None
        super(OnlineComicChooserDialog, self).close()

