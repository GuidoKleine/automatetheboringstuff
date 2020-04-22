#! python3

#bulletPointAdder.py - Adds bulletpoints to copied text

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # loops through lines and adds * at start
text = '\n'.join(lines)

pyperclip.copy(text)
