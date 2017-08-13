# -*- coding: utf-8 -*-

from unittest import TestCase

from pynocchio.utility import (get_file_extension,
                               get_dir_name,
                               get_base_name,
                               convert_string_to_boolean,
                               is_dir,
                               file_exist,
                               path_exist,
                               get_parent_path,
                               join_path)


class TestUtility(TestCase):

    def setUp(self):
        TestCase.setUp(self)

    def test_get_file_extension(self):
        self.assertEqual(get_file_extension('myfile.zip'), '.zip')
        self.assertEqual(get_file_extension('myfile'), '')

    def test_get_dir_name(self):
        self.assertEqual(get_dir_name('/home/user/myfile.zip'), '/home/user')
        self.assertEqual(get_dir_name('myfile'), '')

    def test_get_base_name(self):
        self.assertEqual(get_base_name('/home/user/myfile.zip'), 'myfile.zip')
        self.assertEqual(get_base_name('/home/user/myfile'), 'myfile')

    def test_get_parent_path(self):
        self.assertEqual(get_parent_path('/home/user/myfile.zip'), '/home')
        self.assertEqual(get_parent_path('/home/user/myfile'), '/home')

    def test_join_path(self):
        self.assertEqual(join_path('/home', 'user', 'myfile.zip'),
                         '/home/user/myfile.zip')
        self.assertEqual(join_path('/home', 'user', 'myfile'),
                         '/home/user/myfile')

    def test_path_exist(self):
        self.assertTrue(path_exist('/home'))
        self.assertFalse(path_exist('/foo'))

    def test_file_exist(self):
        self.assertTrue(file_exist('LICENSE'))
        self.assertFalse(file_exist('foo.py'))

    def test_is_dir(self):
        self.assertTrue(is_dir('/home'))
        self.assertFalse(is_dir('LICENSE'))

    def test_convert_string_to_boolean(self):
        self.assertTrue(convert_string_to_boolean('True'))
        self.assertFalse(convert_string_to_boolean('False'))
        self.assertRaises(ValueError, convert_string_to_boolean, 'true')
