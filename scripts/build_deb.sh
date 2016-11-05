#!/bin/bash
################################################################################
# Script for build of .deb package to Pynocchio Comic Reader
# Author: Michell Stuttgart Faria
#-------------------------------------------------------------------------------
#
# This script will build a .deb package to Pynocchio Comic Reader
#-------------------------------------------------------------------------------
# USAGE:
#
# sh scripts/build_deb.sh
#
################################################################################

echo "\n---- Start script ----"

#--------------------------------------------------
# Define variables
#--------------------------------------------------

package_version=$1
build_deb_folder="build_deb_package"
dist='dist'
build='build'
package_name="pynocchio_${package_version}_amd64.deb"

#--------------------------------------------------
# Create the executable with PyInstaller
#--------------------------------------------------

echo "\n---- Run PyInstaller ----"
pyinstaller pynocchio.spec

#--------------------------------------------------
# Create the package directory tree to .deb package
#--------------------------------------------------

echo "\n---- Create ${build_deb_folder}/DEBIAN folder ----"
mkdir -p ${build_deb_folder}/DEBIAN

echo "\n---- Mount .deb package directory tree ----"
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

echo "\n---- Build ${package_name} package ----"
dpkg --build ${build_deb_folder}/ ${package_name}

#--------------------------------------------------
# Clean directory
#--------------------------------------------------

echo "\n---- Remove ${build}, ${dist} and ${build_deb_folder} ----"
rm -rf ${build}
rm -rf ${dist}
rm -rf ${build_deb_folder}
