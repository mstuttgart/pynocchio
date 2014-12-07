# -*- coding:utf-8 -*

import sqlite3


class SQLiteBookmarks(object):

    def __init__(self):
        super(SQLiteBookmarks, self).__init__()

    @staticmethod
    def _verify_table_exist(conn):
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='BOOKMARK'")

        if cursor.rowcount > 0:
            return True

        return False

    @staticmethod
    def add_bookmark(filename, path, page):

        conn = sqlite3.connect('bookmarks.db')

        if SQLiteBookmarks._verify_table_exist(conn) is not True:
            conn.execute('''CREATE TABLE BOOKMARK
                   (PATH TEXT PRIMARY KEY     NOT NULL,
                   NAME           TEXT     NOT NULL,
                   PAGE           INT);''')

        conn.execute("INSERT INTO BOOKMARK (PATH,NAME,PAGE) \
        VALUES (path, filename, page)")

        conn.commit()
        print "Records created successfully";
        conn.close()





