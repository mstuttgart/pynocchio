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

from data_base_manager import DataBaseManager


class Bookmarks(object):
    BOOKMARK_FILE_NAME = "bookmarks.db"

    def __init__(self):
        self.db = DataBaseManager(self.BOOKMARK_FILE_NAME)
        self.db.create_table('Bookmarks', '(Id INTEGER PRIMARY KEY NOT NULL, '
                                          'Path TEXT SECUNDARY KEY NOT NULL, '
                                          'Name TEXT, Page INTEGER)')

    def add_bookmark(self, path, name, page):
        ret = self.db.find('Bookmarks', 'Path', path)

        if ret:
            sql = "UPDATE Bookmarks SET Page=%d WHERE Path='%s';" % (page,
                                                                     path)
        else:
            sql = "INSERT OR IGNORE INTO Bookmarks (Path, Name, Page) " \
                  "VALUES ('%s', '%s', %d);" % (path, name, page)

        self.db.execute(sql)

    def delete_bookmark(self, path):
        sql = "DELETE FROM Bookmarks WHERE Path='%s';" % path
        self.db.execute(sql)

    def find_bookmark(self, path):
        sql = "SELECT Path, Name, Page " \
              "FROM Bookmarks WHERE Path = '%s';" % path
        r = self.db.execute(sql)
        return r.fetchone()

    def _get_last_bookmarks(self, num):
        sql = "SELECT Name, Path, Page FROM " \
              "BOOKMARKS ORDER BY Id DESC LIMIT 5;"
        return self.db.execute(sql).fetchmany(num)

    def _get_all_records(self):
        sql = "SELECT Name, Path, Page FROM BOOKMARKS;"
        return self.db.execute(sql).fetchall()

    def get_records(self, num=0):
        if num == 0:
            book_list = self._get_all_records()
        else:
            book_list = self._get_last_bookmarks(num)
        return book_list

    def close(self):
        self.db.close_db()
