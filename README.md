Pynocchio Comic Reader
==================
[![Build Status](https://travis-ci.org/mstuttgart/pynocchio-comic-reader.svg?branch=master)](https://travis-ci.org/mstuttgart/pynocchio-comic-reader)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/pynocchio-comic-reader/badge.svg?branch=master)](https://coveralls.io/github/mstuttgart/pynocchio-comic-reader?branch=master)
[![Code Health](https://landscape.io/github/mstuttgart/pynocchio-comic-reader/master/landscape.svg?style=flat)](https://landscape.io/github/mstuttgart/pynocchio-comic-reader/master)
[![GitHub release](https://img.shields.io/github/release/pynocchio/pynocchio-comic-reader.svg?maxAge=2592000?style=plastic)](https://github.com/pynocchio/pynocchio-comic-reader)
[![AUR](https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000?style=plastic)](https://pt.wikipedia.org/wiki/GNU_General_Public_License)

Pynocchio is a image viewer specialized in manga/comic reading developed on 
PySide API.

![](https://lh3.googleusercontent.com/-p0TtjyX-GgM/VwwYhAAUjrI/AAAAAAAAF04/_JSom_IMmasZfnRn4EPhxKejjj_9aHzYwCCo/s1152-Ic42/snapshot11.png)

### Features

The current version is stable and we intend to improve it even more.

* Support several view adjust modes using anti-aliasing.
* Support the several image formates provide by Qt: JPG, JPEG, PNG, GIF, BMP, PBM, PGM, PPM, XBM, XPM.
* Support a several comic formats like .ZIP, .RAR, .TAR, .CBT, .CBR, .CBZ and etc
* Elegant visual, free and easy to use.

![](https://lh3.googleusercontent.com/-pedd53CIEtc/VwwYg1TpnoI/AAAAAAAAF04/gOJWtN5XZwYwQT_IBwYQEk-sYhqrw_owgCCo/s1152-Ic42/snapshot12.png)

### Install

#### Ubuntu 14.04 and Linux Mint 17.3 (or later)

* To install *stable* version, add this ppa:

```
sudo add-apt-repository ppa:pynocchio-team/pynocchio-stable
sudo apt-get update
sudo apt-get install pynocchio
``` 

* To install *unstable* version, add this ppa:

```
sudo add-apt-repository ppa:pynocchio-team/pynocchio-dev
sudo apt-get update
sudo apt-get install pynocchio
``` 

#### Windows version and others OS

Coming soon! Please help me build packages to the others OS.

### Contributing

If you'd like to contribute, please create a fork and issue pull requests! I am
very open to newcomers, and will need all the help we can get to make the best
comic reader available.

* To compile .ui files, use:

```
python setup.py compile_ui
```

* To compile .qrc files, please use:

```
python setup.py compile_qrc
```
 
* To compile .pro files, please use:

```
python setup.py compile_pro
```

### Dependences

Ludic Game Library makes use of other libraries to perform some of their routines:

* To develop:
* Python 2.7
* PySide and Qt tools (QtDesigner e QLinguist): 

```
sudo apt-get install python-pyside pyside-tools qt4-designer qt4-linguist-tools python-qt4-sql unrar-free
```

* rarfile and peewee: 

```
sudo pip install rarfile peewee
```

You need of Qt Designer to open and edit .ui view files.

### ToDo:

Please, see this [list](https://github.com/mstuttgart/pynocchio-comic-reader/issues/21)

### I found a bug!

Please report any and all bugs using the project issue
tracker. Be as precise as possible so that the bug can be found easier. Thanks!

### Third party resources

Pynocchio use [Elementary Icon Theme](https://github.com/opengraphix/elementary3-icon-theme) icon set free pack.

## Credits

Copyright (C) 2014-2016 by Michell Stuttgart Faria
