# -*- coding: utf-8 -*-


from unittest import TestCase

from pynocchio.comic import Comic
from pynocchio.comic import Page


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


class TestPage(TestCase):

    def test__init__(self):
        page = Page(None, 'title', 1)
        self.assertEqual(page.data, None)
        self.assertEqual(page.title, 'title')
        self.assertEqual(page.number, 1)
