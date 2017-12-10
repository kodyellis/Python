# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:02:04 2017

@author: Kody Ellis
"""


#august and september wont work for some reason
months = {
        "January" : "01",
        "Febuary": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
        
        }

print months["January"]

ssn = "123456789"
print ssn
#SSN
if len(ssn) == 9:
    #insert dashes
    ssn = ssn[:3] + '-' + ssn[3:5] + "-" + ssn [5:]
    
print ssn




phone = "1234567890"
print phone
#phone
if len(phone) == 10:
    #insert dashes
    phone = phone[:3] + '-' + phone[3:6] + "-" + phone[6:]
    
print phone


delete = raw_input("Enter delete records:")

data = delete.split(" ")
#print data
#0 delete
#1 records
#2 ssn, first-name, dob, etc
#3 type