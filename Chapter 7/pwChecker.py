#! python3
# pwChecker.py - Checks the strength of a password

import re

password = input('Please fill in a password to check its strength \n')

def passwordCheck(pw):
    lengthRegex = re.compile(r'\w{8,}')
    lowerRegex = re.compile(r'[a-z]+')
    upperRegex = re.compile(r'[A-Z]+')
    digitRegex = re.compile(r'[0-9]+')

    mo = lengthRegex.search(pw)
    if mo != None:
        print('Password is longer than 8 characters')
        mo = lowerRegex.search(pw)

        if mo != None:
            print('Password containts lowercase')
            mo = upperRegex.search(pw)

            if mo != None:
                print('Password contains uppercase')
                mo = digitRegex.search(pw)

                if mo != None: 
                    print('Password contains digit')
                    print('ACCEPTED')
                
                else:
                    print('Password needs to contain NUMBERS')
            else:
                print('FAULT Password needs to contain UPPERCASE')
        else:
            print('FAULT Passwords needs to contain LOWERCASE')
    else:
        print('FAULT Password is not LONG enough')


passwordCheck(password)

    
 


