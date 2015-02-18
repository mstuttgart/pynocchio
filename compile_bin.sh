#!/bin/bash

cp setup.py src/ 
cd src/
python setup.py build
mv -i build/exe.linux-x86_64-2.7 ../bin/
rm -r build
rm setup.py
cd ../
cp -r view/ bin/
cp -r i18n/ bin
