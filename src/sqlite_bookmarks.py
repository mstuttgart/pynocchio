# -*- coding:utf-8 -*

import sqlite3


class SQLiteBookmarks(object):

    BOOKMARK_FILE_NAME = "bookmarks.db"

    def __init__(self):
        super(SQLiteBookmarks, self).__init__()
        self.conn = sqlite3.connect(self.BOOKMARK_FILE_NAME)

        sql = "CREATE TABLE IF NOT EXISTS Bookmarks (Path TEXT PRIMARY KEY NOT NULL, Name TEXT, Page INTEGER);"
        self.conn.execute(sql)

    def add_bookmark(self, path, name, page):

        # ret = self._find_bookmark(path)

        if self._find_bookmark(path):
            sql = "UPDATE Bookmarks SET Page=%d WHERE Path='%s';" % (page, path)
        else:
            sql = "INSERT OR IGNORE INTO Bookmarks(Path, Name, Page) VALUES ('%s', '%s', %d);" % (path, name, page)

        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def delete_bookmark(self, path):

        sql = "DELETE FROM Bookmarks WHERE Path='%s';" % path

        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def _find_bookmark(self, path):
        r = self.conn.execute('SELECT * FROM Bookmarks WHERE Path = ?', (path,))
        return r.fetchone()

    def get_rows(self):
        return self.conn.cursor().fetchall()

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")



