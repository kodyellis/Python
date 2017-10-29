# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:17:29 2017

@author: Kody Ellis
"""
import string;
aString = string.lowercase;

#Problem 1
def caesar_encrypt(textfile, shift):
    

    
    global aString;
    
    #int operator overload is for correct division later on 
    #Gets item length of array
    length = int(len(aString));
    
    #Gets max index number of array
    #ERRORRRR needs review
    length1 = int(length - 1);
    
    file_connector = open(textfile, 'r');
    
    open_file = file_connector.read();
    
    new_file = '';
    
    for char in open_file:
        #resets shift
        shift1 = shift
            
        #Gets current number of char in file
        #g = 8
        current = aString.rindex(char);
        
        #Because if shift is greater than or equal 26 number will loop entirely around
        #26 shift means full circle, so no move required
        # 100 % 25 = 22
        #24 / 25 equals 0
        #25 /25 equals 1
        #26 / 25 equals 1
        #so in case 100, 100-26 = 74, 74-26 = 48, 48-26 = 22, 22 / 26 = 0
        
        while ((shift1 / length1) >= 1 and shift1 != length1):
            shift1 = shift1 - length;
        #Max I can shift to the right with shift number
        #or until I hit 25    
        #26 - 8 = 18 shifts to right
        #18
        shift_caln = length - current;
        
        #shift can be done without a loop
        #4 shift
        if shift < shift_caln:
            #execute shift
            #add letter to create new file variation?
            #break?
            
        #shift requires loop
        #25
        elif shift >= shift_caln:
            #go to [0]
            # 25-18 = 7 shifts to right now
            shift1 = shift1 - shift_caln;
            #execute shift
            #index number will find and correspong to aString
           #a bool value before will say uppper or lower?
          # if lower then a mthod will be called to make char1 upper
            #char1 = 
            #add letter to create new file variation?
            #break?
            
    
            
        
        #Decreases number of shift
        #
        #shift = shift - shift_caln;
        
        #so if at end of alphabet and there are more to shift
        #if shift_caln == 25 and shift != 0:
            #current = 0;
        #Shift char index number to next
        
        
        #new file variation?Can't add to existing strigns, so make a new one?
        new_file = new_file + char1;
        
    file_connector.close;
    
    return new_file
    
    


shift_argument = 1;

print '/n' + "jjjjjjjjjjjjjjjjjjjjjjjjj"
print caesar_encrypt("gettysburg.txt", 0)
print '/n' + "jjjjjjjjjjjjjjjjjjjjjjjjj"
print caesar_encrypt("gettysburg.txt", shift_argument)
print '/n' + "jjjjjjjjjjjjjjjjjjjjjjjjj"
print caesar_encrypt("gettysburg.txt", 100)
