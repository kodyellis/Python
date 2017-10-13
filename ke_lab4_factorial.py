# -*- coding: utf-8 -*-
#factorial
"""
Created on Fri Oct 06 16:22:02 2017

@author: Kody Ellis

filename: ke_lab4_factorial.py
"""

#Importing this to only use for the factorial function.
from math import factorial

#This is a function that uses the math factorial function to return a factorialized value
#Because we only import factorial from math library we dont have to use math.factorial
def prodN(n):
    if n > 0:
        return factorial(n)
    elif n == 0:
        return 1
    else :
        return None
    
    
print prodN(5)
print prodN(10)
print prodN(2)
print prodN(0)
print prodN(-10)