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

from collections import deque


class RecenteFiles(object):

    def __init__(self, comic_name, comic_path):
        self.comic_name = comic_name
        self.comic_path = comic_path


class RecentFileManager(object):

    def __init__(self, max_items):
        self.recent_files_deque = deque(maxlen=max_items)

    def append_left(self, text, path):
        rf = self._remove_equal_element(path)

        if rf is not None:
            self.recent_files_deque.appendleft(rf)
        else:
            self.recent_files_deque.appendleft(RecenteFiles(text, path))

    def append_right(self, text, path):
        rf = self._remove_equal_element(path)

        if rf is not None:
            self.recent_files_deque.appendleft(rf)
        else:
            self.recent_files_deque.appendleft(RecenteFiles(text, path))

    def _remove_equal_element(self, path):

        for rf in self.recent_files_deque:
                if rf.comic_path == path:
                    self.recent_files_deque.remove(rf)
                    return rf

        return None

    def get(self, index):
        try:
            return self.recent_files_deque[index]
        except IndexError as exp:
            print exp.message
