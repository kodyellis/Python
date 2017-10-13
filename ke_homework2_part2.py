# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 17:42:13 2017

@author: Kody Ellis

2players, 100 stones
they take turns, removing between 1 and 5 stones. last
person to remove a stone wins

"""

#Allows me to be more precise with my print statments.
#This imports a version of print from a future branch of python code.
from __future__ import print_function

#even though these are caps, these arent real constants
#Python doesn;t have a built in Constant keyword. So these
#are psedo-constants.
TOTAL = 100
MAX = 5
MIN = 1
pile = TOTAL # all stones are in the pile to start
p1_validity = False
p2_validity = False
p1_answer = "n/a"
p2_answer = "n/a2"



def player_choice(valid, answer):
    #Tells the function that we're using the global variable pile.
    global pile
    if answer == "n/a":
        name = "Player1:"
    elif answer == "n/a2":
        name = "Player2:"
    
    #Error checking begins
    while [ valid == False]:
        #print name
        print(name, end= '')
        #ask player 1 to enter a choice
        answer = raw_input("Choose a number of stones to take out that's between 1 and 5: ")
        # check if the user entered number and not something else
        if str.isalpha(answer):
            print ("Sorry please only put in numbers.", end = '\n')
            valid = False
            continue
        #makes the string value in answer a int value for further int comparisons.
        answer = int(answer)
        #check if the user entered a valid number (e.g. between 1 and 5)]
        if answer < 1 or answer > 5:
            print ("Sorry, please choose a number between 1 and 5")
            valid = False
            continue
        #check if there are enough stones in the pile to take]
        if pile < answer:
            print ("Sorry, please choose a different number", end = '\n') 
            valid = False
            continue
        elif pile >= answer:
            valid = True
            pile -= answer
            print('', end = '\n')
            break

while(True):      
    player_choice(p1_validity, p1_answer)
    if pile == 0:
        print ("Pile is ZEROOOOOO", end = '\n')
        break;
    player_choice(p2_validity, p2_answer)
    if pile == 0:
        print ("Pile is ZEROOOOOO", end = '\n')
        break;
    