#! python3
# madLibs.py reads textfiles and searches for the words ADJECTIVE,
# NOUN, ADVERB, or VERB and replaces it with a user chosen word

import re

# read text file, put text in string
searchFile = open('madLibs_text.txt')
content = searchFile.read()
searchFile.close()

# searches for words ADJECTIVE, NOUN, ADVERB, or VERB
regex = re.compile(r'([A-Z]{2,})')
wordList = regex.findall(content)

# Ask user to replace them
for word in wordList: 
    changeWord = input('Enter an ' + word.lower() + ':\n')
    content = content.replace(word, changeWord, 1)

# Write new content to file
newFile = open('madLibs_new.txt', 'w')
newFile.write(content)
newFile.close()

