# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 16:34:07 2017

@author: Kody Ellis
"""
#Imports the module for math. This lets us use heavy math functions and more.
import math

print "This program finds the real solutions using the distance formuala"
#Gets the values of the variables and stores them as string format.
#Program will crash if the variabels are not numbers.
x1 = raw_input("Enter x1: ")
x2 = raw_input("Enter x2: ")
y1 = raw_input("Enter y1: ")
y2 = raw_input("Enter y2: ")

#Converters the variables from string to float format.
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

#The formula for the distance formula
disRoot = math.sqrt(((x2 - x1)**2) + ((y2-y1)**2))
print "The distance between (", x1, ",", x2, ") and (", y1, ",", y2, ") is: ", disRoot