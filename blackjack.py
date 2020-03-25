#!/usr/bin/python3

import os
import sys
import math 
import random

cards = [
         '1','1','1','1',
         '2','2','2','2', 
         '3','3','3','3',  
         '4','4','4','4',  
         '5','5','5','5',  
         '6','6','6','6', 
         '7','7','7','7',  
         '8','8','8','8', 
         '9','9','9','9', 
         'J','J','J','J',  
         'Q','Q','Q','Q',  
         'K','K','K','K',
         'A','A','A','A',  
        ] 

random.shuffle(cards)
    
dealerCards = []
playerCards = []

def start():
   
    playerCards.append(cards.pop())
    dealerCards.append(cards.pop()) 
    playerCards.append(cards.pop())
    dealerCards.append(cards.pop()) 

def hit(): 
    
    print("Do you want to hit or stay? H/S:")
    hitX = input() 
    
    if hitX.lower() in ["h","hit"]:
        playerCards.append(cards.pop())
        print("Player Cards: ",playerCards)
        cardCount()
        hit()
    elif hitX.lower() in ["s","stay"]:
        dealerHand()

def dealerHand(): 
    faceCountD = (dealerCards.count('J') + dealerCards.count('Q') + dealerCards.count('K'))*10  
    totalSumD = faceCountD
    totalIntD = 0
    
    if totalSumD <= 11:
         totalSumD = faceCountD + (dealerCards.count('A')*11) 
    else:
         totalSumD = faceCountD + (dealerCards.count('A')*1) 
   
    for card in dealerCards: 
        if card in 'JQKA':
            totalIntD += 0
            finalSumD =totalIntD + totalSumD
        else: 
            totalIntD += int(card)
            finalSumD = totalIntD + totalSumD 

    if finalSumD <= 16: 
        dealerCards.append(cards.pop())
        dealerHand()
    elif (finalSumD > 16) and (totalSumD < 21):
        print(dealerCards) 
        print("Dealer Card Total: ", finalSumD)
    elif finalSumD == 21: 
        print(dealerCards)
        print("Dealer Card Total :",finalSumD)
    elif finalSumD >= 22: 
        print(dealerCards)
        print("Dealer Card Total: ",finalSumD)

    faceCount = (playerCards.count('J') + playerCards.count('Q') + playerCards.count('K'))*10  
    totalSum = faceCount
    totalInt = 0
    
    if totalSum <= 11:
         totalSum = faceCount + (playerCards.count('A')*11) 
    else:
         totalSum = faceCount + (playerCards.count('A')*1) 
   
   
    for card in playerCards: 
        if card in 'JQKA':
            totalInt += 0
            finalSum =totalInt + totalSum
        else: 
            totalInt += int(card)
            finalSum = totalInt + totalSum 

    if (finalSum < 21) and (finalSumD < 21): 
        if finalSum > finalSumD: 
            print("Player Card Total: ", finalSum)
            print("Player wins!")
            playAgain()
        elif finalSum == finalSumD:
            print("Player Card Total: ", finaSum)
            print("Draw!")
            playAgain()
        else: 
            print("Player Card Total: ", finalSum)
            print("Dealer wins!")
            playAgain()
    elif (finalSum == finalSumD) or ((finalSum > 21) and (finalSumD > 21)): 
        print("Plauer Card Total: ", finaSum)
        print("Draw!")
        playAgain()
    elif finalSum == 21: 
        print("Plauer Card Total: ", finaSum)
        print("Blackjack! Player wins!")
        playAgain()
    elif finalSumD == 21: 
        print("Plauer Card Total: ", finaSum)
        print("Blackjack! Dealer wins!")
        playAgain()
    elif finalSum < 21: 
        print("Plauer Card Total: ", finaSum)
        print("Player wins!")
        playAgain()
    elif finalSumD < 21: 
        print("Plauer Card Total: ", finaSum)
        print("Dealer wins!")
        playAgain()

def showCard(): 

    print("Dealer Cards: ","['",dealerCards[0],"', '?']")
    print("Player Cards: ",playerCards)

def cardCount():
    faceCount = (playerCards.count('J') + playerCards.count('Q') + playerCards.count('K'))*10  
    totalSum = faceCount
    totalInt = 0
    
    if totalSum <= 11:
         totalSum = faceCount + (playerCards.count('A')*11) 
    else:
         totalSum = faceCount + (playerCards.count('A')*1) 
   
   
    for card in playerCards: 
        if card in 'JQKA':
            totalInt += 0
            finalSum =totalInt + totalSum
        else: 
            totalInt += int(card)
            finalSum = totalInt + totalSum 

    print("Player Card Total: ",finalSum)

    if finalSum == 21: 
        print("Blackjack!")
        dealerHand()
    elif finalSum > 21: 
        print("Player Bust!") 
        playAgain()
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

start()
while True:
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("""
  _      _               _      _               _    
 | |__  | |  __ _   ___ | | __ (_)  __ _   ___ | | __
 | '_ \ | | / _` | / __|| |/ / | | / _` | / __|| |/ /
 | |_) || || (_| || (__ |   <  | || (_| || (__ |   < 
 |_.__/ |_| \__,_| \___||_|\_\_/ | \__,_| \___||_|\_|
                             |__/                    

Welcome to blackjack.
The objective of the game is to beat the dealer
by getting a count as close to 21 as possible,
without going over 21.
""") 
    showCard()
    cardCount()
    hit() 
    dealerHand()
    
