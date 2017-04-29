# -*- coding: utf-8 -*-

import os


class Utility:

    @staticmethod
    def get_file_extension(file_name):
        return os.path.splitext(file_name)[1][1:]

    @staticmethod
    def get_dir_name(file_path):
        return os.path.dirname(file_path)

    @staticmethod
    def get_base_name(file_path):
        return os.path.basename(file_path)

    @staticmethod
    def get_parent_path(file_path):
        return os.path.split(os.path.abspath(os.path.dirname(file_path)))[0]

    @staticmethod
    def join_path(root_dir, directory, file_name):
        return os.path.join(root_dir, directory, file_name)

    @staticmethod
    def path_exist(file_path):
        return os.path.lexists(file_path)

    @staticmethod
    def file_exist(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def is_dir(file_path):
        return os.path.isdir(file_path)

    @staticmethod
    def is_file(file_name):
        return os.path.isfile(file_name)

    @staticmethod
    def convert_string_to_boolean(string):
        if string == 'True':
            return True
        elif string == 'False':
            return False
        else:
            raise ValueError
