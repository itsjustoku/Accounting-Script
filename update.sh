#!/bin/bash
apt update
echo -e "\e[1;32;40m"
sleep 1
echo "Updating the script, please wait..."
sleep 1
cd ..
echo "Removing the old files"
sleep 2
rm -r Accounting-Script
sleep 2
echo "Done !"
sleep 2
echo "Installing new files !"
git clone https://github.com/itsjustoku/Accounting-Script.git
sleep 2
echo "Done !"
sleep 1
clear
cd Accounting-Script
echo "Running the script for you :)"
sleep 1
chmod +x FA.py
python3 FA.py
