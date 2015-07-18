# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pynocchio-comic-reader',
    version='0.1',
    package_dir = {'':'pynocchio-comic-reader'},
    packages=['src'],
    scripts=['bin/pynocchio.sh'],
    url='https://github.com/mstuttgart/pynocchio-comic-reader',
    license='GPLv3',
    author='Michell Stuttgart',
    author_email='michell.stut@gmail.com.br',
    description='Pynocchio Comic Reader is a image viewer specialized in '
                'manga/comic reading.',
    requires=[
        'rarfile',
        'peewee'
    ],
    data_files=[
        ('/usr/share/pynocchio-comic-reader/', ['pynocchio-comic-reader/gui/about_dialog.ui',
                                   'pynocchio-comic-reader/gui/bookmark_manager_dialog.ui',
                                   'pynocchio-comic-reader/gui/go_to_page_dialog.ui',
                                   'pynocchio-comic-reader/gui/main_window_view.ui']),
        ('/usr/share/pynocchio-comic-reader/', ['pynocchio-comic-reader/translation/qt_pt_BR.qm']),
        ('/usr/share/pynocchio-comic-reader/', ['pynocchio-comic-reader/resource/pynocchio_icon.png']),
        ('/usr/share/applications', ['pynocchio-comic-reader.desktop']),
        ('share/doc/', ['README.md'])],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Bug Tracking',
    ],

)

