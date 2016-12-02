#!bin/bash
################################################################################
# Script for build pro files to Pynocchio Comic Reader
# Author: Michell Stuttgart Faria
#-------------------------------------------------------------------------------
#
# This script will build a .pro files to Pynocchio Comic Reader
#-------------------------------------------------------------------------------
# USAGE:
#
# sh scripts/build_pro.sh
#
################################################################################

printf "\n---- Start script ----\n"

#--------------------------------------------------
# Define variables
#--------------------------------------------------

pro_path="i18n"
forms_destiny="pynocchio/uic_files"

#--------------------------------------------------
# Scan directories and scan for .ui and .qrc files
#--------------------------------------------------

printf "\n---- Search by .ui files in ${pro_path} folder ----\n\n"

pro_list=$(find -iname *.pro)
printf "${pro_list}\n"

#--------------------------------------------------
# Compile .pro files
#--------------------------------------------------

printf "\n---- Compile .pro files. ----\n\n"

for filename in ${pro_list}; do
    /usr/lib/x86_64-linux-gnu/qt5/bin/lupdate -verbose ${filename}
    if [ $? = 0 ]; then
        printf "Compile ${filename} file successfully!!\n"
    else
        printf "Compile ${filename} file failed!!\n"
    fi
done

printf "\n---- Compile .pro files successfully!! ----\n\n"