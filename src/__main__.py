# -*- coding: UTF-8 -*-

from PySide import QtGui
from main_window import MainWindow


def main():

    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('PySideDemoApplication')

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
