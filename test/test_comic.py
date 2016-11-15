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

from unittest import TestCase

from pynocchio.comic import Comic
from pynocchio.page import Page


class TestComic(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.obj = Comic('comic_test', 'comic_dir')
        self.page = Page(None, 'page_title_1', 1)

    def test_get_number_of_pages(self):
        self.obj.pages = []
        self.obj.pages.append(self.page)
        self.obj.pages.append(Page(None, 'page_title_2', 2))

        self.assertEqual(self.obj.get_number_of_pages(), 2)

    def test_get_path(self):
        self.assertEqual(self.obj.directory + '/' + self.obj.name,
                         self.obj.get_path())
