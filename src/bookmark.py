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

import peewee

db = peewee.SqliteDatabase('bookmark.db', threadlocals=True)


class BookmarkBaseModel(peewee.Model):
    class Meta:
        database = db


class Bookmark(BookmarkBaseModel):
    comic_id = peewee.PrimaryKeyField(unique=True, index=True)
    comic_path = peewee.CharField(unique=True)
    comic_name = peewee.CharField(default='')
    comic_page = peewee.IntegerField(default=0)
    page_data = peewee.BlobField(null=True, default=None)


class BookmarkManager(BookmarkBaseModel):

    @staticmethod
    def before_request():
        db.connect()
        try:
            db.create_tables([Bookmark], safe=True)
            print "[INFO] Table 'Bookmark' create/updates sucessfully!"
        except peewee.OperationalError:
            print "[ERROR] Error to create table 'Bookmark'!"

    @staticmethod
    def after_request():
        db.close()

    @staticmethod
    def add_bookmark(name, path, page):

        try:
            q = Bookmark.insert(comic_name=name, comic_path=path,
                                comic_page=page, page_data=None)
            q.execute()
            print '[INFO] Bookmark inserted.'
        except peewee.IntegrityError:
            q = Bookmark.update(comic_page=page).where(Bookmark.comic_path == path)
            q.execute()
            print '[INFO] Bookmark updated.'

    @staticmethod
    def remove_bookmark(path):

        try:
            q = Bookmark.delete().where(Bookmark.comic_path == path)
            q.execute()
            print '[INFO] Bookmark deleted.'
        except peewee.IntegrityError:
            print '[ERROR] Bookmark not find.'
