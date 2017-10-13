# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:22:29 2017

@author: Kody Ellis
"""


#This Displays the menu
print "Available menu at Moutain Roz"
print "-----------------------------------"
print "1. Shark fins"
print "2. Lamb tongues"
print "3. Dragons wings"

#Obtains input from keyboard
#This while loops keeps looping if the input doesnt match any
#of the menu options.
while True:
    choice = raw_input("Please enter your menu choice using a number between 1-3: ")
    #Thsi converts what was captured in the keyboard into integer
    choice = int(choice)
    if choice > 3 or choice < 1:
        print "Sorry, you have chose an incorrect number. Please pick a choice betweeen 1, 2, and 3"
        
    else:
        break;

    
    

#This while loops keeps looping if the input does not match the requirements
#for the previous choice. For example is the previous chocie
#was choice #1, then you are only allowed to enter 1 or 2
#for this input.
while True:
    number_of_orders = raw_input("A customer can only have 1-2 orders for choice #1, 1-3 orders for choice #2, and 1-5 orders for choice #3. Please enter the number of orders: ")
    number_of_orders = int(number_of_orders)
    
    if choice == 1:
        if number_of_orders >= 3 or number_of_orders <= 0:
            print "Sorry, you have chose an incorrect number. Please pick a choice betweeen 1, 2, and 3"
        else:
            break;
        
    if choice == 2:
        if number_of_orders >= 4 or number_of_orders <= 0:
            print "Sorry, you have chose an incorrect number. Please pick a choice betweeen 1, 2, and 3"
        else:
            break;
        
    if choice == 3:
        if number_of_orders >= 6 or number_of_orders <= 0:
            print "Sorry, you have chose an incorrect number. Please pick a choice betweeen 1, 2, and 3"
        else:
            break;

order_name = "n/a"
order_number = "n/a"
    
 #This Assigns names to varible so when it calls your order, the
 #amount and name are correctly displayed
if choice == 1:
    order_name = "Shark fins"
if number_of_orders == 1:
    order_number = "One"

if choice == 2:
    order_name = "Lamb tongues"
if number_of_orders == 2:
    order_number = "Two"

if choice == 3:
    order_name = "Dragons wings"
if number_of_orders == 3:
    order_number = "Three"
    
if number_of_orders == 4:
    order_number = "Four"
    
if number_of_orders == 5:
    order_number = "Five"


    
print order_number, order_name, "coming right up!"

