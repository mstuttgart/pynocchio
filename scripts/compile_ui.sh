#!/bin/bash

#pylupdate4 ../pynocchio.pro
#pyrcc4 -o ../src/main_window_view_rc.py ../rsc/main_window_view.qrc

pyside-rcc -o ../src/main_window_view_rc.py ../rsc/main_window_view.qrc

pyside-uic ../ui_files/main_window_view.ui -o ../src/view/uic/ui_main_window_view.py
pyside-uic ../ui_files/go_to_page_dialog.ui -o ../src/view/uic/ui_go_to_page_dialog.py
pyside-uic ../ui_files/about_dialog.ui -o ../src/view/uic/ui_about_dialog.py
pyside-uic ../ui_files/preference_dialog.ui -o ../src/view/uic/ui_preference_dialog.py
pyside-uic ../ui_files/bookmark_manager_dialog.ui -o ../src/view/uic/ui_bookmark_manager_dialog.py

#pyside-lupdate pynocchio-comic-reader.pro
