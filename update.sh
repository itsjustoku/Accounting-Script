#!/bin/bash
apt update
echo -e "\e[1;32;40m"
sleep 1
echo "Updating the script, please wait..."
sleep 1
cd ..
echo "Removing tbe old files"
sleep 1.5
rm -r Accounting-Script
sleep 1.5
echo "Done !"
sleep 2
echo "Installing new files !"
git clone https://github.com/itsjustoku/Accounting-Script.git
sleep 2
echo "Done !"
sleep 1
cd Accounting-Script
echo "Running the script for you :)"
sleep 1
chmod +x FA.py
chmod +x update.sh
python3 FA.py
