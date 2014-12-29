# -*- coding:utf-8 -*

import data_base_manager


class Bookmarks(object):

    BOOKMARK_FILE_NAME = "bookmarks.db"
    NUM_BOOKMARK = 5

    def __init__(self):
        self.db = data_base_manager.DataBaseManager(self.BOOKMARK_FILE_NAME)
        self.db.create_table('Bookmarks', '(Id INTEGER PRIMARY KEY NOT NULL, Path TEXT SECUNDARY KEY NOT NULL, Name TEXT, Page INTEGER)')

    def add_bookmark(self, path, name, page):

        ret = self.db.find('Bookmarks', 'Path', path)

        if ret:
            sql = "UPDATE Bookmarks SET Page=%d WHERE Path='%s';" % (page, path)
        else:
            sql = "INSERT OR IGNORE INTO Bookmarks (Path, Name, Page) VALUES ('%s', '%s', %d);" % (path, name, page)

        self.db.execute(sql)

    def delete_bookmark(self, path):
        sql = "DELETE FROM Bookmarks WHERE Path='%s';" % path
        self.db.execute(sql)

    def _find_bookmark(self, path):
        sql = "SELECT * FROM Bookmarks WHERE Path = '%s';" % path
        r = self.db.execute(sql)
        return r.fetchone()

    def get_last_bookmarks(self):
        sql = "SELECT Path, Name FROM BOOKMARKS ORDER BY Id DESC LIMIT 5;"
        return self.db.execute(sql).fetchmany(self.NUM_BOOKMARK)

    def close(self):
        self.db.close_db()


