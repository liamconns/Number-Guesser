import random
from random import randint


print("Hello! Welcome to the Number guessing game")

playAgain = True

while playAgain == True:

    print("Guess a number between 1 and 100!")

    userAnswer = False
    randomNumber = randint(1, 100)


    while userAnswer == False:

        userInput = int(input())

        if userInput == randomNumber:

            userAnswer = True

        elif userInput < randomNumber:

            print("Too low!!")

        else:

            print("Too high!!")

    print("Congrats!! You Win")
    print("Do you want to play again? Select y or n")

    again = input()

    if again == 'n':

        print("Thanks for playinG!")

        break

    


