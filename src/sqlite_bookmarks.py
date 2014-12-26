# -*- coding:utf-8 -*

import sqlite3


class SQLiteBookmarks(object):

    BOOKMARK_FILE_NAME = "bookmarks.db"

    def __init__(self):
        super(SQLiteBookmarks, self).__init__()
        self.con = sqlite3.connect(self.BOOKMARK_FILE_NAME)

        sql = "CREATE TABLE IF NOT EXISTS Bookmarks (Path TEXT PRIMARY KEY NOT NULL, Name TEXT, Page INTEGER);"
        self.con.execute(sql)

    def add_bookmark(self, path, name, page):

        sql = "INSERT OR IGNORE INTO Bookmarks(Path, Name, Page) VALUES ('%s', '%s', %d);" % (path, name, page)
        self.con.execute(sql)

        self.con.commit()
        print "Records created successfully"
        self.con.close()

    def delete_bookmark(self, path):

        sql = "DELETE FROM Bookmarks WHERE Path='%s';" % path
        self.con.execute(sql)

        self.con.commit()
        print "Records removed successfully"
        self.con.close()




