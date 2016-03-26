# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pynocchio-comic-reader',
    version='1.0.2-2',
    packages=[
        'src', 'test'
    ],
    scripts=[
        'bin/pynocchio.sh'
    ],
    url='https://github.com/mstuttgart/pynocchio-comic-reader',
    license='GPLv3',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    description='Pynocchio Comic Reader is a image viewer specialized in '
                'comic reading.',
    requires=[
        'rarfile',
        'peewee'
    ],
    data_files=[
        ('/opt/pynocchio-comic-reader/', ['src/gui/about_dialog.ui',
                                          'src/gui/bookmark_manager_dialog.ui',
                                          'src/gui/go_to_page_dialog.ui',
                                          'src/gui/main_window_view.ui']),
        ('/opt/pynocchio-comic-reader/', ['src/locale/qt_pt_BR.qm']),
        ('/opt/pynocchio-comic-reader/', ['rsc/pynocchio_icon_2.png']),
        ('/usr/share/applications', ['linux/usr/share/applications/pynocchio-comic-reader.desktop']),
    ],
    classifiers=[
        'Development Status :: Stable',
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

