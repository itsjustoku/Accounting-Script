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
hprint(G + 'Welcoming you to Accounting Script...')
sleep(2)
print ('')
system("clear")
print('')
hprint(G + 'Hey there, what is your name ?')
name = input('Name:- ')
sleep(1)
hprint(G + 'Nice to meet you,' +name)
sleep(1)
hprint(G + 'So you want to me solve your problems !')
sleep(1)
hprint(G + 'Cool, let us continue then')
sleep(1)
hprint(G + 'Enter profit & loss debit amounts')
sleep(1)
system("clear")
F = input('Furniture = ')
DOF = input('Depn. on furniture in amount = ')
DF = int(F) - int(DOF)
sleep(1)
M = input('Machinery = ')
DOM = input('Depn. on machinery in amount = ')
DM = int(M) - int(DOM)
sleep(1)
S = input('Salary = ')
sleep(1)
IP = input('Insurance Premium = ')
sleep(1)
PDD = input('Provision for bad debts = ')
sleep(1)
NP = input('New Provision = ')
sleep(1)
BD = input('Bad Debts = ')
sleep(1)
OP = input('Old Provision = ')
sleep(1)
TP = PDD + NP + BD #Total Provision including Bad Debts
RP = int(TP) - int(OP) #Remaining Provision
sleep(1)
system("clear")
R = input('Rent = ')
sleep(1)
BC = input('Bank Charge = ')
sleep(1)
CO = input('Carriage Outward = ')
sleep(1)
DR = DF + DM + S + IP + RP + R + BC + CO #Total Debit
sleep(1)
hprint(G + 'Good, now profit & loss credit amounts !')
sleep(1)
system("clear")
TA = input('Trading Account = ')
BDR = input('Bad Debt Recovered = ')
sleep(1)
SR = input('Sundry Receipts = ')
sleep(1)
C = input('Commission = ')
sleep(1)
CR = TA + BDR + SR + C #Total Credit
sleep(3)
system("clear")
hprint(G + 'Well done, let me calculate the net profit')
if (DR > CR):
     NP = int(DR) - int(CR)
     sleep(1)
     print('The net profit is = ' +NP)
elif(CR > DR):
     NP = int(CR) - int(DR)
     sleep(1)
     print('The net loss is = ' +NP)
elif(DR == CR):
     print('There is neither profit nor loss')
else:
     print('Error in calculating')
sleep(1)
hprint(G + 'Thank you for using Accounting Script')
print('')
hprint(G + 'Have a good day ahead !')
