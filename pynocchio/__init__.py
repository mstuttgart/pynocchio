# -*- coding: utf-8 -*-

from .__version__ import (__title__,  # noqa: F401
                          __description__,
                          __version__,
                          __author__,
                          __author_email__,
                          __maintainer__,
                          __maintainer_email__,
                          __url__,
                          __download_url__,
                          __copyright__,
                          __license__)

from PyQt5 import QtGui

IMAGE_FILE_FORMATS = ['.' + str(ext, encoding='utf8') for ext in
                      QtGui.QImageReader.supportedImageFormats()]

COMPACT_FILE_FORMATS = ['.cbr', '.cbz', '.rar', '.zip', '.tar', '.cbt']

SUPPORTED_FILES = IMAGE_FILE_FORMATS + COMPACT_FILE_FORMATS
