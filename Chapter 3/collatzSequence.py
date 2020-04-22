def collatz(number):
    if number % 2 == 0:
        collatzNumber = number // 2
        return collatzNumber
    elif number % 2 == 1:
        collatzNumber = 3 * number + 1
        return collatzNumber

def userInput():
    try:
        print('Enter a number')
        getal = int(input())
                
        extraNumber = collatz(getal)
        print(extraNumber)
    
        while extraNumber != 1:
            extraNumber = collatz(extraNumber)
            if extraNumber == 1:
                print(extraNumber)
                break
            else:
                print(extraNumber)
                continue
    except ValueError:
        print('only a number')
    
userInput()

    
