#!/bin/bash
cd ..

pyside-rcc -verbose -o pynocchio/src/uic_files/main_window_view_rc.py data/main_window_view.qrc

pyside-uic data/ui_files/main_window_view.ui -o pynocchio/src/uic_files/ui_main_window_view.py
pyside-uic data/ui_files/go_to_page_dialog.ui -o pynocchio/src/uic_files/ui_go_to_page_dialog.py
pyside-uic data/ui_files/about_dialog.ui -o pynocchio/src/uic_files/ui_about_dialog.py
pyside-uic data/ui_files/preference_dialog.ui -o pynocchio/src/uic_files/ui_preference_dialog.py
pyside-uic data/ui_files/bookmark_manager_dialog.ui -o pynocchio/src/uic_files/ui_bookmark_manager_dialog.py

pyside-lupdate -verbose pynocchio.pro
