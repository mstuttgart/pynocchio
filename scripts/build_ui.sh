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

echo "\n---- Start script ----"

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

echo "\n---- Search by .ui files in ${forms_src} folder ----\n"

form_list=$(find -iname *.ui)
echo "${form_list}"

echo "\n---- Search by .qrc files in ${resource_src} folder ----\n"

resource_list=$(find -iname *.qrc)
echo "${resource_list}"

echo "\n---- Compile .ui files. The compiled will be store in \"${forms_destiny}\" folder ----\n"

for filename in ${form_list}; do
    pyuic5 --from-imports ${filename} -o ${forms_destiny}/$(basename ${filename} .ui)_ui.py
    if [ $? = 0 ]; then
        echo "Compile ${filename} file successfully!!"
    else
        echo "Compile ${filename} file failed!!"
    fi
done

#echo "\n---- Compile .ui files successfully!! ----\n"

echo "\n---- Compile .qrc files.  The compiled will be store in \"${resource_destiny}\" folder ----\n"

for filename in ${resource_list}; do
    pyrcc5 ${filename} -o ${resource_destiny}/$(basename ${filename} .qrc)_rc.py
    if [ $? = 0 ]; then
        echo "Compile ${filename} file successfully!!"

    else
        echo "Compile ${filename} file failed!!"
    fi
done

echo "\n---- Compile .qrc files successfully!! ----\n"
