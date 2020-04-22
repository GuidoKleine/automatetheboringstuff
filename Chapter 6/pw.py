#! python3
# pw.py - An insecure password locker program.

Passwords = {'email': '754Sidk87dEids@%od(8',
             'blog': 'ajk#9d)37d92FGJid7*dd',
             'luggage': '15796'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in Passwords:
    pyperclip.copy(Passwords[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' +  account)
