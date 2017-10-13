# -*- coding: utf-8 -*-
#mcdonaold
"""
Created on Fri Oct 06 16:22:00 2017

@author: Kody Ellis
filename: ke_lab4_mcdonald.py
"""


#This is a function to print Old MCDonald lyrics. In certain parts of the lucrics, words can be substitued 
#to a certain animal and the sounds it makes,
#The \ at the end of the line allows me to put the if statement on a differ line for readability
def mcdonald(animal, sound):
    if(animal == "cow" or animal == "sheep" or animal == "dog" or animal == "cat" or animal == "turkey"):
        if( (animal == "cow" and sound == "moo") or (animal == "sheep" and sound == "baaa") \
            or (animal == "dog" and sound == "woof") or (animal == "cat" and sound == "meow") \
            or (animal == "turkey" and sound == "gobble gobble") ):
            
            #Still using the \ for readability. Uses 1 print statement instead of several.
            print "Old MacDonald had a farm, Eeigh, Eeigh, Oh!", '\n', \
            "And on the farm he has a", animal + ", Eeigh, Eeigh, Oh!", '\n', \
            "With a", sound + ", " + sound,"here and a", sound + ", " + sound, "there.", '\n', \
            "Here a", sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound + ".", '\n', \
            "Old MacDonald had a farm, Eeigh, Eeigh, Oh!", '\n'
            

#A Lst variable that contains all the strings for the animals and the sound they make.
list1 = ["cow", "moo", "sheep", "baaa", "dog", "woof", "cat", "meow", "turkey", "gobble gobble"]

#Test Cases
mcdonald(list1[0],list1[1])
mcdonald(list1[2],list1[3])
mcdonald(list1[4],list1[5])
mcdonald(list1[6],list1[7])
mcdonald(list1[8],list1[9])

