# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys

from codecs import open

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'pynocchio',
                            '__version__.py')

about = {}
with open(version_path, 'r') as f:
    exec(f.read(), about)

if sys.argv[-1] == 'build_deb':
    os.system('./scripts/build_ui.sh %s' % about['__version__'])
    os.system('./scripts/build_deb.sh %s' % about['__version__'])
    sys.exit()

if sys.argv[-1] == 'build_ui':
    os.system('./scripts/build_ui.sh %s' % about['__version__'])
    sys.exit()

if sys.argv[-1] == 'build_pro':
    os.system('./scripts/build_pro.sh')
    sys.exit()

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'version %s'" % (about['__version__'],
                                                 about['__version__']))
    os.system("git push --tags")
    sys.exit()

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    description=about['__description__'],
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
