def decimal2Binary(decimal):
    binary = list()
    remainder = ''
    index = -1
    
    print(f'\nThe decimal number {decimal} = ', end='')
    
    while int(decimal) != 0:
        remainder = int(decimal) % 2
        binary.append(int(remainder))
        
        decimal = int(decimal) / 2
        index += 1
    
    while int(index) >= 0:
        print(binary[index], end='')
        index -= 1
        
    print(' in binary.', end='')
    
def decimal2Hex(decimal):
    hexFinal = list()
    hexRep = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    remainder = ''
    index = -1
    
    print(f'\nThe decimal number {decimal} = ', end='')
    
    while int(decimal) != 0:
        remainder = int(decimal) % 16
        hexFinal.append(int(remainder))
        
        decimal = int(decimal) / 16
        index += 1
        
    while int(index) >= 0:
        print(hexRep[hexFinal[index]], end='')
        index -= 1
        
    print(' in hexadecimal.', end='')
        
    
def menuOptions():
    print('\n')
    for i in range(0, 30):
        print('*', end='')
    print('\n' + '{:-^30}'.format(' Decimal Converter '))
    for i in range(0, 30):
        print('*', end='')
    print('\n\nPlease select which base you would like to convert to: ')
    print('1. Binary')
    print('2. Hexadecimal')
    print('3. Both Binary and Hexadecimal')
    print('Input your selection (1-3) here > ', end='')
    
def main():
    userContinue = True

    while userContinue == True:
        menuOptions()
        userChoice = input()
        
        if userChoice.isdigit() != 1:
            print('You have printed a non-number, try again...')
            continue
        
        decimal = input('Please input your decimal number here > ')
        
        if int(userChoice) == 1:
            decimal2Binary(int(decimal))
        elif int(userChoice) == 2:
            decimal2Hex(int(decimal))
        elif int(userChoice) == 3:
            decimal2Binary(decimal)
            decimal2Hex(decimal)
        elif int(userChoice) > 3 or int(userChoice) < 1:
            print('That selection was invalid... Try again.')
    
    
if __name__ == '__main__':
    main()
    