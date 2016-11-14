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

printf "\n---- Start script ----\n"

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

printf "\n---- Run PyInstaller ----\n"
pyinstaller pynocchio.spec

#--------------------------------------------------
# Create the package directory tree to .deb package
#--------------------------------------------------

printf "\n---- Create ${build_deb_folder}/DEBIAN folder ----\n"
mkdir -p ${build_deb_folder}/DEBIAN

printf "\n---- Mount .deb package directory tree ----\n"
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

printf "\n---- Build ${package_name} package ----\n"
dpkg --build ${build_deb_folder}/ ${package_name}

#--------------------------------------------------
# Clean directory
#--------------------------------------------------

printf "\n---- Remove ${build}, ${dist} and ${build_deb_folder} ----\n"
rm -rf ${build}
rm -rf ${dist}
rm -rf ${build_deb_folder}
