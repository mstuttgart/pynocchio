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

PACKAGE_VERSION=$1
BUILD_DEB_FOLDER="build_deb_package"
DIST='dist'
BUILD='build'
PACKAGE_NAME="pynocchio_${PACKAGE_VERSION}_amd64.deb"

#--------------------------------------------------
# Create the executable with PyInstaller
#--------------------------------------------------

printf "\n---- Run PyInstaller ----\n"
pyinstaller pynocchio.spec

#--------------------------------------------------
# Create the package directory tree to .deb package
#--------------------------------------------------

printf "\n---- Create ${BUILD_DEB_FOLDER}/DEBIAN folder ----\n"
mkdir -p ${BUILD_DEB_FOLDER}/DEBIAN

printf "\n---- Mount .deb package directory tree ----\n"
mkdir -p ${BUILD_DEB_FOLDER}/usr/share
mkdir -p ${BUILD_DEB_FOLDER}/usr/bin
mkdir -p ${BUILD_DEB_FOLDER}/usr/share/pynocchio

cp -r linux/applications ${BUILD_DEB_FOLDER}/usr/share/
cp -r linux/hicolor ${BUILD_DEB_FOLDER}/usr/share/
cp -r linux/pixmaps ${BUILD_DEB_FOLDER}/usr/share/
cp -r pynocchio/locale ${BUILD_DEB_FOLDER}/usr/share/pynocchio/

cp ${DIST}/* ${BUILD_DEB_FOLDER}/usr/bin
cp linux/control ${BUILD_DEB_FOLDER}/DEBIAN

printf "\n---- Build ${PACKAGE_NAME} package ----\n"
dpkg --build ${BUILD_DEB_FOLDER}/ ${PACKAGE_NAME}

#--------------------------------------------------
# Clean directory
#--------------------------------------------------

printf "\n---- Remove ${BUILD}, ${DIST} and ${BUILD_DEB_FOLDER} ----\n"
rm -rf ${BUILD}
rm -rf ${DIST}
rm -rf ${BUILD_DEB_FOLDER}
