#!/bin/bash

#cd ..
#echo
#echo "Running PyInstaller"
#pyinstaller pynocchio.spec
#
#echo
#echo "Copy binary file to linux/usr/bin folder"
#cp dist/pynocchio linux/usr/bin
#
#echo
#echo "Copy locale file to linux/usr/share/pynocchio"
#cp -r src/locale linux/usr/share/pynocchio
#
#echo
#echo "Uninstall pynocchio comic reader from system"
#sudo apt-get purge pynocchio -y
#
#echo
#echo "Build .deb file"
#dpkg --build linux pynocchio-0.0.1-amd64.deb
#dpkg-sig --sign builder pynocchio-0.0.1-amd64.deb
#
#echo
#echo "Install .deb file"
#sudo dpkg -i pynocchio-0.0.1-amd64.deb
#
#echo "Remove exec file from linux/bin folder"
##rm -rf build dist
#rm -f linux/usr/bin/pynocchio

cd ..
mkdir dist
cp -r pynocchio dist
