# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:21:56 2017
letterCount

@author: Kody Ellis
"""

import string
alphaString = string.lowercase

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
        #Sees if the current chracters selected is the chracter we are counting right now.
        if char == target_char:
            number_of_occurences += 1
        
    #Closes file
    file_connector.close()
    
    return number_of_occurences
    
print '\n'

for char in alphaString:
    print char, "=", letterCount(char, 'gettysburg.txt')
