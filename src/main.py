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

import sys
from os.path import abspath
from PySide import QtGui, QtCore

from lib.main_window_model import MainWindowModel
from lib.main_window_view import MainWindowView

datadirs = (
        abspath('.'),
        '/usr/share/pynocchio',
        '/usr/local/share/pynocchio',
        QtCore.QDir.homePath() + '/.local/share/pynocchio',
    )

QLocale = QtCore.QLocale
QLibraryInfo = QtCore.QLibraryInfo
QTranslator = QtCore.QTranslator
QFileInfo = QtCore.QFileInfo
QFile = QtCore.QFile


def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName('Pynocchio')
    app.setApplicationName('Pynocchio')
    if hasattr(app, 'setApplicationDisplayName'):
        app.setApplicationDisplayName('Pynocchio')

    translator = QTranslator()
    for path in datadirs:
        if translator.load('pynocchio_' + QLocale.system().name(),
                           path + '/locale'):
            break
    qt_translator = QTranslator()
    qt_translator.load('qt_' + QLocale.system().name(),
                       QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    app.installTranslator(qt_translator)

    model = MainWindowModel()
    view = MainWindowView(model)
    view.show()

    if len(sys.argv) > 1:
        file_name = QFileInfo(sys.argv[1]).canonicalFilePath()
        if QFile.exists(file_name):
            view.open_comics(file_name)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
