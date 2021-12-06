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

# generating three random winning numbers
def get3WinningNum():
    W_Num1, W_num2, W_Num3 = random.sample(range(0, 9), 4)
    Winning_list = [W_Num1, W_num2, W_Num3]
    return Winning_list

# Win or Lose
def checkWinLose(list1, list2):
    if sorted(list1) == sorted(list2):
        print("Winner!")
    else: 
        print("You loss!")
        
# start the game
def play():
    print("Welcome to the Lottery!")
    # asks user 3 numbers and generates 3 winning numbers
    inputNums = ask()
    winningNums = get3WinningNum()
    # dislay user input and winning numbers
    print(f"Your guesses: {inputNums} Winning numbers: {winningNums}")
    # Show Result
    print("RESULT") 
    checkWinLose(inputNums, winningNums)
   
# asks user to play again
def playAgain():
    while True:
        yn = input("Try again? y/n: ")
        yn = yn.lower()
        if yn == 'y':
            print("n")
            play()
        elif yn == 'n':
            print("Bye player!")
            break
        else:
            print("n")
            print("Please enter y if you want to play again, or enter n to exit the game.")

# main
play()
playAgain()