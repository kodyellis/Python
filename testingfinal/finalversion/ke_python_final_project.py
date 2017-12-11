# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 16:13:53 2017

@author: Kody Ellis
"""

import delrec
ent = "enter records"
dele = "delete records"
vis = "visualize records"

#enter records, delete records, visualize records
#def enterRecords():
def enterFirstName():
    first_name = raw_input("Please enter your first name: ")
    x = True
    while(x):
        if str.isalpha(first_name) != True:
            first_name = raw_input("Error. Please put in letters only: ")
        else:
            x = False
    return first_name
    


def enterLastName():
    x = True
    last_name = raw_input("Please enter your last name: ")
    while(x):
        if str.isalpha(last_name) != True:
            last_name = raw_input("Error. Please put in letters only: ")
        else:
            x = False            
    return last_name            
            
            
            
def enterDOB():        
    x = True
    DOB = raw_input("Please enter your DOB in the format XX-XX-XXXX: ")
    while(x):
        if DOB[2] != '-' or DOB[5] != '-' or len(DOB) != 10:   #format is wrong != True:
            DOB = raw_input("Error. Please put incorrect format: ")
        else:
            year = int(DOB[6:10])
            year_difference = 2017 - year
            #1957 -2001 ages
            if year_difference > 60 or year_difference < 16:#ages is not right
                DOB = raw_input("Error. Age is not between 16 to 60 years. Please input again: ")

        
            else:
                x = False
    return DOB
        
##        if #student ages range from 16-60 years//
##            



def enterPhone():
    x = True
    phone_number = raw_input("Please enter your phone number: ")
    #must be  length 10 characters
    #checks [3]and [6] for dashes
    #checks [0-2] for area codes, goes through files.
    while(x):
        if len(phone_number) != 12 or phone_number[3] != '-' or phone_number[7] != '-':
            phone_number = raw_input("Error. Please put in dashes and make sure format is XXX-XXX-XXXX: ")
#        else:
#            x = False
#            
        area_code_check = phone_number[0:3] #0,1,2
        #print area_code_check
#    #uses file
        aFile = "list_valid_area_codes"
        file_connector = open(aFile, "r")
        for line in file_connector:
           # print type(line)
            #to accuratet=ly compare. comparison as strings wont work for now.
            if int(area_code_check) == int(line):
#                breaks out of loop
                x = False
                break
            
        file_connector.close()
        if (x):
            phone_number = raw_input("Error. Wrong area code.Please reenter different number: ")
    
    return phone_number

            
    
#       
#    
#    
#    
def enterSSN():
    x = True
    SSN = raw_input("Please enter your SSN in a XXX-XX-XXXX format: ")
    while(x):
        #checks [3]and [6] for dashes
        #11 char
        if SSN[3] != '-' or SSN[6] != '-' or len(SSN) != 11:
            SSN = raw_input("Error. Please put in dashes and make sure format is XXX-XX-XXXX: ")
        else:
            x= False
            
    return SSN
#        
#    
#    
#    
#    
#    
def enterEmail(first_name,last_name,SSN):
    x = True
    correct_email = first_name[0].lower() + last_name.lower() + SSN[7:11] + "@tuskegee.edu"
    #kellis5099@tuskegee.edu
    email= raw_input("Please enter your email: ")
    #If email doesnt match correct email, then an error happens
    while(x):
        if email != correct_email:
            print "this is supposed to be your right email:", correct_email
            email= raw_input("Error format is bad. Please reenter your email: ")
        else:
            x=False
            
    return email
            
    
    

    

def inputCommand():
    #general command
    #print menu, explanation

    global ent
    global dele
    global vis    
    while(True):
        command = raw_input("Command, all lowercase: ")
        #command = command.lower()
        command = command.split(" ")

        com = command[0] + " " + command[1]
        
        
        #if command != ent or command != dele or command != vis:
        if com == ent:
            return command
        elif com == dele:
            #returns command when correct command is inputted
            return command
        elif com == vis:
            return command

            
        print "Error, please try again"

            
        
        
        
        
def enterRecords():
    first_name = enterFirstName()
    last_name = enterLastName()
    DOB = enterDOB()
    phone = enterPhone()
    SSN = enterSSN()
    email =enterEmail(first_name, last_name, SSN)
    
    record = '\n' + first_name + ","+ last_name +","+ DOB +"," + phone + "," + SSN + "," + email
    print record
    
    #uses file operation
    #delrec.enterRecordsv2(record)
    
#append can create new file too
    files = open("pythontestwritev3.csv",'a')
    record = '\n' + first_name + ","+ last_name +","+ DOB +"," + phone + "," + SSN + "," + email

    files.write("#First,#Last,   #Year,   #Phone Number,    #SSN,      #Email")
    files.write(record)
    files.close()
	
#    except:
#		#incase using the 'a' attribute accnot create the document is the document is not create yet.
#      open("pythontestwritev2.csv", 'a')
#      record = 'first_name + ","+ last_name +","+ DOB +"," + phone + "," + SSN + "," + email
#      files.write("#First,#Last,   #Year,   #Phone Number,    #SSN,      #Email")
#      files.write(record)
#      files.close()
    
    
def visualizeRecords():
    #print "visualizing.."
    file_connector = open("pythontestwrite.csv","r")
    for line in file_connector:
        if line[0] == '#':
            print "#First,#Last,   #Year,   #Phone Number,    #SSN,      #Email"
        else:
            print line
    file_connector.close()
    

def recordSelection():
    global ent
    global dele
    global vis
    command = inputCommand()
    menu_command = command[0] + " " + command[1]
    if len(command) == 4:
        item = command[2]
        value = command[3]
        
    if menu_command == ent:
        print "ent"
        enterRecords()
    
    elif menu_command == dele:
        print "del"
        delrec.deleteRecords(item,value)
    
    
    elif menu_command == vis:
        print "vis"
        visualizeRecords()
        
recordSelection()
    


