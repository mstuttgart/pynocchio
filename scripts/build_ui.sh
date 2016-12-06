#!bin/bash
################################################################################
# Script for build ui and qrc files to Pynocchio Comic Reader
# Author: Michell Stuttgart Faria
#-------------------------------------------------------------------------------
#
# This script will build a .ui and .qrc files to Pynocchio Comic Reader
#-------------------------------------------------------------------------------
# USAGE:
#
# sh scripts/build_ui.sh
#
################################################################################

printf "\n---- Start script ----\n"

#--------------------------------------------------
# Define variables
#--------------------------------------------------

PACKAGE_VERSION=$1
HTML_FOLDER="data/others/about.html"
FORMS_SRC="forms"
FORMS_DESTINY="pynocchio/uic_files"

RESOURCE_SRC="data"
RESOURCE_DESTINY="pynocchio/uic_files"

#--------------------------------------------------
# Scan directories and scan for .ui and .qrc files
#--------------------------------------------------

# Change package version in html about file
sed -i -e "s:<h1>Pynocchio *.*.*</h1>:<h1>Pynocchio ${PACKAGE_VERSION}</h1>:g" ${HTML_FOLDER}

printf "\n---- Search by .ui files in ${FORMS_SRC} folder ----\n\n"

FORM_LIST=$(find -iname *.ui)
printf "${FORM_LIST}\n"

printf "\n---- Search by .qrc files in ${RESOURCE_SRC} folder ----\n\n"

RESOURCE_LIST=$(find -iname *.qrc)

printf "${RESOURCE_LIST}\n"

printf "\n---- Compile .ui files. The compiled will be store in \"${FORMS_DESTINY}\" folder ----\n\n"

for FILENAME in ${FORM_LIST}; do
    pyuic5 --from-imports ${FILENAME} -o ${FORMS_DESTINY}/$(basename ${FILENAME} .ui)_ui.py
    if [ $? = 0 ]; then
        printf "Compile ${FILENAME} file successfully!!\n"
    else
        printf "Compile ${FILENAME} file failed!!\n"
    fi
done

printf "\n---- Compile .qrc files.  The compiled will be store in \"${RESOURCE_DESTINY}\" folder ----\n\n"

for FILENAME in ${RESOURCE_LIST}; do
    pyrcc5 ${FILENAME} -o ${RESOURCE_DESTINY}/$(basename ${FILENAME} .qrc)_rc.py
    if [ $? = 0 ]; then
        printf "Compile ${FILENAME} file successfully!!\n"

    else
        printf "Compile ${FILENAME} file failed!!\n"
    fi
done

printf "\n---- Compile .qrc files successfully!! ----\n\n"
