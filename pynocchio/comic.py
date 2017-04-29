# -*- coding: utf-8 -*-


class Comic:

    FILE = 0
    FOLDER = 1

    def __init__(self, name, directory, comic_type=FILE):
        self.name = name
        self.directory = directory
        self.type = comic_type
        self.pages = []

    def get_number_of_pages(self):
        return len(self.pages)

    def get_path(self):
        return self.directory + '/' + self.name


class Page:

    def __init__(self, data, title, number):
        self.data = data
        self.title = title
        self.number = number
