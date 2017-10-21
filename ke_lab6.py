# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:21:56 2017
@author: Kody Ellis
Prints the amount of time each letter of the alphabet occurs in a file.
"""

import string

#Makes a variable that has all of the lower case alphabet
alphaStringLow = string.lowercase

#function returns the value of the number of time an alphabet letter occurs in a file
##Test file provided is gettysburg.txt
def letterCount(target_char, file_name):
    
    #Creates a file object that connects to a file for reading
    file_connector = open(file_name, 'r')
    
    #reads the file and stores contents as a giant string
    data = file_connector.read()
    
    number_of_occurences = 0 
    
    #traverses each character in the file
    for char in data:
        #Sees if the current characters selected is the chracter we are counting right now.
        #Counts the lower or upper case occurance of the target character.
        if char == target_char or char == target_char.upper():
            number_of_occurences += 1
            
    #Closes file.
    file_connector.close()
    
    return number_of_occurences
    
#Prints a newline for aesthetic reasons
print '\n'

for char in alphaStringLow:
    print char, "=", letterCount(char, 'gettysburg.txt')
