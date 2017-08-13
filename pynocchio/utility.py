# -*- coding: utf-8 -*-

import os

from PyQt5 import QtGui

IMAGE_FILE_FORMATS = ['.' + str(ext, encoding='utf8') for ext in
                      QtGui.QImageReader.supportedImageFormats()]

COMPACT_FILE_FORMATS = ['.cbr', '.cbz', '.rar', '.zip', '.tar', '.cbt']

SUPPORTED_FILES = IMAGE_FILE_FORMATS + COMPACT_FILE_FORMATS


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]


def get_dir_name(file_path):
    return os.path.dirname(file_path)


def get_base_name(file_path):
    return os.path.basename(file_path)


def get_parent_path(file_path):
    return os.path.split(os.path.abspath(os.path.dirname(file_path)))[0]


def join_path(root_dir, directory, file_name):
    return os.path.join(root_dir, directory, file_name)


def path_exist(file_path):
    return os.path.lexists(file_path)


def file_exist(file_path):
    return os.path.exists(file_path)


def is_dir(file_path):
    return os.path.isdir(file_path)


def is_file(file_name):
    return os.path.isfile(file_name)


def convert_string_to_boolean(string):
    if string == 'True':
        return True
    elif string == 'False':
        return False
    else:
        raise ValueError
