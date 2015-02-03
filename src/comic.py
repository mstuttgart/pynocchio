# -*- coding: UTF-8 -*-
import page


class Comic(object):
    def __init__(self, name, directory, initial_page=0):
        super(Comic, self).__init__()
        self.name = name
        self.directory = directory
        self.current_page_index = initial_page
        self.pages = []

    def add_page(self, obj_page):
        if isinstance(obj_page, page.Page):
            self.pages.append(obj_page)

    def remove_page(self, obj_page):
        if isinstance(obj_page, page.Page):
            self.pages.remove(obj_page)

    def get_current_page(self):
        return self.pages[self.current_page_index].data

    def get_current_page_title(self):
        return self.pages[self.current_page_index].title

    def get_current_page_number(self):
        return self.pages[self.current_page_index].number

    def go_next_page(self):
        if self.current_page_index < self.get_number_of_pages() - 1:
            self.current_page_index += 1

    def go_previous_page(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1

    def go_first_page(self):
        self.current_page_index = 0

    def go_last_page(self):
        self.current_page_index = self.get_number_of_pages() - 1

    def set_current_page_index(self, idx):
        if idx in range(0, self.get_number_of_pages()):
            self.current_page_index = idx

    def get_number_of_pages(self):
        return len(self.pages)

    def get_path(self):
        return self.directory + '/' + self.name
