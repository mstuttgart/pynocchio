# -*- coding: UTF-8 -*-
from main_window import MainWindow
from PyQt4 import QtGui


def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Pynocchio')
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
