# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

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

from peewee import OperationalError, IntegrityError
from .bookmark import Bookmark, TemporaryBookmark, BookmarkBaseModel, db

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


TABLES = {
    False: Bookmark,
    True: TemporaryBookmark,
}


class BookmarkManager(BookmarkBaseModel):

    @staticmethod
    def connect():
        try:
            db.connect()
            db.create_tables([Bookmark, TemporaryBookmark], safe=True)
            logger.info('Table Bookmark and TemporaryBookmark create/updates '
                        'successfully!')
        except OperationalError:
            logger.exception("Error to create table Bookmark!")

    @staticmethod
    def close():
        if not -db.is_closed():
            db.close()
            logger.info('Bookmark database closed.')

    @staticmethod
    def add_bookmark(name, path, page, data=None, table=Bookmark):
        BookmarkManager.connect()
        try:
            q = table.insert(comic_name=name, comic_path=path,
                             comic_page=page, page_data=data)
            q.execute()
            logger.info('%s item inserted.' % table.__class__)
        except IntegrityError:
            q = table.update(comic_page=page, page_data=data).where(
                table.comic_path == path)
            q.execute()
            logger.info('Bookmark updated.')
        BookmarkManager.close()

    @staticmethod
    def remove_bookmark(path, table=Bookmark):
        BookmarkManager.connect()
        try:
            q = table.delete().where(table.comic_path == path)
            q.execute()
            logger.info('Bookmark deleted.')
        except IntegrityError:
            logger.exception('Bookmark not find!')
        BookmarkManager.close()

    @staticmethod
    def get_bookmarks(rows_number, table=Bookmark):
        query = table.select().order_by(table.comic_id.desc()).limit(
            rows_number)
        return list(query)

    @staticmethod
    def get_bookmark_by_path(path, table=Bookmark):
        BookmarkManager.connect()
        bk_list = table.select().where(table.comic_path == path)
        BookmarkManager.close()
        return bk_list[0] if bk_list else None

    @staticmethod
    def is_bookmark(path, table=Bookmark):
        BookmarkManager.connect()
        bk_list = table.select().where(table.comic_path == path)
        BookmarkManager.close()
        return True if bk_list else False
