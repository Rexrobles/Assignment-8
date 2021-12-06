# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

# Greetings
print("Hello! This Program will ask you a three winning number from (0-9)")

import random

#ask input from the user
def ask():
    while True:
        try: 
            FirstNum = int(input("Enter first number (0-9): "))
            if FirstNum not in range(0,9):
                print("Invalid. Input is out of range (0-9)") 
                continue
            SecondNum = int(input("Enter second number (0-9): "))
            if SecondNum not in range(0,9):
                print("Invalid. Input is out of range (0-9)") 
                continue
            ThridNum = int(input("Enter third number (0-9): "))
            if ThridNum not in range(0,9):
                print("Invalid. Input is out of range (0-9)") 
                continue
        except ValueError:
            print("Invalid. Please enter a number.")
            continue
        else:
            break
    List = [FirstNum, SecondNum, ThridNum]
    return List