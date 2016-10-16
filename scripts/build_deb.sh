#!/usr/bin/env bash

package_version=$1
build_deb_folder="build_deb_package"
dist='dist'
build='build'
package_name="pynocchio_${package_version}_amd64.deb"

pyinstaller pynocchio.spec

mkdir -p ${build_deb_folder}/DEBIAN
mkdir -p ${build_deb_folder}/usr/share
mkdir -p ${build_deb_folder}/usr/bin
mkdir -p ${build_deb_folder}/usr/share/pynocchio

cp -r linux/applications ${build_deb_folder}/usr/share/
cp -r linux/hicolor ${build_deb_folder}/usr/share/
cp -r linux/pixmaps ${build_deb_folder}/usr/share/
cp -r pynocchio/locale ${build_deb_folder}/usr/share/pynocchio/

cp ${dist}/* ${build_deb_folder}/usr/bin
cp linux/control ${build_deb_folder}/DEBIAN
cp linux/changelog ${build_deb_folder}/DEBIAN

dpkg --build ${build_deb_folder}/ ${package_name}

rm -rf ${build}
rm -rf ${dist}
rm -rf ${build_deb_folder}
