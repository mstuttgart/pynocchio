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

forms_src="forms"
forms_destiny="pynocchio/uic_files"

resource_src="data"
resource_destiny="pynocchio/uic_files"

#--------------------------------------------------
# Scan directories and scan for .ui and .qrc files
#--------------------------------------------------

printf "\n---- Search by .ui files in ${forms_src} folder ----\n\n"

form_list=$(find -iname *.ui)
printf "${form_list}\n"

printf "\n---- Search by .qrc files in ${resource_src} folder ----\n\n"

resource_list=$(find -iname *.qrc)

printf "${resource_list}\n"

printf "\n---- Compile .ui files. The compiled will be store in \"${forms_destiny}\" folder ----\n\n"

for filename in ${form_list}; do
    pyuic5 --from-imports ${filename} -o ${forms_destiny}/$(basename ${filename} .ui)_ui.py
    if [ $? = 0 ]; then
        printf "Compile ${filename} file successfully!!\n"
    else
        printf "Compile ${filename} file failed!!\n"
    fi
done

printf "\n---- Compile .qrc files.  The compiled will be store in \"${resource_destiny}\" folder ----\n\n"

for filename in ${resource_list}; do
    pyrcc5 ${filename} -o ${resource_destiny}/$(basename ${filename} .qrc)_rc.py
    if [ $? = 0 ]; then
        printf "Compile ${filename} file successfully!!\n"

    else
        printf "Compile ${filename} file failed!!\n"
    fi
done

printf "\n---- Compile .qrc files successfully!! ----\n\n"
