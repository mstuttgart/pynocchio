# -*- coding:utf-8 -*

import sqlite3


class SQLiteBookmarks(object):

    def __init__(self):
        super(SQLiteBookmarks, self).__init__()

    # @staticmethod
    # def _verify_table_exist(conn):
    #     cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='BOOKMARK'")
    #
    #     if cursor is None:
    #         return True
    #
    #     return False

    @staticmethod
    def add_bookmark(filename, path, page):

        conn = sqlite3.connect('bookmarks.db')

        sql = "CREATE TABLE IF NOT EXISTS BOOKMARK (PATH TEXT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PAGE INTEGER);"
        conn.execute(sql)
        conn.execute("INSERT INTO BOOKMARK VALUES ('%s', '%s', %d)" % (path, filename, page))

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




