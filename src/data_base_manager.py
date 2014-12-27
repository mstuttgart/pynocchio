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

        except sqlite3.Error, err:
            print("Error: %s to open %s!" % err, db_name)

    def create_table(self, name, tuple_columns):
        sql = "CREATE TABLE IF NOT EXISTS %s %s;" % (name, tuple_columns)
        self.conn.execute(sql)

    def execute(self, sql):
        if self.conn:
            self.conn.execute(sql)
            self.conn.commit()

    def find(self, table_name, column, value):

        if self.conn:
            sql = "SELECT * FROM %s WHERE %s = '%s';" % (table_name, column, value)
            r = self.conn.execute(sql)
            return r.fetchone()

        return False

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Connection closed!")
