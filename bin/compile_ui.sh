#!/bin/bash

pylupdate4 ../pynocchio-comic-reader/pynocchio.pro
pyrcc4 -o ../pynocchio-comic-reader/src/main_window_view_rc.py ../pynocchio-comic-reader/resource/main_window_view.qrc

#pyside-uic view/main_window.ui -o src/main_window_ui.py
#pyside-uic view/go_to_page_dialog.ui -o src/go_to_page_dialog_ui.py
#pyside-uic view/about_dialog.ui -o src/about_dialog_ui.py
#pyside-uic view/preference_dialog.ui -o src/preference_dialog_ui.py
#pyside-uic view/bookmark_manager_dialog.ui -o src/bookmark_manager_dialog_ui.py

#pyside-lupdate pyellow-comic-reader.pro
