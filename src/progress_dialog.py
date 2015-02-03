from PyQt4 import QtGui
from PyQt4 import QtCore


class ProgressDialog(QtGui.QProgressDialog):
    def __init__(self, msg, button, initial_step, final_step, parent=None):
        super(ProgressDialog, self).__init__(msg, button, initial_step,
                                             final_step, parent)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setAutoReset(True)
        self.setAutoClose(True)
        self.resize(350, 50)