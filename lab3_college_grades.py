# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:49:04 2017

@author: Kody Ellis
"""

name = raw_input("What is the full name of your university: ")
print " -----------------------------------"
print "Graduation Status Check"
print name
print "-------------------------------------"

#Gets input of all grades
cal = raw_input("Enter your Calculus letter grade: ")
bio = raw_input("Enter your Biology letter grade: ")
chem = raw_input("Enter your Chemistry letter grade: ")
comp_sci = raw_input("Enter your Computer Science letter grade: ")
ee = raw_input("Enter your Eletrical Engineering letter grade: ")


#Initialzes value of grades and gpa
cal_score = 0.0
bio_score = 0.0
chem_score = 0.0
comp_sci_score = 0.0
ee_score = 0.0
gpa = 0.0
grad_status = "n/a"

#This is a function to "convert" the letter grade to its numeric value
def gpa_to_score(grade):
    if grade == "A" or grade == "a":
        grade_score = 4.0
        return grade_score
    elif grade == "B" or grade == "b":
        grade_score = 3.0
        return grade_score
    elif grade == "C" or grade == "c":
        grade_score = 2.0
        return grade_score
    elif grade == "D" or grade == "d":
        grade_score = 1.0
        return grade_score
    elif grade == "F" or grade == "f":
        grade_score = 0.0
        return grade_score
        

#Converts letter grade to its corresponding value.
cal_score = gpa_to_score(cal)
bio_score = gpa_to_score(bio)
chem_score = gpa_to_score(chem)
comp_sci_score = gpa_to_score(comp_sci)
ee_score = gpa_to_score(ee)


gpa =  (cal_score + bio_score + chem_score + comp_sci_score + ee_score) / 5

#Sets the graduation status message
if gpa < 2.5:
    grad_status = "Sorry, but you can't graduate."
elif gpa >= 2.5 and gpa < 3.25:
    grad_status = "Congratulations!! You can graduate."
elif gpa >=3.25 and gpa < 3.5:
    grad_status = "Congratulations!! You can graduate with cum laude honors."
elif gpa >= 3.5 and gpa < 3.75:
    grad_status = "Congratulations!! You can graduate with magna cum laude honors."
elif gpa >= 3.75:
    grad_status = "Congratulations!! You can graduate with summa cum laude honors."
       
print "--------------------------------"
print "GRADUATION STATUS"
print" --------------------------------"
print "GPA:", gpa
print "STATUS: ", grad_status
