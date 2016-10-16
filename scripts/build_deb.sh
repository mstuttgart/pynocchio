#!/usr/bin/env bash

build_deb_folder='pynocchio-deb'

rm -rf ${build_deb_folder}

cd ..
rm -rf ${build_deb_folder}
pyinstaller pynocchio.spec
mkdir -p ${build_deb_folder}/DEBIAN
mkdir -p ${build_deb_folder}/usr/share
mkdir -p ${build_deb_folder}/usr/bin
mkdir -p ${build_deb_folder}/usr/share/pynocchio

cp -r linux/applications ${build_deb_folder}/usr/share/
cp -r linux/hicolor ${build_deb_folder}/usr/share/
cp -r linux/pixmaps ${build_deb_folder}/usr/share/
cp -r pynocchio/locale ${build_deb_folder}/usr/share/pynocchio/

cp dist/* ${build_deb_folder}/usr/bin
cp linux/control ${build_deb_folder}/DEBIAN
cp linux/changelog ${build_deb_folder}/DEBIAN

dpkg --build ${build_deb_folder}/ pynocchio-deb-0.8.0_amd64.deb

rm -rf build
rm -rf dist