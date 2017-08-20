# -*- coding: utf-8 -*-

import os
import zipfile
import random
import sys

from PyQt5 import QtGui, QtWidgets

from unittest import TestCase
from unittest import mock

from pynocchio.comic_file_loader_zip import ComicZipLoader, is_zipfile
from pynocchio.utility import get_file_extension
from pynocchio.utility import IMAGE_FILE_FORMATS
from pynocchio.exception import NoDataFindException


class TestComicZipLoader(TestCase):
    """ This class load Zip compact files.
    """
    def setUp(self):
        self.loader = ComicZipLoader()
        self.comic_name = 'no_existing_comic.cbz'

        self.files = [
            'text_file_01.txt',
        ]

        # Create .txt file
        with open('text_file_01.txt', 'w') as f:
            f.write('test')

    def test_is_zipfile(self):
        """Test is_zipfile function
        """
        with mock.patch('zipfile.is_zipfile') as mock_zipfile:
            mock_zipfile.return_value = True
            self.assertTrue(is_zipfile(self.comic_name))

        with mock.patch('zipfile.is_zipfile') as mock_zipfile:
            mock_zipfile.return_value = False
            self.assertFalse(is_zipfile('tesste.rar'))

    def test_load_supported_file_format(self):
        """Test load method from ComicZipLoader class. Load only image files.
        """

        app = QtWidgets.QApplication(sys.argv)

        # Create image file name with the supported PyQT5 image formats
        for idx, ext in enumerate(['.png', '.jpg']):
            img_name = '%d-image-file%s' % (idx, ext)
            QtGui.QPixmap(500, 500).save(img_name)
            self.files.append(img_name)

        # Shuffle files to simulate sorted when loaded them
        random.shuffle(self.files)

        # First, we 'create' the comic.cbz file
        with zipfile.ZipFile(self.comic_name, 'w') as zf:
            for f in self.files:
                zf.write(f)

        # Verify if data is empty
        self.assertListEqual(self.loader.data, [])

        # Call load method
        self.loader.load(self.comic_name)

        # The data list not is empty. All images files were loaded
        self.assertTrue(self.loader.data)

        # The data list must be sorted in alphabetical order
        # then we sort this list to make easy compare
        self.files.sort()

        # Remove txt from files list because only image files must be loaded
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
        """Test load method from ComicZipLoader class. The load method only
         load image file.
        """

        with zipfile.ZipFile(self.comic_name, 'w') as zf:
            zf.write('text_file_01.txt')

        # Data list must be empty, because not exist image files in .cbt file
        self.assertListEqual(self.loader.data, [])

        with self.assertRaises(NoDataFindException):
            self.loader.load(self.comic_name)

        os.remove(self.comic_name)
        os.remove('text_file_01.txt')
