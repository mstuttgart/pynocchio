#!/bin/bash

echo "Preparing..."
cp setup.py src/ 
cd src/
echo "Build python files..."
python setup.py build
echo "\nMoving binary files to bin folder"
rm -r ../bin/*
mv -f build/exe.linux-x86_64-2.7 ../bin/
rm -r build
rm setup.py
cd ../
echo "Moving ui files to bin folder"
cp -r view/ bin/
echo "Moving translation files to bin folder"
cp -r i18n/ bin

echo "Get the binary in the bin/exe.linux-x86_64-2.7 folder"
