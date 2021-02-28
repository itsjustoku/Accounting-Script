#!/usr/local/bin
apt update
color 0a
sleep(1)
echo "Updating the script, please wait..."
sleep(1)
git clone https://github.com/itsjustoku/Accounting-Script.git
sleep(1.5)
echo "Done !"
sleep(1.5)
echo "Running the script for you :)"
sleep(1)
python3 FA.py
