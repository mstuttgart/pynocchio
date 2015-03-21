# coding=UTF-8
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

try:
    import peewee
except ImportError, err:
    print 'peewee module not installed.\n' \
          'Please install it using: sudo pip install peewee\n'
    import sys
    sys.exit(err)

db = peewee.SqliteDatabase('recente_files.db')


class RecenteFilesBaseModel(peewee.Model):
    class Meta:
        database = db


class RecenteFiles(RecenteFilesBaseModel):
    comic_id = peewee.PrimaryKeyField(unique=True, index=True)
    comic_path = peewee.CharField(unique=True)
    comic_name = peewee.CharField(default='')
