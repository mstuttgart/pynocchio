#!/bin/bash
pyside-rcc -o ../pynocchio_comic_reader/lib/uic_files/main_window_view_rc.py main_window_view.qrc

pyside-uic ui_files/main_window_view.ui -o ../pynocchio_comic_reader/lib/uic_files/ui_main_window_view.py
pyside-uic ui_files/go_to_page_dialog.ui -o ../pynocchio_comic_reader/lib/uic_files/ui_go_to_page_dialog.py
pyside-uic ui_files/about_dialog.ui -o ../pynocchio_comic_reader/lib/uic_files/ui_about_dialog.py
pyside-uic ui_files/preference_dialog.ui -o ../pynocchio_comic_reader/lib/uic_files/ui_preference_dialog.py
pyside-uic ui_files/bookmark_manager_dialog.ui -o ../pynocchio_comic_reader/lib/uic_files/ui_bookmark_manager_dialog.py
pyside-uic ui_files/progress_dialog.ui -o ../pynocchio_comic_reader/lib/uic_files/ui_progress_dialog.py

pyside-lupdate -verbose ../pynocchio.pro
