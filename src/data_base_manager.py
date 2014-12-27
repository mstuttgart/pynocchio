import sqlite3


class DataBaseManager(object):

    def __init__(self, db_name):

        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()

            print("Database:", db_name)

            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)

        except sqlite3.Error:
            print("Error to open %s!" % db_name)

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def insert(self, sql_command):
        self.conn.execute(sql_command)
        self.conn.commit()

    def delete(self, sql_command):
        self.conn.execute(sql_command)
        self.conn.commit()

    def find(self, sql_command):
        r = self.conn.execute(sql_command)
        return r.fetchone()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Connection closed!")
