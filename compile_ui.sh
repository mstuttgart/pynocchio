#!/bin/bash

pyside-rcc resource/main_window.qrc -o src/main_window_rc.py

pyside-uic view/main_window.ui -o src/ui_main_window.py
pyside-uic view/go_to_page_dialog.ui -o src/ui_go_to_page_dialog.py
pyside-uic view/about_dialog.ui -o src/ui_about_dialog.py
pyside-uic view/preference_dialog.ui -o src/ui_preference_dialog.py

pyside-lupdate pyellow-comic-reader.pro
