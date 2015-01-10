# -*- coding: UTF-8 -*-
from main_window import MainWindow
from PySide import QtCore, QtGui, QtUiTools


def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Pynocchio')
    # QCoreApplication.setApplicationName('Pynocchio')

    # main_window =loadUiWidget("../view/main_window.ui")
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
