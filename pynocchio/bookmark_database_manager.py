# -*- coding: utf-8 -*-

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
            BookmarkManager.close()
            db.connect()
            db.create_tables([Bookmark, TemporaryBookmark], safe=True)
            logger.info('Table Bookmark and TemporaryBookmark create/updates '
                        'successfully!')
        except OperationalError as exc:
            logger.exception(exc)

    @staticmethod
    def close():
        if not db.is_closed():
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
