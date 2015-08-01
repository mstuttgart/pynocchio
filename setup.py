# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pynocchio-comic-reader',
    version='1.0.2',
    # package_dir={'': 'src'},
    packages=['src'],
    # scripts=['bin/pynocchio.sh'],
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
        ('/usr/share/pynocchio-comic-reader/', ['src/gui/about_dialog.ui',
                                                'src/gui/bookmark_manager_dialog.ui',
                                                'src/gui/go_to_page_dialog.ui',
                                                'src/gui/main_window_view.ui']),
        ('/usr/share/pynocchio-comic-reader/', ['lib/*.py']),
        ('/usr/share/pynocchio-comic-reader/', ['src/locale/qt_pt_BR.qm']),
        ('/usr/share/pynocchio-comic-reader/', ['rsc/pynocchio_icon.png']),
        ('/usr/share/applications', ['linux/usr/share/applications/pynocchio-comic-reader.desktop']),
        ('share/doc/', ['README.md'])],
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

