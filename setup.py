# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pynocchio-comic-reader',
    version='beta',
    packages=['test', 'test.lib',
              'test.lib.custom_widgets', 'pynocchio_comic_reader',
              'pynocchio_comic_reader.lib',
              'pynocchio_comic_reader.lib.uic_files',
              'pynocchio_comic_reader.lib.uic_files.custom_widgets'],
    test_suite='test',
    url='https://github.com/mstuttgart/pynocchio-comic-reader#'
        'pynocchio-comic-reader',
    license='GPL v3',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    description='Pynocchio is a image viewer specialized in manga/comic '
                'reading developed on PySide API.'
)
