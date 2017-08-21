# -*- coding: utf-8 -*-

import os
import tarfile
import random
import sys

from PyQt5 import QtGui, QtWidgets

from unittest import TestCase
from unittest import mock

from pynocchio.comic_file_loader_tar import ComicTarLoader, is_tarfile
from pynocchio.utility import get_file_extension
from pynocchio.utility import IMAGE_FILE_FORMATS
from pynocchio.exception import NoDataFindException


class TestComicTarLoader(TestCase):
    """ This class load Tar compact files.
    """
    def setUp(self):
        self.loader = ComicTarLoader()
        self.comic_name = 'no_existing_comic.cbt'

        self.files = [
            'text_file_01.txt',
        ]

        # Create .txt file
        with open('text_file_01.txt', 'w') as f:
            f.write('test')

    def test_is_tarfile(self):
        """Test is_tarfile function
        """
        with mock.patch('tarfile.is_tarfile') as mock_tar:
            mock_tar.return_value = True
            self.assertTrue(is_tarfile, True)

        with mock.patch('tarfile.is_tarfile') as mock_tar:
            mock_tar.return_value = False
            self.assertTrue(is_tarfile, False)

    def test_load_supported_file_format(self):
        """Test load method from ComicTarLoader class. Load only image files.
        """

        app = QtWidgets.QApplication(sys.argv)

        # Create image file name with the supported PyQT5 image formats
        for idx, ext in enumerate(['.png', '.jpg']):
            img_name = '%d-image-file%s' % (idx, ext)
            QtGui.QPixmap(500, 500).save(img_name)
            self.files.append(img_name)

        # Shuffle files to simulate sorted when loaded them
        random.shuffle(self.files)

        # First, we 'create' the comic.cbt file
        with tarfile.open(self.comic_name, 'w') as tf:
            for f in self.files:
                tf.add(f)

        # Verify if data is empty
        self.assertListEqual(self.loader.data, [])

        # Call load method
        self.loader.load(self.comic_name)

        # The data list not is empty. All images files were loaded
        self.assertTrue(self.loader.data)

        # The data list must be sorted in alphabetical order
        # then we sort this list to make easy compare
        self.files.sort()

        self.files.remove('text_file_01.txt')

        # The files list must be same amount of pages
        self.assertEqual(len(self.loader.data), len(self.files))

        # Compare loaded file with files in self.files
        for idx, page in enumerate(self.loader.data):
            # Verify with exist data
            self.assertTrue(page.data)

            # Verify page title
            self.assertEqual(page.title, os.path.join(self.files[idx]))

            # Verify if all loaded image is support format file
            self.assertIn(get_file_extension(page.title),
                          IMAGE_FILE_FORMATS)

            # Verify page number
            self.assertEqual(page.number, idx + 1)

        # Remove .cbt and .txt file
        os.remove(self.comic_name)
        os.remove('text_file_01.txt')

        # Remove all temp files
        for f in self.files:
            os.remove(f)

    def test_load_not_supported_file_format(self):
        """Test load method from ComicTarLoader class. The load method only
         load image file.
        """

        # First, we 'create' the comic.cbt file and add txt file in it
        with tarfile.open(self.comic_name, 'w') as tf:
            tf.add('text_file_01.txt')

        # The data list is empty
        self.assertListEqual(self.loader.data, [])

        # No image to load, then loader raise a exception
        with self.assertRaises(NoDataFindException):
            self.loader.load(self.comic_name)

        # Remove.cbt comic
        os.remove(self.comic_name)

        # Remove.txt file
        os.remove('text_file_01.txt')
