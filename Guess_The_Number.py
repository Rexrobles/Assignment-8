# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

# greetings to the user
print ("\033[1m\033[94mThis program will generate a random number from 0 to 100.\033[0m")

# code to generate random number from 0-100
from random import randrange
randomNum = randrange(0, 100)

Guess = int(input("\033[1m\033[92mPlease Enter your guess here: \033[0m"))

# code block that will ask user repeatedly until the random number guess correctly
while randomNum != Guess:
    if Guess > randomNum:
        Guess = int(input("Your guess is \033[93mGreater than\033[0m the number. Try \033[93mDecreasing\033[0m your input number.\033[1m\033[92mPlease Enter your guess here: \033[0m"))
        if Guess == randomNum:
            break
    elif Guess < randomNum:
        Guess = int(input("Your guess is \033[93mLess than\033[0m the number. Try \033[93mincreasing\033[0m your  input number.\033[1m\033[92mPlease Enter your guess here: \033[0m"))
        if Guess == randomNum:
            break
        
# calling the variables if the user guessed the number correctly
if Guess == randomNum:
    print (f"\033[1m\033[92mYou're Guess the correct Number!\033[0m The answer is \033[97m{randomNum}\033[0m.")