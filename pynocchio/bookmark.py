# -*- coding: utf-8 -*-

import peewee

from .utility import Utility
from .settings_manager import SettingsManager


# get settings path. In Linux is .config/Pynocchio
def get_settings_path():
    path = Utility.get_dir_name(SettingsManager().settings.fileName())
    return path + '/bookmark.db'

db = peewee.SqliteDatabase(get_settings_path())


class BookmarkBaseModel(peewee.Model):
    class Meta(object):
        database = db


class Bookmark(BookmarkBaseModel):
    comic_id = peewee.PrimaryKeyField(unique=True, index=True)
    comic_path = peewee.CharField(unique=True)
    comic_name = peewee.CharField(default='')
    comic_page = peewee.IntegerField(default=0)
    page_data = peewee.BlobField(null=True, default=None)


class TemporaryBookmark(Bookmark):
    pass
