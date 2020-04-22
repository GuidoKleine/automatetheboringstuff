#! python3
# selectiveCopy.py - searches for specific file extension in folder and copies
# these to different location

import os, shutil, re

def copyFileExtension(folderSource, folderDestination):
    
    sourceFolder = os.path.abspath(folderSource)
    destinationFolder = os.path.abspath(folderDestination)
    
    fileExtension = input('Fill in the file extension you want to search pdf\doc\jpeg etc:\n')

    # compile regex for specific file extension
    searchExtRegex = re.compile(r'([_a-zA-Z0-9]*).' + fileExtension)

    # search files through folder
    for foldername, subfolder, filename in os.walk(sourceFolder):
        for file in filename:
            newPath = os.path.join(sourceFolder, file)
            if searchExtRegex.search(file):           
    # TODO: files to specific destination
                print('moving file: ' + file + ' from ' + sourceFolder + ' to ' + destinationFolder)
                #shutil.copy(newPath, destinationFolder)
            

    

copyFileExtension('C:\\delicious', 'C:\\terrible')
