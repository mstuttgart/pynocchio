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
from lxml import html
import requests


class BaseParser(object):

    def __init__(self):
        self.comics_urls = {}
        self.chapter_urls = {}
        self.pages_urls = []
        self.image_urls = []

    def updated_comic_list(self):
        pass

    def update_chapters_list(self, comic_name):
        pass

    def update_pages_url(self, chapter_name):
        pass

    def update_image_url(self, page_url):
        pass


