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


class OnlineComicChooser(OnlineComicChooserForm, OnlineComicChooserBase):

    def __init__(self, parent=None):
        super(OnlineComicChooser, self).__init__(parent)
        self.setupUi(self)

        self.parser = None

        self.host_combo_box.addItem('MangaPanda')
        self.host_combo_box.addItem('MangaHere')
        self.host_combo_box.addItem('MangaFox')
        self.host_combo_box.addItem('Potato')
        self.host_combo_box.addItem('HQBR')

        self.host_combo_box.activated[str].connect(self.on_activat_host)
        self.comic_combo_box.activated[str].connect(self.on_activat_comic)

    def on_activat_host(self, host_name):
        self.parser = ParserFactory.create_loader(str(host_name))

        if self.parser is not None:
            self.comic_combo_box.clear()
            self.chapter_combo_box.clear()

            self.comic_combo_box.setEnabled(True)
            comics_names = self.parser.updated_comic_list()

            for name in comics_names:
                print name
                self.comic_combo_box.addItem(name)

    def on_activat_comic(self, comic_name):
        print comic_name
        if self.parser is not None:
            self.chapter_combo_box.clear()
            self.chapter_combo_box.setEnabled(True)
            chapter_names = self.parser.update_chapters_list(str(comic_name))

            for name in chapter_names:
                self.chapter_combo_box.addItem(name)
