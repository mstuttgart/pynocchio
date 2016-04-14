Pynocchio Comic Reader
==================
[![Build Status](https://travis-ci.org/mstuttgart/pynocchio-comic-reader.svg?branch=develop)](https://travis-ci.org/mstuttgart/pynocchio-comic-reader)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/pynocchio-comic-reader/badge.svg?branch=master)](https://coveralls.io/github/mstuttgart/pynocchio-comic-reader?branch=develop)
[![Code Health](https://landscape.io/github/mstuttgart/pynocchio-comic-reader/develop/landscape.svg?style=flat)](https://landscape.io/github/mstuttgart/pynocchio-comic-reader/develop)
[![Project Status](https://img.shields.io/badge/status-development-yellow.svg)](https://github.com/mstuttgart/pynocchio-comic-reader/tree/develop)
[![AUR](https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000?style=plastic)](https://pt.wikipedia.org/wiki/GNU_General_Public_License)

Pynocchio is a image viewer specialized in manga/comic reading
developed on PySide API.

![](https://lh3.googleusercontent.com/-p0TtjyX-GgM/VwwYhAAUjrI/AAAAAAAAF04/_JSom_IMmasZfnRn4EPhxKejjj_9aHzYwCCo/s1152-Ic42/snapshot11.png)

## Features
The current version is stable and we intend to improve it even more.

* Support several view adjust modes using anti-aliasing.
* Support the several image formates provide by Qt: JPG, PNG, GIF.
* Support a several comic formats like .ZIP, .RAR, .TAR, .CBR, .CBZ and etc
* Elegant visual, free and easy to use.

![](https://lh3.googleusercontent.com/-pedd53CIEtc/VwwYg1TpnoI/AAAAAAAAF04/gOJWtN5XZwYwQT_IBwYQEk-sYhqrw_owgCCo/s1152-Ic42/snapshot12.png)

## Contributing
If you'd like to contribute, please create a fork and issue pull requests! I am
very open to newcomers, and will need all the help we can get to make the best
comic reader available.

### Dependences
Ludic Game Library makes use of other libraries to perform some of their routines:

* To develop:
* Python 2.7
* PySide and Qt tools (QtDesigner e QLinguist): 
```
sudo apt-get install python-pyside pyside-tools python-qt4-sql qt4-designer 
qt4-linguist-tools qt4-dev-tools unrar
```
* rarfile: 
```
sudo pip install rarfile
```
* peewee: 
```
sudo pip install peewee
```

* To use Pynocchio, you must only install *rarfile* and *peewee* modules.

You need of Qt Designer to open and edit .ui view files.
Use de **compile_ui.sh** file to compile views of project.

### Download
In this moment, only Linux version is avaliable:

[pynocchio-comic-reader-beta.deb]()

Obs.: Please, don't forget to install *rarfile* and *peewee* Python modules.

```
sudo pip install peewee rarfile
```

### TODO:
[TODO list](https://github.com/mstuttgart/pynocchio-comic-reader/issues/21)

### I found a bug!
Please report any and all bugs using the project issue
tracker. Be as precise as possible so that the bug can be found easier. Thanks!

### Third party resources
Pynocchio use [Elementary Icon Theme](https://github.com/mstuttgart/elementary3-icon-theme) icon set free pack.

## Credits
Copyright (C) 2014-2016 by Michell Stuttgart Faria
