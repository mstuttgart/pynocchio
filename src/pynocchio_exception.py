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


class PynocchioBaseException(Exception):
    def __init__(self, **kwargs):
        if 'msg' in kwargs:
            self.msg = kwargs['msg']
        self.msg = self.msg.format(**kwargs)


class OpenComicFileException(PynocchioBaseException):
    def __init__(self, **kwargs):
        if 'comic_name' in kwargs:
            self.msg = "Error to open %s comic file" % kwargs['comic_name']
        super(OpenComicFileException, self).__init__(**kwargs)

