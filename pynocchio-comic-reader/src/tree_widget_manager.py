# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


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


class TreeWidgetManager(object):

    def __init__(self, tree_widget):
        self.tree_widget = tree_widget

        self.tree_widget.setHeaderHidden(True)
        self.addItems(self.tree_widget.invisibleRootItem())
        self.tree_widget.itemDoubleClicked.connect(self.handleChanged)

    def addItems(self, parent):
        column = 0
        self.addParent(parent, column, 'MangaPanda', 'MangaPanda',
                       'http://www.mangapanda.com/alphabetical')

    def addParent(self, parent, column, title, data, status_tip):
        item = CustomQTreeWidgetItem(parent, title, CustomQTreeWidgetItem.SITE)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        item.setStatusTip(column, status_tip)
        return item

    def addChild(self, parent, column, title, data, status_tip):
        item = CustomQTreeWidgetItem(
            parent, title, CustomQTreeWidgetItem.COMIC)
        item.setData(column, QtCore.Qt.DisplayRole, data)
        item.setStatusTip(column, status_tip)
        return item

    def handleChanged(self, item, column):
        print 'double clicked'

        if item.nivel() == CustomQTreeWidgetItem.SITE:
            print 'SITE'
            self.load_mangas(item, column)
        elif item.nivel() == CustomQTreeWidgetItem.COMIC:
            self.load_comic(item, column)
            print 'COMIC'
        elif item.nivel() == CustomQTreeWidgetItem.CHAPTER:
            self.load_chapter(item, column)
            print 'CHAPTER'
        else:
            print 'NADA'

    def load_mangas(self, item, column):

        from lxml import html
        import requests

        url = item.statusTip(column)
        page = requests.get(url)
        tree = html.fromstring(page.text)

        for option in tree.xpath("//div[@class='series_alpha']/ul[@class='series_alpha']/li/a"):
            url = 'http://www.mangapanda.com' + option.get('href')
            self.addChild(
                item, column,
                option.text.encode("utf-8"),
                option.text.encode("utf-8"), url)

    def load_comic(self, item, column):
        from lxml import html
        import requests

        url = item.statusTip(column)
        page = requests.get(url)
        tree = html.fromstring(page.text)

        for option in tree.xpath("//table[@id='listing']/tr/td/a"):
            self.addChild(
                item, column,
                option.text.encode("utf-8"),
                option.text.encode("utf-8"),
                'http://www.mangapanda.com' + option.get('href'))

    def load_chapter(self, item, column):
        from lxml import html
        import requests

        url = item.statusTip(column)
        page = requests.get(url)
        tree = html.fromstring(page.text)

        for option in tree.xpath("//table[@id='listing']/tr/td/a"):
            self.addChild(
                item, column, option.text.encode(
                    "utf-8"), option.text.encode("utf-8"),
                'http://www.mangapanda.com' + option.get('href'))