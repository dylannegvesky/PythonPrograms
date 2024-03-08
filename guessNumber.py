import random

# Generate a random number by choosing from a list sent to function
def generateNum(range):
    randomNum = random.choice(range)
    return randomNum

def main():
    # Initialize a list with range 0-100
    numRange = list(range(100))
    
    numGuesses = 0
    userCont = True
    inputValid = False
    
    print("\nYou will have 5 guesses to correctly locate the magic number (1-100)...")
    while userCont == True:
        # Set magicNum = a random number from above list
        magicNum = generateNum(numRange)
        while numGuesses <= 4:
            userGuess = input(f"\nPlease enter guess #{numGuesses + 1} > ")
            userGuess = int(userGuess)
        
            if userGuess < magicNum:
                print('That guess is too low... Try again!')
            elif userGuess > magicNum:
                print('That guess is too high... Try again!')
            elif userGuess == magicNum:
                print('That is CORRECT!!!')
                break
            
            numGuesses += 1
        
        if numGuesses >= 5:
            print("Sorry, you did not find the magic number...")
        
        numGuesses = 0
        
        while inputValid == False:
            tOrF = input("\nWould you like to try again? Input T or F > ")
            
            if tOrF == 't' or tOrF == 'T':
                userCont = True
                inputValid == True
                break
            elif tOrF == 'f' or tOrF == 'F':
                userCont = False
                inputValid == True
                break
            else:
                print("That is not a valid input...")
                inputValid == False
        

    
if __name__ == '__main__':
    main()