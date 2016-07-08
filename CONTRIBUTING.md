### Contributing

If you'd like to contribute, please create a fork and issue pull requests! I am
very open to newcomers, and will need all the help we can get to make the best
comic reader available.

Ps: please, make your work on `develop` branch and send your pull request to `develop`branch to.

Fork this repo and make a git clone with follow command:

```bash
git clone --recursive https://github.com/youusername/pynocchio-comic-reader.git
```

Pynocchio Comic Reader makes use of follow dependences:

* To develop:
* Python 2.7
* PySide and Qt tools (QtDesigner e QLinguist):

```bash
sudo apt-get install python-pyside pyside-tools qt4-designer qt4-linguist-tools qt4-dev-tools libqt4-sql-sqlite unrar-free
```

* rarfile and peewee:

```bash
sudo pip install rarfile peewee
```

* To compile .ui and qrc files, please first install [pyqt_distutils](https://github.com/ColinDuquesnoy/pyqt_distutils) module:

```bash
sudo pip install pyqt-distutils
```

You need of Qt Designer to open and edit .ui view files and QtLinguist to
translate .ts files.

To compile .ui and qrc files, please first install pyqt_distutils module:

```bash
python setup.py build_ui
```

* To compile .pro files, please use:

```bash
python setup.py build_pro
```

New .ui files must be added in `pyuic.json` file.

#### Run Pynocchio
 To run pynocchio, only double-click in `pynocchio_run`, run `./pynocchio_run` or `python pynocchio_run`.

### To Do list:

Please, see this [list](https://github.com/mstuttgart/pynocchio-comic-reader/issues/21).

### I found a bug!

Please report any and all bugs using the project issue
tracker. Be as precise as possible so that the bug can be found easier. Thanks!
