# -*- coding: UTF-8 -*-

import collections


class Comic(object):

    Pages = collections.namedtuple('Page', 'data title')

    def __init__(self, name, path, pages, titles):
        super(Comic, self).__init__()

        self.name = name
        self.path = path
        self.current_page_index = 0
        self.page_data = self.Pages(pages, titles)

    def get_current_page(self):
        if self.page_data is not None:
            return self.page_data.data[self.current_page_index]
        return None

    def get_current_page_title(self):
        if self.page_data is not None:
            return self.page_data.title[self.current_page_index]
        return None

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
