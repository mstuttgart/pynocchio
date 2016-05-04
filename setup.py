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

import distutils.cmd
import distutils.log
from setuptools import setup, find_packages
import os
import re
import sys


try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    build_ui = None  # user won't have pyqt_distutils when deploying
    cmdclass = {}


def get_version(package):
    """
    Based in https://github.com/tomchristie/django-rest-framework/blob/
    971578ca345c3d3bae7fd93b87c41d43483b6f05/setup.py
    :param package Package name
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


package_name = 'pynocchio'
version = get_version(package_name)
debian_version = '1'


class BuildProFileCommand(distutils.cmd.Command):
    """
    A command to compile pro condig files.
    """

    description = "Compile PySide pro files"

    # The format is (long option, short option, description).
    user_options = [
        ('path=', None, 'The path of pro files folder'),
    ]

    def initialize_options(self):
        self.path = 'pynocchio.pro'

    def finalize_options(self):
        assert os.path.isfile(self.path), ('[INFO] %s not is valid file!' %
                                           self.path)
        assert os.path.exists(self.path), ('[INFO] File %s not exist!' %
                                           self.path)

    def run(self):
        print "[INFO] Compile pro files..."
        os.system('pyside-lupdate -verbose %s' % self.path)
        sys.exit()


class BuildDEBPackageCommand(distutils.cmd.Command):
    """
    A command build deb package.
    """

    description = "Build .deb package"

    # The format is (long option, short option, description).
    user_options = [
        ('folder=', None, 'The folder where deb package will be build'),
        ('upload=', None, 'Upload package to launchpad'),
        ('stable=', None, 'Upload package to launchpad stable ppa'),
    ]

    def initialize_options(self):
        self.folder = 'dist'
        self.upload = None
        self.stable = None

    def finalize_options(self):
        if os.path.isdir(self.folder) and os.path.lexists(self.folder):
            os.system('rm -rf %s' % self.folder)

        if self.upload:
            assert self.upload == 'True'

        if self.stable:
            assert self.stable == 'True'

    def run(self):

        print "[INFO] Compile a deb package..."

        os.system('mkdir %s' % self.folder)
        os.system('cp stdeb.cfg setup.py pynocchio_run %s' % self.folder)
        os.system('cp -r pynocchio linux %s' % self.folder)
        os.system('cd %s && python setup.py --command-packages=stdeb.command '
                  'sdist_dsc --package %s' % (self.folder, package_name))
        os.system(
            'cd %s/deb_dist && dpkg-source -x %s_%s-%s.dsc' % (self.folder,
                                                               package_name,
                                                               version,
                                                               debian_version))
        os.system('cd %s/deb_dist/%s-%s && debuild -S -sa' % (self.folder,
                                                              package_name,
                                                              version))

        if self.upload and self.stable:
            os.system('cd %s/deb_dist && dput '
                      'ppa:pynocchio-team/pynocchio-stable '
                      '%s_%s-%s_source.changes' % (self.folder,
                                                   package_name,
                                                   version,
                                                   debian_version))
        elif self.upload and not self.stable:
            os.system('cd %s/deb_dist && dput '
                      'ppa:pynocchio-team/pynocchio-dev '
                      '%s_%s-%s_source.changes' % (self.folder,
                                                   package_name,
                                                   version,
                                                   debian_version))
        else:
            print '[INFO] Local build.'

        sys.exit()

cmdclass['build_pro'] = BuildProFileCommand
cmdclass['build_deb'] = BuildDEBPackageCommand

setup(
    name=package_name,
    version=version,
    author='Michell Stuttgart Faria',
    author_email='michellstut@gmail.com',
    url='https://github.com/mstuttgart/pynocchio-comic-reader',
    license='GPL v3',
    description='Pynocchio is a image viewer specialized in comic reading.',
    long_description='Pynocchio Comic Reader is a new and nice image viewer '
                     'which uses PySide API specialized in comic reading. '
                     'It is a comic reader that allow read cbr, cbz and cbt '
                     'files and have nice elementary icons theme on your '
                     'interface.',
    keywords="pynocchio comics manga viewer image",
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    test_suite='test',
    cmdclass=cmdclass,
    scripts=[
        'pynocchio_run',
    ],
    include_package_data=True,
    data_files=[
        ('/usr/share/applications', ['linux/applications/pynocchio.desktop']),
        ('/usr/share/pixmaps', ['linux/pixmaps/pynocchio_icon.png']),
        ('/usr/share/pynocchio/locale/', [
            'pynocchio/locale/pynocchio_en_US.qm',
            'pynocchio/locale/pynocchio_pt_BR.qm',
        ]),
        ('/usr/share/icons/hicolor/16x16/apps', ['linux/hicolor/16x16/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/32x32/apps', ['linux/hicolor/32x32/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/48x48/apps', ['linux/hicolor/48x48/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/128x128/apps', ['linux/hicolor/128x128/apps/pynocchio.png']),
        ('/usr/share/icons/hicolor/256x256/apps', ['linux/hicolor/256x256/apps/pynocchio.png']),
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
        'Programming Language :: Python',
    ],
)
