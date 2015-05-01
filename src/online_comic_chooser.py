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

        # self.addItems(self.tree_widget.invisibleRootItem())
        # self.tree_widget.itemDoubleClicked.connect(self.handleChanged)

        self.host_list_widget.itemClicked.connect(self.item_click)

    def item_click(self, item):
        print item, str(item.text())
        self.load_mangas()



    def addItems(self, parent):
        column = 0
        # clients_item = self.addParent(
        #     parent, column, 'MangaPanda', 'MangaPanda', 'http://www.mangapanda.com/alphabetical')
        # self.load_mangas()

    def addParent(self, parent, column, title, data, status_tip):
        item = QtGui.QTreeWidgetItem(parent, title)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        item.setStatusTip(column, status_tip)
        return item

    def addChild(self, parent, column, title, data, status_tip):
        item = QtGui.CustomQTreeWidgetItem(parent, title)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setStatusTip(column, status_tip)
        return item
    #
    # def handleChanged(self, item, column):
    #     print 'double clicked'
    #
    #     if item.nivel() == CustomQTreeWidgetItem.SITE:
    #         print 'SITE'
    #         self.load_mangas(item, column)
    #     elif item.nivel() == CustomQTreeWidgetItem.COMIC:
    #         self.load_comic(item, column)
    #         print 'COMIC'
    #     elif item.nivel() == CustomQTreeWidgetItem.CHAPTER:
    #         self.load_chapter(item, column)
    #         print 'CHAPTER'
    #     else:
    #         print 'NADA'
    #

    def load_mangas(self):

        from lxml import html
        import requests

        url = 'http://www.mangapanda.com/alphabetical'
        page = requests.get(url)
        tree = html.fromstring(page.text)

        for option in tree.xpath("//div[@class='series_alpha']/ul[@class='series_alpha']/li/a"):
            url = 'http://www.mangapanda.com' + option.get('href')
            self.addParent(self.tree_widget.invisibleRootItem(), 0,
                           option.text.encode("utf-8"),
                           option.text.encode("utf-8"), url)

    def load_comic(self):
        from lxml import html
        import requests

        page = requests.get('http://www.mangapanda.com/alphabetical')
        tree = html.fromstring(page.text)

        for option in tree.xpath("//table[@id='listing']/tr/td/a"):
            self.addParent(self.tree_widget.invisibleRootItem(), 0,
                           option.text.encode("utf-8"),
                           option.text.encode("utf-8"),
                           'http://www.mangapanda.com' + option.get('href'))
            print 'eita'
    #
    # def load_chapter(self, item, column):
    #     from lxml import html
    #     import requests
    #
    #     url = item.statusTip(column)
    #     page = requests.get(url)
    #     tree = html.fromstring(page.text)
    #
    #     for option in tree.xpath("//table[@id='listing']/tr/td/a"):
    #         self.addChild(
    #             item, column, option.text.encode(
    #                 "utf-8"), option.text.encode("utf-8"),
    #             'http://www.mangapanda.com' + option.get('href'))
    #







    #     self.parser = None
    #
    #     self.host_combo_box.addItem('MangaPanda')
    #     self.host_combo_box.addItem('MangaHere')
    #     self.host_combo_box.addItem('MangaFox')
    #     self.host_combo_box.addItem('Potato')
    #     self.host_combo_box.addItem('HQBR')
    #
    #     self.host_combo_box.activated[str].connect(self.on_activat_host)
    #     self.comic_combo_box.activated[str].connect(self.on_activat_comic)
    #
    # def on_activat_host(self, host_name):
    #     self.parser = ParserFactory.create_loader(str(host_name))
    #
    #     if self.parser is not None:
    #         self.comic_combo_box.clear()
    #         self.chapter_combo_box.clear()
    #
    #         self.comic_combo_box.setEnabled(True)
    #         comics_names = self.parser.updated_comic_list()
    #
    #         for name in comics_names:
    #             print name
    #             self.comic_combo_box.addItem(name)
    #
    # def on_activat_comic(self, comic_name):
    #     print comic_name
    #     if self.parser is not None:
    #         self.chapter_combo_box.clear()
    #         self.chapter_combo_box.setEnabled(True)
    #         chapter_names = self.parser.update_chapters_list(str(comic_name))
    #
    #         for name in chapter_names:
    #             self.chapter_combo_box.addItem(name)
