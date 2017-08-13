#!/bin/bash
################################################################################
# Script for build ui and qrc files to Pynocchio Comic Reader
# Author: Michell Stuttgart
#-------------------------------------------------------------------------------
#
# This script will build a .ui and .qrc files to Pynocchio Comic Reader
#-------------------------------------------------------------------------------
# USAGE:
#
# ./scripts/build_ui.sh [version] or python setup.py build_ui
#
################################################################################

#--------------------------------------------------
# Define variables
#--------------------------------------------------

export Off=$'\e[0m'
export White=$'\e[1;37m'
export BlueBG=$'\e[1;44m'
export Yellow=$'\e[1;33m'

echo -e ""
echo -e " ${White}${BlueBG}                                                         ${Off}"
echo -e " ${White}${BlueBG}         -= Build .ui and .qrc files =-                  ${Off}"
echo -e " ${White}${BlueBG}                                                         ${Off}"
echo -e ""

PACKAGE_VERSION=$1
HTML_FOLDER="data/others/about.html"
FORMS_SRC="forms"
FORMS_DESTINY="pynocchio/uic_files"

RESOURCE_SRC="data"
RESOURCE_DESTINY="pynocchio/uic_files"

#--------------------------------------------------
# Scan directories and scan for .ui and .qrc files
#--------------------------------------------------

echo -e ""
echo -e "${Yellow} Update Pynocchio version to ${White}${PACKAGE_VERSION}"
echo -e "${Yellow} =-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ${Off}"
echo -e "${White}"

# Change package version in html about file
sed -i -e "s:<h1>Pynocchio *.*.*</h1>:<h1>Pynocchio ${PACKAGE_VERSION}</h1>:g" ${HTML_FOLDER}

echo -e ""
echo -e "${Yellow} Search by .ui files in ${FORMS_SRC} folder"
echo -e "${Yellow} =-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ${Off}"
echo -e "${White}"

FORM_LIST=$(find -iname *.ui)

echo -e "${White}${FORM_LIST}"
echo -e ""

echo -e "${Yellow} Search by .qrc files in ${RESOURCE_SRC} folder"
echo -e "${Yellow} =-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ${Off}"
echo -e "${White}"

RESOURCE_LIST=$(find -iname *.qrc)

echo -e "${White}${RESOURCE_LIST}"
echo -e ""

echo -e "${Yellow} Compile .ui files. The compiled will be store in \"${FORMS_DESTINY}\" folder"
echo -e "${Yellow} =-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ${Off}"
echo -e "${White}"

for FILENAME in ${FORM_LIST}; do
    pyuic5 --from-imports ${FILENAME} -o ${FORMS_DESTINY}/$(basename ${FILENAME} .ui)_ui.py
    if [ $? = 0 ]; then
        echo -e "${White} [OK] Compile ${FILENAME}"
    else
        echo -e "${White} [ERROR] Compile ${FILENAME}"
    fi
done

echo -e ""
echo -e "${Yellow} Compile .qrc files.  The compiled will be store in \"${RESOURCE_DESTINY}\" folder"
echo -e "${Yellow} =-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ${Off}"
echo -e "${White}"

for FILENAME in ${RESOURCE_LIST}; do
    pyrcc5 ${FILENAME} -o ${RESOURCE_DESTINY}/$(basename ${FILENAME} .qrc)_rc.py
    if [ $? = 0 ]; then
        echo -e "${White} [OK] Compile ${FILENAME}"
    else
        echo -e "${White} [ERROR] Compile ${FILENAME}"
    fi
done

echo -e ""
