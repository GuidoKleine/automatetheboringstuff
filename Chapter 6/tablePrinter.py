tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def checkLength(printableTable):
    colWidths = [0] * len(printableTable)
    loops = -1

    # Loops through 'tableData' list
    for i in range(len(printableTable)):
        loops += 1
        longestValue = 0
        printList = printableTable[i]
        #Loops through every list in tableData
        for j in printList:
            checkValue = len(j)
            #Checks for longest value in each list
            if checkValue > longestValue:
                longestValue = checkValue
        #puts the longest values of each list in colWidths
            colWidths[loops] = longestValue
    return colWidths

        
def printTable(tableData):
    colWidths = checkLength(tableData)

    #Print the appropiated value of each column in a row
    for i in range(len(tableData[0])):
        x=''
        for j in range(len(tableData)):
            x = x + ' ' + str(tableData[j][i]).rjust(colWidths[j])
        print(x)
    
printTable(tableData)



              
    

