Pynocchio Comic Reader
==================
Pynocchio is a image viewer specialized in manga/comic reading
developed on PyQt4 API.

![](https://lh3.googleusercontent.com/-NUdXYl_JOjs/VvFn3L812JI/AAAAAAAAFlg/B9ykmSlwcG4OkD6a7x7WoaXW9SZlC-ddwCCo/s1152-Ic42/snapshot4.png)

## Features
The current version is stable and we intend to improve it even more.

* Support several view adjust modes using anti-aliasing.
* Support the several image formates provide by Qt: JPG, PNG, GIF.
* Support a several comic formats like .ZIP, .RAR, .TAR, .CBR, .CBZ and etc
* Elegant visual, free and easy to use.

![](https://lh3.googleusercontent.com/-b9aym21zMx4/VvFn1uNp39I/AAAAAAAAFls/-S0EtcegtHoafXJVLCbz5Rga5zbmI0FqQCCo/s1024-Ic42/snapshot5.png)

## Contributing
If you'd like to contribute, please create a fork and issue pull requests! I am
very open to newcomers, and will need all the help we can get to make the best
comic reader available.

### Dependences
Ludic Game Library makes use of other libraries to perform some of their routines:

* To develop:
* Python 2.7
* PyQT4 and Qt tools (QtDesigner e QLinguist: 
```
sudo apt-get install python-qt4-dev pyqt4-dev-tools python-qt4-sql qt4-designer qt4-linguist-tools qt4-dev-tools unrar python-lxml
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

### I found a bug!
Please report any and all bugs using the project issue
tracker. Be as precise as possible so that the bug can be found easier. Thanks!

### Third party resources
Pynocchio use [Elementary Icon Theme](https://github.com/mstuttgart/elementary3-icon-theme) icon set free pack.

## Credits
Copyright (C) 2014-2015 by Michell Stuttgart Faria
