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
from unittest import mock

from pynocchio.comic_path_filter import ComicPathFilter
from pynocchio.exception import NoDataFindException


class TestComicPathFilter(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.obj = ComicPathFilter(["*.cbr", "*.cbz", "*.rar", "*.zip",
                                    "*.tar", "*.cbt"])

    def test_parse(self):
        with mock.patch('glob.glob1') as mock_glob:
            mock_glob.return_value = ['comic_1.cbr', 'abc.cbr']

            self.obj = ComicPathFilter(['*.cbr'])
            self.obj.parse('.')

            self.assertListEqual(self.obj.file_list,
                                 ['abc.cbr', 'comic_1.cbr'])

            mock_glob.return_value = []

            self.obj = ComicPathFilter(['*.zip'])
            self.obj.parse('.')
            self.assertListEqual(self.obj.file_list, [])

    def test_is_first_comic(self):
        with mock.patch('glob.glob1') as mock_glob:
            mock_glob.return_value = ['comic_3.cbr', 'comic_1.cbr', 'abc.cbr']

            self.obj = ComicPathFilter(['*.cbr'])
            self.obj.parse('.')

            self.assertTrue(self.obj.is_first_comic('abc.cbr'))
            self.assertFalse(self.obj.is_first_comic('comic_3.cbr'))

            self.obj.file_list = []

            self.assertRaises(NoDataFindException, self.obj.is_first_comic,
                              'co.cbr')

    def test_is_last_comic(self):
        with mock.patch('glob.glob1') as mock_glob:
            mock_glob.return_value = ['comic_3.cbr', 'comic_1.cbr', 'abc.cbr']

            self.obj = ComicPathFilter(['*.cbr'])
            self.obj.parse('.')

            self.assertFalse(self.obj.is_last_comic('abc.cbr'))
            self.assertTrue(self.obj.is_last_comic('comic_3.cbr'))

            self.obj.file_list = []

            self.assertRaises(NoDataFindException, self.obj.is_last_comic,
                              'co.cbr')

    def test_get_previous_comic(self):
        with mock.patch('glob.glob1') as mock_glob:
            mock_glob.return_value = ['comic_3.cbr', 'comic_1.cbr', 'abc.cbr']

            self.obj = ComicPathFilter(['*.cbr'])
            self.obj.parse('pynocchio/comics/')

            previous_comics = self.obj.get_previous_comic('comic_1.cbr')
            self.assertEqual('pynocchio/comics/' + 'abc.cbr', previous_comics)

            self.assertRaises(NoDataFindException, self.obj.get_previous_comic,
                              'abc.cbr')

    def test_get_next_comic(self):
        with mock.patch('glob.glob1') as mock_glob:
            mock_glob.return_value = ['comic_3.cbr', 'comic_1.cbr', 'abc.cbr']

            self.obj = ComicPathFilter(['*.cbr'])
            self.obj.parse('pynocchio/comics/')

            next_comics = self.obj.get_next_comic('comic_1.cbr')
            self.assertEqual('pynocchio/comics/' + 'comic_3.cbr', next_comics)

            self.assertRaises(NoDataFindException, self.obj.get_next_comic,
                              'comic_3.cbr')
