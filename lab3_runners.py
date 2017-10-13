# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:18:54 2017

@author: Kody Ellis
"""

print " ----------------------------"
print "Data entry for 100-meter dash"
print "-----------------------------"


#Gets data for the runners information

runner1 = raw_input("Name of Runner #1? ")
country1 = raw_input("Country of Runner #1? ")
time1 = raw_input("Time (in seconds) of Runner #1? ")

runner2 = raw_input("Name of Runner #2? ")
country2 = raw_input("Country of Runner #2? ")
time2 = raw_input("Time (in seconds) of Runner #2? ")

runner3 = raw_input("Name of Runner #3? ")
country3 = raw_input("Country of Runner #3? ")
time3 = raw_input("Time (in seconds) of Runner #3? ")

#Makes sure to convert the time values inputted for the time variables are of float type
time1 = float(time1)
time2 = float(time2)
time3 = float(time3)

#Makes set variable for first,second, third place and the 3 medals
first = "Gold"
second = "Silver"
third  = "Gold"

medal1, medal2, medal3 = "n/a"


#Makes a function so that I can easily print the runner's names
def run1():
    print runner1, ",", country1, ",", medal1
def run2():
    print runner2, ",", country2, ",", medal2
def run3():
    print runner3, ",", country3, ",", medal3
        
#> slower   < faster
if time1 < time2:
    medal1 = first
    medal2 = second
    if medal3 < medal2:
        medal3 = second
        medal2 = third
    if medal3 > medal2:
        medal3 = third
    
if time1 > time2:             
    medal1 = second
    medal2 = first
    if time3 < time2:
        medal3 = first
        medal2 = second
        medal1 = third
        
    if time3 > time2:
        if medal3 < medal1:
            medal3 = second
            medal1 =  third
        if time3 > time1:
            medal1 = second
            medal3 =  third
    
if time1 ==time2 == time3:
    medal1,medal2,medal3 = first
    
if time1 == time2:
    if time1 < time3:
        medal1 = first
        medal2 = first
        medal3 = second
        
    if time1 > time3:
        medal1 = second
        medal2 = second
        medal3 = first
    
if time1 == time3:
    if time1 < time2:
        medal1 = first
        medal3 = first
        medal2 = second
         
    if time1 > time2:
        medal1 = second
        medal3 = second
        medal2 = first
       
    
if time2 == time3:
    if time2 < time1:
        medal2 = first
        medal3 = first
        medal1 = second
        
    if time2 > time1:
        medal2 = second
        medal3 = second
        medal1 = first
        
    
    


print " ----------------------------"
print "Results of 100-meter dash"
print "-----------------------------"

run1()
run2()
run3()



