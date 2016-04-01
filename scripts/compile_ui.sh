#!/bin/bash

pylupdate4 ../pynocchio.pro
pyrcc4 -o ../src/main_window_view_rc.py ../rsc/main_window_view.qrc

#pyside-uic view/main_window.ui -o pynocchio_comic_reader/main_window_ui.py
#pyside-uic view/go_to_page_dialog.ui -o pynocchio_comic_reader/go_to_page_dialog_ui.py
#pyside-uic view/about_dialog.ui -o pynocchio_comic_reader/about_dialog_ui.py
#pyside-uic view/preference_dialog.ui -o pynocchio_comic_reader/preference_dialog_ui.py
#pyside-uic view/bookmark_manager_dialog.ui -o pynocchio_comic_reader/bookmark_manager_dialog_ui.py

#pyside-lupdate pyellow-comic-reader.pro
