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
    from peewee import IntegerField, CharField, Model, OperationalError, \
        PrimaryKeyField, BlobField, SqliteDatabase, IntegrityError
except ImportError, err:
    print 'rarfile module not installed.\n' \
          'Please install it using: sudo pip install peewee\n'
    import sys
    sys.exit(err)

db = SqliteDatabase('bookmark.db')


class BookmarkBaseModel(Model):
    class Meta:
        database = db


class Bookmark(BookmarkBaseModel):
    comic_id = PrimaryKeyField(unique=True, index=True)
    comic_path = CharField(unique=True)
    comic_name = CharField(default='')
    comic_page = IntegerField(default=0)
    page_data = BlobField(null=True, default=None)
