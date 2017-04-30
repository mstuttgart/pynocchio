# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys

from pynocchio import __version__

if sys.argv[-1] == 'build_deb':
    os.system('sh scripts/build_deb.sh %s' % __version__)
    sys.exit()
#
if sys.argv[-1] == 'build_ui':
    os.system('sh scripts/build_ui.sh %s' % __version__)
    sys.exit()

if sys.argv[-1] == 'build_pro':
    os.system('sh scripts/build_pro.sh')
    sys.exit()

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'version %s'" % (__version__, __version__))
    os.system("git push --tags")
    sys.exit()

setup(
    name='pynocchio',
    version=__version__,
    author='Michell Stuttgart Faria',
    author_email='michellstut@gmail.com',
    url='https://github.com/pynocchio',
    license='GPLv3 License',
    description='Pynocchio is a image viewer specialized in comic reading.',
    long_description='Pynocchio Comic Reader is a new and nice image viewer '
                     'which uses PySide API specialized in comic reading. '
                     'It is a comic reader that allow read cbr, cbz and cbt '
                     'files and have nice elementary icons theme on your '
                     'interface.',
    keywords="pynocchio comics manga viewer image",
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    test_suite='test',
    scripts=[
        'pynocchio-client.py',
    ],
    include_package_data=True,
    data_files=[
        ('/usr/share/applications', ['linux/applications/pynocchio.desktop']),
        ('/usr/share/pixmaps', ['linux/pixmaps/pynocchio.png']),
        ('/usr/share/pynocchio/locale/', [
            'pynocchio/locale/en-US.qm',
            'pynocchio/locale/pt-BR.qm',
        ]),
        ('/usr/share/icons/hicolor/16x16/apps',
         ['linux/hicolor/16x16/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/32x32/apps',
         ['linux/hicolor/32x32/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/48x48/apps',
         ['linux/hicolor/48x48/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/128x128/apps',
         ['linux/hicolor/128x128/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/256x256/apps',
         ['linux/hicolor/256x256/apps/pynocchio.png']),
    ],
    install_requires=[
        'rarfile>=2.8',
        'peewee>=2.9.2',
        'PyQt5>=5.7.1',
        'qdarkgraystyle>=0.0.2',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Users',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python 3.5',
    ],
)
