# -*- coding:utf-8 -*

import sqlite3


class SQLiteBookmarks(object):

    BOOKMARK_FILE_NAME = "bookmarks.db"

    def __init__(self):
        super(SQLiteBookmarks, self).__init__()

    def add_bookmark(self, filename, path, page):

        conn = sqlite3.connect(self.BOOKMARK_FILE_NAME)

        sql = "CREATE TABLE IF NOT EXISTS bookmarks (path TEXT PRIMARY KEY NOT NULL, name TEXT NOT NULL, page INTEGER);"
        conn.execute(sql)

        sql = "INSERT OR IGNORE INTO bookmarks VALUES ('%s', '%s', %d)" % (path, filename, page)
        conn.execute(sql)

        conn.commit()
        print "Records created successfully"
        conn.close()

    def delete_bookmark(self, path):

        conn = sqlite3.connect(self.BOOKMARK_FILE_NAME)

        sql = "CREATE TABLE IF NOT EXISTS bookmarks (path TEXT PRIMARY KEY NOT NULL, name TEXT NOT NULL, page INTEGER);"
        conn.execute(sql)

        sql = "DELETE FROM bookmarks WHERE path='%s'" % path
        conn.execute(sql)

        conn.commit()
        print "Records removed successfully"
        conn.close()




