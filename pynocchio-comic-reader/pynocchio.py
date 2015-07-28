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

try:
    from PyQt4 import QtCore, QtGui
except ImportError, err:
    sys.exit(err)

from src.main_window_controller import MainWindowController


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('pynocchio-comic-reader')
    app.setApplicationVersion('1.0.0')

    qm = QtCore.QLocale.system().name()

    if qm != 'en_US':
        translator = QtCore.QTranslator()
        try:
            translator.load('locale/qt_%s.qm' % qm)
            app.installTranslator(translator)
        except IOError:
            print 'Translation file qt_%s.qm not find' % qm

    main_window = MainWindowController()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
