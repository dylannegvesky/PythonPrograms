def addition(x, y):
    return float(x) + float(y)
   
def subtraction(x, y):
    return float(x) - float(y)
    
def multiplication(x, y):
    return float(x) * float(y)
    
def division(x, y):
    return float(x) / float(y)

def negate(x):
    return -float(x)

def modulus(x, y):
    return float(x) % float(y)

def percentage(x):
    return f'{float(x)*100}%'

def exponent(x, y):
    return float(x) ** float(y)

def sqrt(x):
    return float(x) ** (float(1/2))

def menu():
    print('Welcome to Basic Scientific Calculator 2024')
    print('----===================================----')
    print('Please select from the following choices:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Percentage of')
    print('6. Negation')
    print('7. Exponent')
    print('8. Square Root')
    print('9. Modulus (division remainder)')
    print('-1. Exit the Program')
    print('Input the number associated with your choice > ', end='')
    
def main():
    
    userChoice = 0
    
    x = 0
    y = 0
    
    while int(userChoice) != -1:
        menu()
        userChoice = input()
        
        if int(userChoice) == 1:
            x = input('Please input the first value > ')
            y = input('Please input the second value > ')
            sum = addition(x, y)
            print(f'{x} + {y} = {sum}\n')
        elif int(userChoice) == 2:
            x = input('Please input the first value > ')
            y = input('Please input the second value > ')
            difference = subtraction(x, y)
            print(f'{x} - {y} = {difference}\n')
        elif int(userChoice) == 3:
            x = input('Please input the first value > ')
            y = input('Please input the second value > ')
            product = multiplication(x, y)
            print(f'{x} * {y} = {product}\n')
        elif int(userChoice) == 4:
            x = input('Please input the first value > ')
            y = input('Please input the second value > ')
            quotient = division(x, y)
            print(f'{x} / {y} = {quotient}\n')
        elif int(userChoice) == 5:
            x = input('Please input the value > ')
            percent = percentage(x)
            print(f'{x} as a percent is {percent}%\n')
        elif int(userChoice) == 6:
            x = input('Please input the value > ')
            negation = negate(x)
            print(f'The negation of {x} = {negation}\n')
        elif int(userChoice) == 7:
            x = input('Please input the first value > ')
            y = input('Please input the second value > ')
            exp = exponent(x, y)
            print(f'{x} to the {y} power = {exp}\n')
        elif int(userChoice) == 8:
            x = input('Please input the value > ')
            root = sqrt(x)
            print(f'The square root of {x} = {root}\n')
        elif int(userChoice) == 9:
            x = input('Please input the first value > ')
            y = input('Please input the second value > ')
            remainder = modulus(x, y)
            print(f'The remainder of {x} / {y} = {remainder}\n')
        elif userChoice == -1:
            break
        
    print('Thank you for using this calculator!!\n')
    
    
if __name__ == '__main__':
    main()