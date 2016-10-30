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

from pynocchio.core.comic import Comic
from pynocchio.core.page import Page


class TestComic(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.obj = Comic('comic_test', 'comic_dir')
        self.page = Page(None, 'page_title_1', 1)

    def test_add_page(self):
        self.assertNotIn(self.page, self.obj.pages)
        self.obj.add_page(self.page)
        self.assertIn(self.page, self.obj.pages)

    def test_remove_page(self):
        self.obj.add_page(self.page)
        self.obj.remove_page(self.page)
        self.assertNotIn(self.page, self.obj.pages)

    def test_get_current_page(self):
        self.obj.pages = []
        self.obj.add_page(self.page)
        self.assertEqual(self.page, self.obj.get_current_page())

    def test_get_current_page_title(self):
        self.obj.pages = []
        self.obj.add_page(self.page)
        self.assertEqual(self.page.title, self.obj.get_current_page_title())

    def test_get_current_page_number(self):
        self.obj.pages = []
        self.obj.add_page(self.page)
        self.assertEqual(self.page.number, self.obj.get_current_page_number())

    def test_go_next_page(self):
        self.obj.pages = []
        self.obj.add_page(self.page)

        self.obj.go_next_page()
        self.assertEqual(0, self.obj.current_page_index)

        self.obj.add_page(Page(None, 'page_title_2', 2))
        self.obj.go_next_page()
        self.assertEqual(1, self.obj.current_page_index)

    def test_go_previous_page(self):
        self.obj.pages = []

        self.obj.add_page(self.page)
        self.obj.go_previous_page()
        self.assertEqual(0, self.obj.current_page_index)

        self.obj.add_page(Page(None, 'page_title_2', 2))
        self.obj.go_next_page()

        self.obj.go_previous_page()
        self.assertEqual(0, self.obj.current_page_index)

    def test_go_first_page(self):
        self.obj.current_page_index = 10
        self.obj.go_first_page()
        self.assertEqual(self.obj.current_page_index, 0)

    def test_go_last_page(self):
        self.obj.pages = []
        self.obj.add_page(self.page)
        self.obj.add_page(Page(None, 'page_title_2', 2))

        self.assertEqual(0, self.obj.current_page_index)
        self.obj.go_last_page()
        self.assertEqual(self.obj.current_page_index, len(self.obj.pages) - 1)

    def test_set_current_page_index(self):
        self.obj.pages = []
        self.obj.add_page(self.page)
        self.obj.add_page(Page(None, 'page_title_2', 2))

        self.obj.set_current_page_index(3)
        self.assertNotEqual(self.obj.current_page_index, 3)

        self.obj.set_current_page_index(1)
        self.assertEqual(self.obj.current_page_index, 1)

    def test_get_number_of_pages(self):
        self.obj.pages = []
        self.obj.add_page(self.page)
        self.obj.add_page(Page(None, 'page_title_2', 2))

        self.assertEqual(self.obj.get_number_of_pages(), 2)

    def test_get_path(self):
        self.assertEqual(self.obj.directory + '/' + self.obj.name,
                         self.obj.get_path())
