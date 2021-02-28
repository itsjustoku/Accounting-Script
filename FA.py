import os
import sys
import time
from os import system
from time import sleep
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import playsound
except ImportError:
    os.system('pip3 install playsound')

try:
	request = requests.get("https://www.google.com/search?q=accounting", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] No internet connection [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """ 
\033[1;31m                            #   #
\033[1;31m ##### ##### ##### #####     # #   ##### ##### ##### #####
\033[1;31m                           #######                                     
\033[1;31m ##### ##### ##### #####     # #   ##### ##### ##### #####
\033[1;31m                            #   #

\033[1;31m     #      
\033[1;31m    # #    ####   ####   ####  #    # #    # ##### # #    #  #####
\033[1;32m   #   #  #   #  #    # #    # #    # #    #   #   # #    # ##
\033[1;32m  #     # #      #      #    # #    # # #  #   #   # # #  # #
\033[1;32m  ####### #      #      #    # #    # #  # #   #   # #  # # #   ###
\033[1;32m  #     # #    # #    # #    # #    # #   ##   #   # #   ## #     #
\033[1;31m  #     #  ####   ####   ####   ####  #    #   #   # #    # ######

\033[1;33m            ###    ####  #####  # #####  #####
\033[1;33m           #      #    # #    # # #    #   #
\033[1;32m            ###   #      #    # # #    #   #
\033[1;32m              ##  #      #####  # #####    #
\033[1;31m           #   #  #    # #   #  # #        #
\033[1;31m            ###    ####  #    # # #        #
 
 
\033[1;31m                            #   #
\033[1;31m ##### ##### ##### #####     # #   ##### ##### ##### #####
\033[1;31m                           #######
\033[1;31m ##### ##### ##### #####     # #   ##### ##### ##### #####
\033[1;31m                            #   #

\033[1;32m    Created by itsjustoku @Kaku Baruah Copyright ©️ 2021
"""

hprint(G + 'Wait, script is loading...')
sleep(3)
system("clear")
print (logo)
sleep(7)
print ('')
hprint(G + ' Welcoming you to Accounting Script...')
sleep(2)
print ('')
system("clear")
print('')
hprint(G + ' Hey there... please input profit & loss amounts !')
sleep(2)
hprint(G + 'Debit amounts first')
system("clear")
F = input('Furniture =')
DOF = input('Depn. on furniture in amount =')
DF = int(F) - int(DOF)
print (DF)
