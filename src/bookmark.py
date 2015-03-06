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

db = SqliteDatabase('bookmark.db', threadlocals=True)


class BookmarkBaseModel(Model):
    class Meta:
        database = db


class Bookmark(BookmarkBaseModel):
    comic_id = PrimaryKeyField(unique=True, index=True)
    comic_path = CharField(unique=True)
    comic_name = CharField(default='')
    comic_page = IntegerField(default=0)
    page_data = BlobField(null=True, default=None)


class BookmarkManager(BookmarkBaseModel):

    @staticmethod
    def connect():
        db.connect()
        try:
            db.create_tables([Bookmark], safe=True)
            print "[INFO] Table 'Bookmark' create/updates sucessfully!"
        except OperationalError:
            print "[ERROR] Error to create table 'Bookmark'!"

    @staticmethod
    def close():
        db.close()
        print '[INFO] Bookmark database closed.'

    @staticmethod
    def add_bookmark(name, path, page, data):

        try:
            q = Bookmark.insert(comic_name=name, comic_path=path,
                                comic_page=page, page_data=data)
            q.execute()
            print '[INFO] Bookmark %s inserted.' % name
        except IntegrityError:
            q = Bookmark.update(comic_page=page).where(
                Bookmark.comic_path == path)
            q.execute()
            print '[INFO] Bookmark updated.'

    @staticmethod
    def remove_bookmark(path):

        try:
            q = Bookmark.delete().where(Bookmark.comic_path == path)
            q.execute()
            print '[INFO] Bookmark deleted.'
        except IntegrityError:
            print '[ERROR] Bookmark not find.'

    @staticmethod
    def get_bookmarks(rows_number):

        bk_list = []

        try:
            for q in Bookmark.select().order_by(
                    Bookmark.comic_id.desc()).limit(rows_number):
                print q.comic_name
                bk_list.append(q)
            print '[INFO] Bookmark deleted.'
        except IntegrityError:
            print '[ERROR] Bookmark not find.'

        return bk_list


