# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 16:19:18 2017

@author: Kody Ellis
"""

#lb2_quadratic_formula
# A program that computes the real roots of a quadratic  
#Note: This simple program wil crash if the equation has no real roots
#Author: Kody Ellis

#Making the math library availble
import math

print "This program finds the real solutions to a quadratic"
print "Note: this program will crash if the equation has no real roots"
print
#Get the vale of the coefficietnts and store them as variables a, b, and c
a = raw_input("Enter the coefficient a: ")
b = raw_input("Enter the coefficient b: ")
c = raw_input("Enter the coefficient c: ")

#Convert the coefficients from string format to float-point format
a = float(a)
b = float(b)
c = float(c)


#This is the discrimant for quadratic equation
disc = (b**2) - (4*a*c)

#these are roots. Values are put into them to initialize the variables
root1 = a
root2 = b

#x is root
#if a does equal zero
if a  == 0:
    if b == 0 and c!= 0:
        print "No solutions"
        
    if b != 0 and c== 0:
        print "x = 0 is the only solution"
        x = 0.0
        
    if b == 0 and c== 0:
        print "No solutions"
        
    if b != 0 and c!= 0:
        print " x will equal -c/b"
        x = (-c)/b
        print "x equals ", x
        
        
#if a doesn't equal zero        
if a != 0 :
    if disc > 0:
        print "There are two distinct real solutions"
        root1 = (-b + math.sqrt(disc)) /  ( 2*a)
        root2 = (-b - math.sqrt(disc)) /  ( 2*a)
        print "First root equals: ", root1, " and Second root equals: ", root2, " ."

    elif disc < 0:
        print "There are two distinct complex solutions"
        root1 = (-b + math.sqrt(abs(disc)) /  ( 2*a))
        root2 = (-b - math.sqrt(abs(disc)) /  ( 2*a))
        print "First root equals: ", root1, " and Second root equals: ", root2, " ."
             
    elif disc == 0:
        print "There is a single real solution"
        root1 = disc / (2 *a)
        
        #If first root is zero, this changes the value
        if root1 == 0 :
            root1 = root1 * (-1)
            
        print "First root equals: ", root1
    





