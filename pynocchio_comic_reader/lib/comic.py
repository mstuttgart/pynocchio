# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


class Comic(object):

    def __init__(self, name, directory, initial_page=0):
        super(Comic, self).__init__()
        self.name = name
        self.directory = directory
        self.current_page_index = initial_page
        self.pages = []

    def add_page(self, obj_page):
        self.pages.append(obj_page)

    def remove_page(self, obj_page):
        self.pages.remove(obj_page)

    def get_current_page(self):
        return self.pages[self.current_page_index]

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
        if idx in xrange(self.get_number_of_pages()):
            self.current_page_index = idx

    def get_number_of_pages(self):
        return len(self.pages)

    def get_path(self):
        return self.directory + '/' + self.name
