# -*- coding: UTF-8 -*-


class Page(object):
    def __init__(self, data, title, number):
        super(Page, self).__init__()
        self.data = data
        self.title = title
        self.number = number
