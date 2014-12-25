# -*- coding:utf-8 -*

import sqlite3


class SQLiteBookmarks(object):

    def __init__(self):
        super(SQLiteBookmarks, self).__init__()

    @staticmethod
    def add_bookmark(filename, path, page):

        conn = sqlite3.connect('bookmarks.db')

        sql = "CREATE TABLE IF NOT EXISTS BOOKMARK (PATH TEXT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PAGE INTEGER);"
        conn.execute(sql)

        sql = "INSERT OR IGNORE INTO BOOKMARK VALUES ('%s', '%s', %d)" % (path, filename, page)
        conn.execute(sql)

        conn.commit()
        print "Records created successfully"
        conn.close()

    @staticmethod
    def delete_bookmark(path, page):

        conn = sqlite3.connect('bookmarks.db')

        sql = "CREATE TABLE IF NOT EXISTS BOOKMARK (PATH TEXT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PAGE INTEGER);"
        conn.execute(sql)

        conn.execute("DELETE FROM BOOKMARK WHERE PATH='%s'" % path)

        conn.commit()
        print "Records created successfully"
        conn.close()




