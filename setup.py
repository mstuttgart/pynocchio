# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pynocchio-comic-reader',
    version='0.0.1',
    packages=['src'],
    url='https://github.com/mstuttgart/pynocchio-comic-reader',
    license='GPL v3',
    author='Michell Stuttgart',
    author_email='michell.stut@gmail.com.br',
    description='Pynocchio Comic Reader is a image viewer specialized in '
                'manga/comic reading.',
    platforms='UNIX',
    requires=['rarfile', 'peewee'],
)