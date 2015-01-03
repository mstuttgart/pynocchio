#!/bin/bash

pyside-rcc resource/main_window.qrc -o src/main_window_rc.py

pyside-uic view/main_window.ui -o src/dialogs/ui_python_files/ui_main_window.py
pyside-uic view/go_to_page_dialog.ui -o src/dialogs/ui_python_files/ui_go_to_page_dialog.py
pyside-uic view/about_dialog.ui -o src/dialogs/ui_python_files/ui_about_dialog.py
pyside-uic view/preference_dialog.ui -o src/dialogs/ui_python_files/ui_preference_dialog.py
pyside-uic view/bookmark_manager_dialog.ui -o src/dialogs/ui_python_files/ui_bookmark_manager_dialog.py

#pyside-lupdate pyellow-comic-reader.pro
