SOURCES = src/lib/main_window_view.py \
src/lib/bookmark_manager_dialog.py \
src/lib/go_to_page_dialog.py \
src/lib/preference_dialog.py \
src/lib/uic_files/custom_widgets/status_bar.py


FORMS = resources/ui_files/about_dialog.ui \
resources/ui_files/bookmark_manager_dialog.ui \
resources/ui_files/go_to_page_dialog.ui \
resources/ui_files/preference_dialog.ui \
resources/ui_files/main_window_view.ui

TRANSLATIONS = i18n/pynocchio_en_US.ts i18n/pynocchio_pt_BR.ts

RESOURCES += resources/main_window_view.qrc
