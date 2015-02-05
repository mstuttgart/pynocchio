# -*- coding:utf-8 -*-
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

        if self.conn:
            self.conn.execute(sql)

    def execute(self, sql):
        if self.conn:
            r = self.conn.execute(sql)
            self.conn.commit()
            return r

        return None

    def find(self, table_name, column, value):
        if self.conn:
            sql = "SELECT * FROM %s WHERE %s = '%s';" % (
            table_name, column, value)
            r = self.conn.execute(sql)
            return r.fetchone()

        return False

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Connection closed!")
