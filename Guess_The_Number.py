# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

# greetings to the user
print ("This program will generate a random number from 0 to 100.")

# code to generate random number from 0-100
from random import randrange
randomNum = randrange(0, 100)

Guess = int(input("Please Enter your guess here: "))

# code block that will ask user repeatedly until the random number guess correctly
while randomNum != Guess:
    if Guess > randomNum:
        Guess = int(input("Your guess is greater than the number. Try decreasing your input number. Please Enter your guess here: "))
        if Guess == randomNum:
            break
    
        
