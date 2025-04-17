import pytest

from src.models.utils import (
    convertStringToBoolean,
    fileExist,
    getBaseName,
    getDirName,
    getFileExtension,
    getParentPath,
    isDir,
    joinPath,
    pathExist,
)


def test_getFileExtension():
    assert getFileExtension("myfile.zip") == ".zip"
    assert getFileExtension("myfile") == ""


def test_getDirName():
    assert getDirName("/home/user/myfile.zip") == "/home/user"
    assert getDirName("myfile") == ""


def test_getBaseName():
    assert getBaseName("/home/user/myfile.zip") == "myfile.zip"
    assert getBaseName("/home/user/myfile") == "myfile"


def test_getParentPath():
    assert getParentPath("/home/user/myfile.zip") == "/home"
    assert getParentPath("/home/user/myfile") == "/home"


def test_joinPath():
    assert joinPath("/home", "user", "myfile.zip") == "/home/user/myfile.zip"
    assert joinPath("/home", "user", "myfile") == "/home/user/myfile"


def test_pathExist():
    assert pathExist("/home") is True
    assert pathExist("/foo") is False


def test_fileExist():
    assert fileExist("LICENSE") is True
    assert fileExist("foo.py") is False


def test_isDir():
    assert isDir("/home") is True
    assert isDir("LICENSE") is False


def test_convertStringToBoolean():
    assert convertStringToBoolean("True") is True
    assert convertStringToBoolean("False") is False
    with pytest.raises(ValueError):
        convertStringToBoolean("true")
