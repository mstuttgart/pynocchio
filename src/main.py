# -*- coding: UTF-8 -*-
from PyQt4 import QtGui, QtCore

from main_window import MainWindow


def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Pynocchio')

    translator = QtCore.QTranslator()
    translator.load("../i18n/pt_BR.qm")
    app.installTranslator(translator)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
