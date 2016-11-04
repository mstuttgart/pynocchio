# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
import distutils.log
import os
import re
import sys

from pynocchio.version import __version__


version = __version__

if sys.argv[-1] == 'build_deb':
    os.system('sh scripts/build_deb.sh %s' % version)
    sys.exit()
#
if sys.argv[-1] == 'build_ui':
    os.system('sh scripts/build_ui.sh')
    sys.exit()

if sys.argv[-1] == 'compile_pro':
    path = 'i18n/pynocchio.pro'
    os.system('pyside-lupdate -verbose %s' % path)
    sys.exit()

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

exec(open('pynocchio/version.py').read())

setup(
    name='pynocchio',
    version=version,
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
            'pynocchio/locale/pynocchio_en_US.qm',
            'pynocchio/locale/pynocchio_pt_BR.qm',
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
        'rarfile',
        'peewee',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Users',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python 3.5',
    ],
)
