# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/michell/Projects/pynocchio/forms/main_window_view.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowView(object):
    def setupUi(self, MainWindowView):
        MainWindowView.setObjectName("MainWindowView")
        MainWindowView.resize(1048, 561)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowView.sizePolicy().hasHeightForWidth())
        MainWindowView.setSizePolicy(sizePolicy)
        MainWindowView.setBaseSize(QtCore.QSize(0, 3))
        MainWindowView.setFocusPolicy(QtCore.Qt.WheelFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pynocchio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowView.setWindowIcon(icon)
        MainWindowView.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #bdff66;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 1px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        MainWindowView.setIconSize(QtCore.QSize(22, 22))
        MainWindowView.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindowView.setAnimated(True)
        MainWindowView.setDocumentMode(False)
        MainWindowView.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindowView.setDockNestingEnabled(False)
        MainWindowView.setUnifiedTitleAndToolBarOnMac(True)
        self.central_widget = QtWidgets.QWidget(MainWindowView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setAutoFillBackground(False)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qscroll_area_viewer = QScrollAreaViewer(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qscroll_area_viewer.sizePolicy().hasHeightForWidth())
        self.qscroll_area_viewer.setSizePolicy(sizePolicy)
        self.qscroll_area_viewer.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qscroll_area_viewer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qscroll_area_viewer.setAutoFillBackground(True)
        self.qscroll_area_viewer.setStyleSheet("background-color: rgb(5, 5, 5);")
        self.qscroll_area_viewer.setFrameShape(QtWidgets.QFrame.HLine)
        self.qscroll_area_viewer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.qscroll_area_viewer.setLineWidth(0)
        self.qscroll_area_viewer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.qscroll_area_viewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.qscroll_area_viewer.setWidgetResizable(True)
        self.qscroll_area_viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.qscroll_area_viewer.setObjectName("qscroll_area_viewer")
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 1048, 476))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area_widget_contents.sizePolicy().hasHeightForWidth())
        self.scroll_area_widget_contents.setSizePolicy(sizePolicy)
        self.scroll_area_widget_contents.setAutoFillBackground(False)
        self.scroll_area_widget_contents.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scroll_area_widget_contents)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scroll_area_widget_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap(":/icons/pynocchio_icon.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.qscroll_area_viewer.setWidget(self.scroll_area_widget_contents)
        self.horizontalLayout.addWidget(self.qscroll_area_viewer)
        MainWindowView.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindowView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setAcceptDrops(False)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_recent_files = QtWidgets.QMenu(self.menu_file)
        self.menu_recent_files.setEnabled(True)
        self.menu_recent_files.setTearOffEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/document-open-recent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_recent_files.setIcon(icon1)
        self.menu_recent_files.setSeparatorsCollapsible(False)
        self.menu_recent_files.setObjectName("menu_recent_files")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_navegation = QtWidgets.QMenu(self.menubar)
        self.menu_navegation.setAcceptDrops(False)
        self.menu_navegation.setTearOffEnabled(False)
        self.menu_navegation.setObjectName("menu_navegation")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        self.menu_bookmarks = QtWidgets.QMenu(self.menubar)
        self.menu_bookmarks.setTearOffEnabled(False)
        self.menu_bookmarks.setSeparatorsCollapsible(True)
        self.menu_bookmarks.setObjectName("menu_bookmarks")
        self.menu_recent_bookmarks = QtWidgets.QMenu(self.menu_bookmarks)
        self.menu_recent_bookmarks.setIcon(icon1)
        self.menu_recent_bookmarks.setObjectName("menu_recent_bookmarks")
        MainWindowView.setMenuBar(self.menubar)
        self.toolbar = QtWidgets.QToolBar(MainWindowView)
        self.toolbar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolbar.setAcceptDrops(True)
        self.toolbar.setAutoFillBackground(False)
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolbar.setFloatable(False)
        self.toolbar.setObjectName("toolbar")
        MainWindowView.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.statusbar = StatusBar(MainWindowView)
        self.statusbar.setObjectName("statusbar")
        MainWindowView.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(MainWindowView)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/help-info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon2)
        self.action_about.setObjectName("action_about")
        self.action_about_qt = QtWidgets.QAction(MainWindowView)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_exit = QtWidgets.QAction(MainWindowView)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/application-exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit.setIcon(icon3)
        self.action_exit.setObjectName("action_exit")
        self.action_next_page = QtWidgets.QAction(MainWindowView)
        self.action_next_page.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_page.setIcon(icon4)
        self.action_next_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_next_page.setVisible(True)
        self.action_next_page.setPriority(QtWidgets.QAction.HighPriority)
        self.action_next_page.setObjectName("action_next_page")
        self.action_previous_page = QtWidgets.QAction(MainWindowView)
        self.action_previous_page.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-previous.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_page.setIcon(icon5)
        self.action_previous_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_previous_page.setVisible(True)
        self.action_previous_page.setObjectName("action_previous_page")
        self.action_first_page = QtWidgets.QAction(MainWindowView)
        self.action_first_page.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-first.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_first_page.setIcon(icon6)
        self.action_first_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_first_page.setObjectName("action_first_page")
        self.action_last_page = QtWidgets.QAction(MainWindowView)
        self.action_last_page.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-last.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_last_page.setIcon(icon7)
        self.action_last_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_last_page.setObjectName("action_last_page")
        self.action_rotate_left = QtWidgets.QAction(MainWindowView)
        self.action_rotate_left.setCheckable(False)
        self.action_rotate_left.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/object-rotate-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_left.setIcon(icon8)
        self.action_rotate_left.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_rotate_left.setObjectName("action_rotate_left")
        self.action_rotate_right = QtWidgets.QAction(MainWindowView)
        self.action_rotate_right.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/object-rotate-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_right.setIcon(icon9)
        self.action_rotate_right.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_rotate_right.setObjectName("action_rotate_right")
        self.action_horizontal_fit = QtWidgets.QAction(MainWindowView)
        self.action_horizontal_fit.setCheckable(True)
        self.action_horizontal_fit.setChecked(False)
        self.action_horizontal_fit.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/horizontal-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_horizontal_fit.setIcon(icon10)
        self.action_horizontal_fit.setVisible(True)
        self.action_horizontal_fit.setObjectName("action_horizontal_fit")
        self.action_fullscreen = QtWidgets.QAction(MainWindowView)
        self.action_fullscreen.setCheckable(False)
        self.action_fullscreen.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/fullscreen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_fullscreen.setIcon(icon11)
        self.action_fullscreen.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_fullscreen.setObjectName("action_fullscreen")
        self.action_go_to_page = QtWidgets.QAction(MainWindowView)
        self.action_go_to_page.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_go_to_page.setIcon(icon12)
        self.action_go_to_page.setObjectName("action_go_to_page")
        self.action_original_fit = QtWidgets.QAction(MainWindowView)
        self.action_original_fit.setCheckable(True)
        self.action_original_fit.setChecked(True)
        self.action_original_fit.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/original-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_original_fit.setIcon(icon13)
        self.action_original_fit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.action_original_fit.setVisible(True)
        self.action_original_fit.setObjectName("action_original_fit")
        self.action_show_statusbar = QtWidgets.QAction(MainWindowView)
        self.action_show_statusbar.setCheckable(True)
        self.action_show_statusbar.setChecked(True)
        self.action_show_statusbar.setObjectName("action_show_statusbar")
        self.action_add_bookmark = QtWidgets.QAction(MainWindowView)
        self.action_add_bookmark.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/bookmark-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_bookmark.setIcon(icon14)
        self.action_add_bookmark.setVisible(True)
        self.action_add_bookmark.setObjectName("action_add_bookmark")
        self.action_remove_bookmark = QtWidgets.QAction(MainWindowView)
        self.action_remove_bookmark.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/stock_delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove_bookmark.setIcon(icon15)
        self.action_remove_bookmark.setVisible(False)
        self.action_remove_bookmark.setIconVisibleInMenu(True)
        self.action_remove_bookmark.setObjectName("action_remove_bookmark")
        self.action_bookmark_manager = QtWidgets.QAction(MainWindowView)
        self.action_bookmark_manager.setEnabled(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/apps/48/office-database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_bookmark_manager.setIcon(icon16)
        self.action_bookmark_manager.setObjectName("action_bookmark_manager")
        self.action_open_folder = QtWidgets.QAction(MainWindowView)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/document-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_folder.setIcon(icon17)
        self.action_open_folder.setVisible(True)
        self.action_open_folder.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.action_open_folder.setIconVisibleInMenu(True)
        self.action_open_folder.setObjectName("action_open_folder")
        self.action_next_comic = QtWidgets.QAction(MainWindowView)
        self.action_next_comic.setEnabled(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/media-skip-forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_comic.setIcon(icon18)
        self.action_next_comic.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_next_comic.setObjectName("action_next_comic")
        self.action_previous_comic = QtWidgets.QAction(MainWindowView)
        self.action_previous_comic.setEnabled(False)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/media-skip-backward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_comic.setIcon(icon19)
        self.action_previous_comic.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_previous_comic.setObjectName("action_previous_comic")
        self.action_preference_dialog = QtWidgets.QAction(MainWindowView)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/document-properties.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_preference_dialog.setIcon(icon20)
        self.action_preference_dialog.setVisible(False)
        self.action_preference_dialog.setObjectName("action_preference_dialog")
        self.action_vertical_fit = QtWidgets.QAction(MainWindowView)
        self.action_vertical_fit.setCheckable(True)
        self.action_vertical_fit.setChecked(False)
        self.action_vertical_fit.setEnabled(False)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/vertical-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vertical_fit.setIcon(icon21)
        self.action_vertical_fit.setAutoRepeat(True)
        self.action_vertical_fit.setVisible(True)
        self.action_vertical_fit.setObjectName("action_vertical_fit")
        self.action_best_fit = QtWidgets.QAction(MainWindowView)
        self.action_best_fit.setCheckable(True)
        self.action_best_fit.setChecked(False)
        self.action_best_fit.setEnabled(False)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/best-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_best_fit.setIcon(icon22)
        self.action_best_fit.setVisible(True)
        self.action_best_fit.setObjectName("action_best_fit")
        self.action_save_image = QtWidgets.QAction(MainWindowView)
        self.action_save_image.setEnabled(True)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_image.setIcon(icon23)
        self.action_save_image.setObjectName("action_save_image")
        self.action_open_file = QtWidgets.QAction(MainWindowView)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/archive-extract.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_file.setIcon(icon24)
        font = QtGui.QFont()
        self.action_open_file.setFont(font)
        self.action_open_file.setObjectName("action_open_file")
        self.actionRecent_file_1 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_1.setText("recent_file_1")
        self.actionRecent_file_1.setIconText("recent_file_1")
        self.actionRecent_file_1.setToolTip("recent_file_1")
        self.actionRecent_file_1.setVisible(False)
        self.actionRecent_file_1.setObjectName("actionRecent_file_1")
        self.actionRecent_file_2 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_2.setText("recent_file_2")
        self.actionRecent_file_2.setIconText("recent_file_2")
        self.actionRecent_file_2.setToolTip("recent_file_2")
        self.actionRecent_file_2.setVisible(False)
        self.actionRecent_file_2.setObjectName("actionRecent_file_2")
        self.actionRecent_file_3 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_3.setText("recent_file_3")
        self.actionRecent_file_3.setIconText("recent_file_3")
        self.actionRecent_file_3.setToolTip("recent_file_3")
        self.actionRecent_file_3.setVisible(False)
        self.actionRecent_file_3.setObjectName("actionRecent_file_3")
        self.actionRecent_file_4 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_4.setText("recent_file_4")
        self.actionRecent_file_4.setIconText("recent_file_4")
        self.actionRecent_file_4.setToolTip("recent_file_4")
        self.actionRecent_file_4.setVisible(False)
        self.actionRecent_file_4.setObjectName("actionRecent_file_4")
        self.actionRecent_file_5 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_5.setText("recent_file_5")
        self.actionRecent_file_5.setIconText("recent_file_5")
        self.actionRecent_file_5.setToolTip("recent_file_5")
        self.actionRecent_file_5.setVisible(False)
        self.actionRecent_file_5.setObjectName("actionRecent_file_5")
        self.actionRecent_file_6 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_6.setText("recent_file_6")
        self.actionRecent_file_6.setToolTip("recent_file_6")
        self.actionRecent_file_6.setVisible(False)
        self.actionRecent_file_6.setObjectName("actionRecent_file_6")
        self.actionRecent_file_7 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_7.setText("recent_file_7")
        self.actionRecent_file_7.setIconText("recent_file_7")
        self.actionRecent_file_7.setToolTip("recent_file_7")
        self.actionRecent_file_7.setVisible(False)
        self.actionRecent_file_7.setObjectName("actionRecent_file_7")
        self.actionRecent_file_8 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_8.setText("recent_file_8")
        self.actionRecent_file_8.setIconText("recent_file_8")
        self.actionRecent_file_8.setToolTip("recent_file_8")
        self.actionRecent_file_8.setVisible(False)
        self.actionRecent_file_8.setObjectName("actionRecent_file_8")
        self.actionRecent_file_9 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_9.setText("recent_file_9")
        self.actionRecent_file_9.setIconText("recent_file_9")
        self.actionRecent_file_9.setToolTip("recent_file_9")
        self.actionRecent_file_9.setVisible(False)
        self.actionRecent_file_9.setObjectName("actionRecent_file_9")
        self.actionRecent_file_10 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_file_10.setText("recent_file_10")
        self.actionRecent_file_10.setIconText("recent_file_10")
        self.actionRecent_file_10.setToolTip("recent_file_10")
        self.actionRecent_file_10.setVisible(False)
        self.actionRecent_file_10.setObjectName("actionRecent_file_10")
        self.actionRecent_bookmark_1 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_bookmark_1.setText("recent_bookmark_1")
        self.actionRecent_bookmark_1.setIconText("recent_bookmark_1")
        self.actionRecent_bookmark_1.setToolTip("recent_bookmark_1")
        self.actionRecent_bookmark_1.setVisible(False)
        self.actionRecent_bookmark_1.setObjectName("actionRecent_bookmark_1")
        self.actionRecent_bookmark_2 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_bookmark_2.setText("recent_bookmark_2")
        self.actionRecent_bookmark_2.setIconText("recent_bookmark_2")
        self.actionRecent_bookmark_2.setToolTip("recent_bookmark_2")
        self.actionRecent_bookmark_2.setVisible(False)
        self.actionRecent_bookmark_2.setObjectName("actionRecent_bookmark_2")
        self.actionRecent_bookmark_3 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_bookmark_3.setText("recent_bookmark_3")
        self.actionRecent_bookmark_3.setIconText("recent_bookmark_3")
        self.actionRecent_bookmark_3.setToolTip("recent_bookmark_3")
        self.actionRecent_bookmark_3.setVisible(False)
        self.actionRecent_bookmark_3.setObjectName("actionRecent_bookmark_3")
        self.actionRecent_bookmark_4 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_bookmark_4.setText("recent_bookmark_4")
        self.actionRecent_bookmark_4.setToolTip("recent_bookmark_4")
        self.actionRecent_bookmark_4.setVisible(False)
        self.actionRecent_bookmark_4.setObjectName("actionRecent_bookmark_4")
        self.actionRecent_bookmark_5 = QtWidgets.QAction(MainWindowView)
        self.actionRecent_bookmark_5.setText("recent_bookmark_5")
        self.actionRecent_bookmark_5.setIconText("recent_bookmark_5")
        self.actionRecent_bookmark_5.setToolTip("recent_bookmark_5")
        self.actionRecent_bookmark_5.setVisible(False)
        self.actionRecent_bookmark_5.setObjectName("actionRecent_bookmark_5")
        self.action_en_us = QtWidgets.QAction(MainWindowView)
        self.action_en_us.setCheckable(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icons/famfamfam_flag_icons/png/us.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_en_us.setIcon(icon25)
        self.action_en_us.setObjectName("action_en_us")
        self.action_pt_br = QtWidgets.QAction(MainWindowView)
        self.action_pt_br.setCheckable(True)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/icons/famfamfam_flag_icons/png/br.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pt_br.setIcon(icon26)
        self.action_pt_br.setIconText("pt_BR")
        self.action_pt_br.setObjectName("action_pt_br")
        self.action_show_toolbar = QtWidgets.QAction(MainWindowView)
        self.action_show_toolbar.setCheckable(True)
        self.action_show_toolbar.setChecked(True)
        self.action_show_toolbar.setObjectName("action_show_toolbar")
        self.menu_recent_files.addAction(self.actionRecent_file_1)
        self.menu_recent_files.addAction(self.actionRecent_file_2)
        self.menu_recent_files.addAction(self.actionRecent_file_3)
        self.menu_recent_files.addAction(self.actionRecent_file_4)
        self.menu_recent_files.addAction(self.actionRecent_file_5)
        self.menu_recent_files.addAction(self.actionRecent_file_6)
        self.menu_recent_files.addAction(self.actionRecent_file_7)
        self.menu_recent_files.addAction(self.actionRecent_file_8)
        self.menu_recent_files.addAction(self.actionRecent_file_9)
        self.menu_recent_files.addAction(self.actionRecent_file_10)
        self.menu_file.addAction(self.action_open_file)
        self.menu_file.addAction(self.action_open_folder)
        self.menu_file.addAction(self.menu_recent_files.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save_image)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_view.addAction(self.action_fullscreen)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_original_fit)
        self.menu_view.addAction(self.action_vertical_fit)
        self.menu_view.addAction(self.action_horizontal_fit)
        self.menu_view.addAction(self.action_best_fit)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_rotate_left)
        self.menu_view.addAction(self.action_rotate_right)
        self.menu_navegation.addAction(self.action_next_page)
        self.menu_navegation.addAction(self.action_previous_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_first_page)
        self.menu_navegation.addAction(self.action_last_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_go_to_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_next_comic)
        self.menu_navegation.addAction(self.action_previous_comic)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_about_qt)
        self.menu_settings.addAction(self.action_show_toolbar)
        self.menu_settings.addAction(self.action_show_statusbar)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.action_preference_dialog)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_1)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_2)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_3)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_4)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_5)
        self.menu_bookmarks.addAction(self.action_add_bookmark)
        self.menu_bookmarks.addAction(self.action_remove_bookmark)
        self.menu_bookmarks.addSeparator()
        self.menu_bookmarks.addAction(self.action_bookmark_manager)
        self.menu_bookmarks.addAction(self.menu_recent_bookmarks.menuAction())
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_navegation.menuAction())
        self.menubar.addAction(self.menu_bookmarks.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolbar.addAction(self.action_open_file)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_previous_comic)
        self.toolbar.addAction(self.action_first_page)
        self.toolbar.addAction(self.action_previous_page)
        self.toolbar.addAction(self.action_next_page)
        self.toolbar.addAction(self.action_last_page)
        self.toolbar.addAction(self.action_next_comic)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_go_to_page)
        self.toolbar.addAction(self.action_add_bookmark)
        self.toolbar.addAction(self.action_remove_bookmark)
        self.toolbar.addAction(self.action_bookmark_manager)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_rotate_left)
        self.toolbar.addAction(self.action_rotate_right)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_original_fit)
        self.toolbar.addAction(self.action_vertical_fit)
        self.toolbar.addAction(self.action_horizontal_fit)
        self.toolbar.addAction(self.action_best_fit)
        self.toolbar.addAction(self.action_fullscreen)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_exit)

        self.retranslateUi(MainWindowView)
        QtCore.QMetaObject.connectSlotsByName(MainWindowView)

    def retranslateUi(self, MainWindowView):
        _translate = QtCore.QCoreApplication.translate
        MainWindowView.setWindowTitle(_translate("MainWindowView", "Pynocchio Comic Reader"))
        MainWindowView.setAccessibleName(_translate("MainWindowView", "Pynocchio Comic Reader"))
        MainWindowView.setAccessibleDescription(_translate("MainWindowView", "The Best Comic Reader"))
        self.menu_file.setTitle(_translate("MainWindowView", "&File"))
        self.menu_recent_files.setTitle(_translate("MainWindowView", "Recent files"))
        self.menu_view.setTitle(_translate("MainWindowView", "&View"))
        self.menu_navegation.setTitle(_translate("MainWindowView", "&Navegation"))
        self.menu_help.setTitle(_translate("MainWindowView", "&Help"))
        self.menu_settings.setTitle(_translate("MainWindowView", "&Settings"))
        self.menu_bookmarks.setTitle(_translate("MainWindowView", "&Bookmarks"))
        self.menu_recent_bookmarks.setTitle(_translate("MainWindowView", "Recente bookmarks"))
        self.toolbar.setWindowTitle(_translate("MainWindowView", "toolBar"))
        self.action_about.setText(_translate("MainWindowView", "About Pynocchio"))
        self.action_about_qt.setText(_translate("MainWindowView", "About Qt"))
        self.action_exit.setText(_translate("MainWindowView", "Exit"))
        self.action_exit.setShortcut(_translate("MainWindowView", "Ctrl+Q"))
        self.action_next_page.setText(_translate("MainWindowView", "Next page"))
        self.action_next_page.setShortcut(_translate("MainWindowView", "Right"))
        self.action_previous_page.setText(_translate("MainWindowView", "Previous page"))
        self.action_previous_page.setShortcut(_translate("MainWindowView", "Left"))
        self.action_first_page.setText(_translate("MainWindowView", "First page"))
        self.action_first_page.setShortcut(_translate("MainWindowView", "Ctrl+Left"))
        self.action_last_page.setText(_translate("MainWindowView", "Last page"))
        self.action_last_page.setShortcut(_translate("MainWindowView", "Ctrl+Right"))
        self.action_rotate_left.setText(_translate("MainWindowView", "Rotate left"))
        self.action_rotate_left.setShortcut(_translate("MainWindowView", "Ctrl+Shift+R"))
        self.action_rotate_right.setText(_translate("MainWindowView", "Rotate right"))
        self.action_rotate_right.setShortcut(_translate("MainWindowView", "Ctrl+R"))
        self.action_horizontal_fit.setText(_translate("MainWindowView", "Horizontal fit"))
        self.action_horizontal_fit.setShortcut(_translate("MainWindowView", "Ctrl+K"))
        self.action_fullscreen.setText(_translate("MainWindowView", "Fullscreen"))
        self.action_fullscreen.setShortcut(_translate("MainWindowView", "F"))
        self.action_go_to_page.setText(_translate("MainWindowView", "Go to page"))
        self.action_go_to_page.setShortcut(_translate("MainWindowView", "Ctrl+G"))
        self.action_original_fit.setText(_translate("MainWindowView", "Original fit"))
        self.action_original_fit.setShortcut(_translate("MainWindowView", "Ctrl+H"))
        self.action_show_statusbar.setText(_translate("MainWindowView", "Show Statusbar"))
        self.action_add_bookmark.setText(_translate("MainWindowView", "Add bookmark"))
        self.action_remove_bookmark.setText(_translate("MainWindowView", "Remove bookmark"))
        self.action_bookmark_manager.setText(_translate("MainWindowView", "Bookmark manager"))
        self.action_open_folder.setText(_translate("MainWindowView", "Open Folder"))
        self.action_next_comic.setText(_translate("MainWindowView", "Next Comic"))
        self.action_next_comic.setShortcut(_translate("MainWindowView", "Ctrl+Shift+Right"))
        self.action_previous_comic.setText(_translate("MainWindowView", "Previous Comic"))
        self.action_previous_comic.setShortcut(_translate("MainWindowView", "Ctrl+Shift+Left"))
        self.action_preference_dialog.setText(_translate("MainWindowView", "Preferences"))
        self.action_vertical_fit.setText(_translate("MainWindowView", "Vertical fit"))
        self.action_vertical_fit.setShortcut(_translate("MainWindowView", "Ctrl+J"))
        self.action_best_fit.setText(_translate("MainWindowView", "Best fit"))
        self.action_best_fit.setShortcut(_translate("MainWindowView", "Ctrl+L"))
        self.action_save_image.setText(_translate("MainWindowView", "Save image"))
        self.action_save_image.setWhatsThis(_translate("MainWindowView", "Save current image in disk."))
        self.action_save_image.setShortcut(_translate("MainWindowView", "Ctrl+S"))
        self.action_open_file.setText(_translate("MainWindowView", "Open File"))
        self.action_open_file.setShortcut(_translate("MainWindowView", "Ctrl+O"))
        self.action_en_us.setText(_translate("MainWindowView", "English"))
        self.action_en_us.setIconText(_translate("MainWindowView", "en_US"))
        self.action_pt_br.setText(_translate("MainWindowView", "Portuguese"))
        self.action_show_toolbar.setText(_translate("MainWindowView", "Show Toolbar"))

from .custom_widgets.qscroll_area_viewer import QScrollAreaViewer
from .custom_widgets.status_bar import StatusBar
from . import main_window_view_rc
