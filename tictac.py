#!/usr/bin/env python3

## Tic Tac Toe Game ##
import os
import time
import random
import sys

#Define the board 
board = [""," "," "," "," "," "," "," "," "," "]

# Header for displayed above the board
def tictacHeader(): 
    print("""

Welcome to Tic Tac Toe      
To Play Tic Tac Toe, you need to get three in a row
Your choices are defined, they must be from 1 to 9
   
1|2|3
4|5|6
7|8|9

    """)

# Define the print board function
def ticBoard(): 
    print("  |  |  ") 
    print(""+board[1]+" |"+board[2]+" | "+board[3]+" ")
    print("--|--|--")
    print("  |  |  ") 
    print(""+board[4]+" |"+board[5]+" | "+board[6]+" ")
    print("--|--|--")
    print("  |  |  ") 
    print(""+board[7]+" |"+board[8]+" | "+board[9]+" ")
    print("  |  |  ") 
    print(" ")

# Clear board and print it back to screen
def ticClear(): 
    os.system("clear")
    tictacHeader()
    ticBoard()


winVal = "X" or "0"
# Defines the logic for winning in the world's most exciting game
def checkWin():
        if (board[1] == winVal and board[2] == winVal and board[3] == winVal) or \
            (board[4] == winVal and board[5] == winVal and  board[6] == winVal) or \
            (board[7] == winVal and  board[8] == winVal and  board[9] == winVal) or \
            (board[1] == winVal and  board[4] == winVal and  board[7] == winVal) or \
            (board[2] == winVal and  board[5] == winVal and  board[8] == winVal) or \
            (board[3] == winVal and  board[6] == winVal and  board[9] == winVal) or \
            (board[1] == winVal and  board[5] == winVal and  board[9] == winVal) or \
            (board[3] == winVal and  board[5] == winVal and  board[7] == winVal):
            if winVal == "X":
                ticClear()
                print("Congratulations X, you won the game!")
                playAgain()
            elif winVal == "0":
                ticClear()
                print("Congratulations 0, you won the game!")
                playAgain()
        else:
            ticClear()

# Restarts the game
def playAgain():
    print("would you like to play again? Y/N :")
    playAgainx  = input()
    if playAgainx.lower() in ["y","yes"]:
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif playAgainx.lower() in ["n", "no"]:
        sys.exit()
    else:
        print("invalid input")
        playAgain()

# Outputs turn to index in the main string to be printed on the board
def turn0():
    print("Please choose and empty space for 0: ")
    choice0 = int(input())
    if board[choice0] == " ":
        board[choice0] = "0"
    else:
        print("Sorry, that space is not empty")
        turn0()

# Outputs turn to index in the main string to be printed on the board
def turnX():
    print("Please choose an empty space for X: ")
    choiceX = int(input())
    if board[choiceX] == " ":
        board[choiceX] = "X"
    else:
        print("Sorry, that space is not empty")
        turnX()

# Checks to see if the board is full
def isFull():
    if " " in board:
        checkWin()
        turn0()
    else:
        checkWin()
        print("Tie Game!")
        playAgain()

while True:
    checkWin()
    turnX()
    isFull()



