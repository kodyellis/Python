# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:15:00 2017

@author: Kody Ellis
"""

print "-----------------------------------"
print "Corporate Calculator"

#This gets the input from the keyboard and test to see if
#any of the input has a chracter. If it has a character 
#The program should ask you to renter your input, but with all
#digits this time.




while True:
    hours_worked = raw_input("Enter number of hours worked: ")
    if str.isalpha(hours_worked):
        print" Error. Please put in numbers only"
    else:
        hours_worked = float(hours_worked)
        break;
    
    
#This gets the input from the keyboard and test to see if
#any of the input has a chracter. If it has a character 
#The program should ask you to renter your input, but will all
#digits this time.

while True:
    hourly_rate = raw_input("Enter your base hourly rate: ")
    if str.isalpha(hourly_rate):
        print" Error. Please put in numbers only"     
    else:
        hourly_rate = float(hourly_rate)
        break;

weekly_gross_pay = 0.0

#Calculates the weekly gross pay by certain conditions.
if hours_worked > 40 and hours_worked < 60:
    weekly_gross_pay = (hourly_rate * 1.5) * hours_worked
    
elif hours_worked > 60:
    weekly_gross_pay = (hourly_rate * 2.0) * hours_worked
    
else:
    weekly_gross_pay = hourly_rate * hours_worked
    


print "Your weekly gross pay is ", weekly_gross_pay, "dollars."

