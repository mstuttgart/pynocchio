#!/bin/bash

#pylupdate4 ../pynocchio.pro
#pyrcc4 -o ../src/main_window_view_rc.py ../rsc/main_window_view.qrc

pyside-rcc -o ../src/main_window_view_rc.py ../rsc/main_window_view.qrc

pyside-uic ../ui_files/main_window_view.ui -o ../src/view/main_window_view_ui.py
pyside-uic ../ui_files/go_to_page_dialog.ui -o ../src/view/go_to_page_dialog_ui.py
pyside-uic ../ui_files/about_dialog.ui -o ../src/view/about_dialog_ui.py
pyside-uic ../ui_files/preference_dialog.ui -o ../src/view/preference_dialog_ui.py
pyside-uic ../ui_files/bookmark_manager_dialog.ui -o ../src/view/bookmark_manager_dialog_ui.py
pyside-uic ../ui_files/progress_dialog.ui -o ../src/view/progress_dialog_ui.py

#pyside-lupdate pynocchio-comic-reader.pro
