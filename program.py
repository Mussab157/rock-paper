#Assignment 1
#PROG10004
#Muhammad Mussab Asif 

#importing the function 'choice' from the 'random' library 
from random import choice

print(" = || 8< = || 8<= || 8< ROCK PAPER SCISSORS = || 8< = || 8<= || 8< ")
print("Welcome to the game of ROCK PAPER SCISSORS")

def gameStart():
    numberOfRounds = 0
    while numberOfRounds <= 1:
        numberOfRounds = int(input("Enter the number of rounds you want to play: "))
    print("May the best one win " + numberOfRounds + "games!")
    