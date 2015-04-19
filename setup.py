from distutils.core import setup

setup(
    name='pynocchio-comic-reader',
    version='beta',
    package_dir = {' ':'src'},
    packages=[' '],
    data_files = [('src/', ['src/about_dialog.ui',
                            'src/bookmark_manager_dialog.ui',
                            'src/go_to_page_dialog.ui',
                            'src/main_window.ui']),
                   ('i10n',['i18n/qt_pt_BR.qm']),
                 ],
    url='http://pynocchio.github.io/',
    license='GPLv3',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    description='Comic Reader', 
    requires=['peewee', 'rarfile', 'requests', 'lxml'],
    platforms = 'UNIX',
    
)
