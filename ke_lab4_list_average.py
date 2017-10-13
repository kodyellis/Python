# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 16:25:22 2017

@author: Kody Ellis

filename: ke_lab4_list_average.py
This file returns the average of a list / amount of numbers
"""
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = [12, 45, 67, 89, 77]

#Returns the average of a list / amount of numbers
#sum get the sum amount and len gets the amount of numbers in the list/amount
#some sum/#amount would be the average
def my_average(some_list):
    return sum(some_list) / len(some_list)


print my_average(list1)
print my_average(list2)
print my_average(list3)