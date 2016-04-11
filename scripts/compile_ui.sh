#!/bin/bash

#pylupdate4 ../pynocchio.pro
#pyrcc4 -o ../src/main_window_view_rc.py ../rsc/main_window_view.qrc

pyside-rcc -o ../src/main_window_view_rc.py ../rsc/main_window_view.qrc

pyside-uic ../ui_files/main_window_view.ui -o ../src/ui_main_window_view.py
pyside-uic ../ui_files/go_to_page_dialog.ui -o ../src/ui_go_to_page_dialog.py
pyside-uic ../ui_files/about_dialog.ui -o ../src/ui_about_dialog.py
pyside-uic ../ui_files/preference_dialog.ui -o ../src/ui_preference_dialog.py
pyside-uic ../ui_files/bookmark_manager_dialog.ui -o ../src/ui_bookmark_manager_dialog.py
pyside-uic ../ui_files/progress_dialog.ui -o ../src/ui_progress_dialog.py

pyside-lupdate ../src/pynocchio.pro
