# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


class QWebImageWidget(QWebView):

    BACKGROUND_COLOR_BLACK = 'Black'
    BACKGROUND_COLOR_GRAY = 'Gray'
    BACKGROUND_COLOR_SILVER = 'Silver'
    BACKGROUND_COLOR_WHITE = 'White'
    BACKGROUND_COLOR_Yellow = 'Yellow'
    BACKGROUND_COLOR_LIME = 'Lime'
    BACKGROUND_COLOR_AQUA = 'Aqua'
    BACKGROUND_COLOR_FUCHSIA = 'Fuchsia'
    BACKGROUND_COLOR_RED = 'Red'
    BACKGROUND_COLOR_GREEN = 'Green'
    BACKGROUND_COLOR_BLUE = 'Blue'
    BACKGROUND_COLOR_PURPLE = 'Purple'
    BACKGROUND_COLOR_MARRON = 'Maroon'
    BACKGROUND_COLOR_OLIVE = 'Olive'
    BACKGROUND_COLOR_NAVY = 'Navy'
    BACKGROUND_COLOR_TEAL = 'Teal'

    def __init__(self):
        super(QWebView, self).__init__()
        self.url_image_list = []
        self.current_url_index = 0
        self.image_height = 'image description' 
        self.background_color = QWebImageWidget.BACKGROUND_COLOR_BLACK
        html = '<body bgcolor="%s"></body>' % self.background_color
        self.setHtml(html)

    def load_url(self, url):
        img_aatr = '<img src="%s" alt="%s">' % (url, self.image_height)
        html = '<body bgcolor="%s"><center>%s</center></body>' % (self.background_color, img_aatr)
        self.setHtml(html, QUrl(url))

    def add_image_url(self, url):
        self.url_image_list.append(url)

    def remove_image_url(self, url):
        self.url_image_list.remove(url)

    def reload_page(self):
        self.load_url(self.url_image_list[self.current_url_index])

    def next_url(self):
        if self.current_url_index <= len(self.url_image_list):
            self.current_url_index += 1

    def previous_url(self):
        if self.current_url_index > 0:
            self.current_url_index -= 1

    def set_zoom_factor(self, factor):
        self.setZoomFactor(factor)

    def cler_url_list(self):
        self.url_image_list = []
