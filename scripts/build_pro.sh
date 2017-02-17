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

PRO_PATH="i18n"

#--------------------------------------------------
# Scan directories and scan for .ui and .qrc files
#--------------------------------------------------

printf "\n---- Search by .ui files in ${PRO_PATH} folder ----\n\n"

PRO_LIST=$(find -iname *.pro)
printf "${PRO_LIST}\n"

#--------------------------------------------------
# Compile .pro files
#--------------------------------------------------

printf "\n---- Compile .pro files. ----\n\n"

for FILENAME in ${PRO_LIST}; do
    pylupdate5 -verbose ${FILENAME}
    if [ $? = 0 ]; then
        printf "Compile ${FILENAME} file successfully!!\n"
    else
        printf "Compile ${FILENAME} file failed!!\n"
    fi
done

printf "\n---- Compile .pro files successfully!! ----\n\n"