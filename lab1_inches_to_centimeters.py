# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#inches_to_centimeters.py
#A program to convert inches to centimeters
#by: Kody Ellis

#Asks the user to emter an amount via keyboard.
#Program will crash if the variabels are not numbers.


inches = raw_input("Enter the distance in inches: ")

#Converters whatever amount the user entered into float.(decimal numbers.)
inches = float(inches)

#The formula to converting cm to inches. Converts all the inches into
#centimerters and stores it into a variable.
centimeters = 2.54*inches

#Displays the amount of centimeters
print "The Distance is:", centimeters, "centimeters."