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

from PySide import QtGui, QtCore

from progress_dialog_ui import Ui_QProgressDialog


class QProgressBarDialog(QtGui.QDialog):

    def __init__(self, model, parent=None):
        super(QProgressBarDialog, self).__init__(parent)

        self.ui = Ui_QProgressDialog()
        self.ui.setupUi(self)
        model.load_progress.connect(self.set_progressbar_value)
        model.load_done.connect(self.close)
        QtGui.QApplication.processEvents()

    def set_progressbar_value(self, n):
        print 'tetet', n
        self.ui.progress_bar.setValue(n)

