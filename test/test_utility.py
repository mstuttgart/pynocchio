# -*- coding: utf-8 -*-


from unittest import TestCase

from pynocchio.utility import Utility


class TestUtility(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.obj = Utility()

    def test_get_file_extension(self):
        self.assertEqual(Utility.get_file_extension('myfile.zip'), 'zip')
        self.assertEqual(Utility.get_file_extension('myfile'), '')

    def test_get_dir_name(self):
        self.assertEqual(Utility.get_dir_name('/home/user/myfile.zip'),
                         '/home/user')
        self.assertEqual(Utility.get_dir_name('myfile'), '')

    def test_get_base_name(self):
        self.assertEqual(Utility.get_base_name('/home/user/myfile.zip'),
                         'myfile.zip')
        self.assertEqual(Utility.get_base_name('/home/user/myfile'), 'myfile')

    def test_get_parent_path(self):
        self.assertEqual(Utility.get_parent_path('/home/user/myfile.zip'),
                         '/home')
        self.assertEqual(Utility.get_parent_path('/home/user/myfile'), '/home')

    def test_join_path(self):
        self.assertEqual(Utility.join_path('/home', 'user', 'myfile.zip'),
                         '/home/user/myfile.zip')
        self.assertEqual(Utility.join_path('/home', 'user', 'myfile'),
                         '/home/user/myfile')

    def test_path_exist(self):
        self.assertTrue(Utility.path_exist('/home'))
        self.assertFalse(Utility.path_exist('/foo'))

    def test_file_exist(self):
        self.assertTrue(Utility.file_exist('LICENSE'))
        self.assertFalse(Utility.file_exist('foo.py'))

    def test_is_dir(self):
        self.assertTrue(Utility.is_dir('/home'))
        self.assertFalse(Utility.is_dir('LICENSE'))

    def test_convert_string_to_boolean(self):
        self.assertTrue(Utility.convert_string_to_boolean('True'))
        self.assertFalse(Utility.convert_string_to_boolean('False'))
        self.assertRaises(ValueError, Utility.convert_string_to_boolean,
                          'true')
