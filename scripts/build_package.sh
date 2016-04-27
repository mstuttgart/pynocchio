#!/bin/bash

cd ..
echo
echo "Running PyInstaller"
pyinstaller pynocchio.spec

echo
echo "Copy binary file to linux/usr/bin folder"
cp dist/pynocchio linux/usr/bin

echo
echo "Copy locale file to linux/usr/share/pynocchio"
cp -r pynocchio_comic_reader/locale linux/usr/share/pynocchio

echo
echo "Uninstall pynocchio comic reader from system"
sudo apt-get purge pynocchio -y

echo
echo "Build .deb file"
dpkg --build linux pynocchio-0.0.1-amd64.deb

echo
echo "Install .deb file"
sudo dpkg -i pynocchio-0.0.1-amd64.deb

echo "Remove buind and dist foldere exec file"
rm -rf build dist
rm -rf linux/usr/bin/pynocchio