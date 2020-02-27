import random
from random import randint


print("Hello! Welcome to the Number guessing game")

playAgain = True

while playAgain == True:

    print("Guess a number between 1 and 100!")

    userAnswer = False
    randomNumber = randint(1, 100)

    numTries = 0

    while userAnswer == False:

        userInput = int(input())

        if userInput == randomNumber:

            userAnswer = True

            numTries = numTries + 1

        elif userInput < randomNumber:

            print("Too low!!")

            numTries = numTries + 1
        else:

            print("Too high!!")

            numTries = numTries + 1

    print("Congrats!! You Win!!")
    print("It took you ",numTries, " tries" )
    print("Do you want to play again? Select y or n")

    again = input()

    if again == 'n':

        print("Thanks for playing!")

        break

    


