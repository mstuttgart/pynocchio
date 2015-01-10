# -*- coding: UTF-8 -*-


class Page(object):

    def __init__(self, data, path, number):
        super(Page, self).__init__()
        self.data = data
        self.path = path
        self.number = number
