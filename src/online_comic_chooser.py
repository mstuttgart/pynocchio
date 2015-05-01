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

from parser_factory import ParserFactory

OnlineComicChooserForm, OnlineComicChooserBase = \
    uic.loadUiType('online_comic_chooser.ui')


class CustomQTreeWidgetItem(QtGui.QTreeWidgetItem):

    SITE = 0
    COMIC = 1
    CHAPTER = 2

    def __init__(self, parent, title, nivel):
        super(CustomQTreeWidgetItem, self).__init__(parent, [title])
        self._nivel = nivel

    def set_nivel(self, value):
        self._nivel = value

    def nivel(self):
        return self._nivel


class OnlineComicChooser(OnlineComicChooserForm, OnlineComicChooserBase):

    def __init__(self, parent=None):
        super(OnlineComicChooser, self).__init__(parent)
        self.setupUi(self)

        self.parser = None
        self.tree_widget.itemDoubleClicked.connect(self.handle_changed)
        self.host_list_widget.itemClicked.connect(self.item_click)

    def item_click(self, item):
        print item, str(item.text())
        self.parser = ParserFactory.create_loader(str(item.text()))
        self.load_mangas()

    def add_parent(self, parent, column, title, data, status_tip):
        item = QtGui.QTreeWidgetItem(parent, title)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        item.setStatusTip(column, status_tip)
        item.setIcon(0, QtGui.QIcon(
            ':icons/elementary3-icon-theme/actions/48/dialog-apply.svg'))

        return item

    def add_child(self, parent, column, title, data, status_tip):
        item = QtGui.QTreeWidgetItem(parent, title)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setStatusTip(column, status_tip)
        return item

    def handle_changed(self, item, column):
        if item.parent() is None:
            self.load_chapter(item, column)

    def load_mangas(self):

        for name, url in self.parser.updated_comic_list().items():
            self.add_parent(
                self.tree_widget.invisibleRootItem(), 0, name, name, url)

    def load_chapter(self, item, column):
        chapter_names = self.parser.update_chapters_list(str(item.text(column)))

        for name, url in chapter_names.items():
            self.add_child(item, column, name, name, url)
