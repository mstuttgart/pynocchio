# -*- coding: UTF-8 -*-

from rar_loader import *
from zip_loader import *
import collections


class Comic(object):

    Pages = collections.namedtuple('Page', 'data title')

    def __init__(self):

        object.__init__(self)

        self.name = ''
        self.path = ''
        self.current_page_index = 0
        self.page_data = None

    def load(self, filename):

        if ZipLoader.is_zip_file(filename):
            self._load_content(ZipLoader(), filename)

        elif RarLoader.is_rar_file(filename):
            self._load_content(RarLoader(), filename)

        else:
            print 'File type is not supported!'
            return False

        self.current_page_index = 0

        return True

    def _load_content(self, loader, file_name):
        pages, titles, self.path, self.name = loader.load_file(file_name)
        self.page_data = self.Pages(pages, titles)

    def get_current_page(self):
        return self.page_data.data[self.current_page_index]

    def go_next_page(self):

        range_list = range(0, self.get_number_of_pages() - 1)

        if self.current_page_index in range_list:
            self.current_page_index += 1

    def go_previous_page(self):

        range_list = range(1, self.get_number_of_pages())

        if self.current_page_index in range_list:
            self.current_page_index -= 1

    def go_first_page(self):
        self.current_page_index = 0

    def go_last_page(self):
        self.current_page_index = self.get_number_of_pages() - 1

    def set_current_page_index(self, idx):

        if idx in range(0, self.get_number_of_pages()):
            self.current_page_index = idx

    def get_number_of_pages(self):
        return len(self.page_data.data)

