# -*- coding: UTF-8 -*-
from main_window import MainWindow
from PyQt4 import QtCore, QtGui
import ui_file_loader


def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Pynocchio')
    # QCoreApplication.setApplicationName('Pynocchio')

    # ui_file_loader.ui
    # main_window = ui_file_loader.loadUi("../view/main_window.ui")
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
