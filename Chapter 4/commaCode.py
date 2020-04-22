def changelist():
    newList = []
    print('Enter a item for the list or enter nothing when done')

    while True:
        item = input()
        if item == '':
            break
        newList = newList + [item]

    strItem = ''
    
    for item in newList:
        if strItem == '':
            strItem = str(item)
        else:
            strItem = strItem + ', ' + str(item)
    
    print(strItem)
    
changelist()

