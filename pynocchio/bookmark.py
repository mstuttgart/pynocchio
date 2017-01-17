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
