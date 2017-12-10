# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:30:36 2017

@author: Kody Ellis
"""

files = open("pythontestwrite.csv", 'a')
#f = "Kody"
#l = "Ellis"
#d = "08-20-1997"
#phone = "201-111-1111"
#ssn = "543-22-5099"
#email = "kellis5099@tuskegee.edu"
#record = f + ","+ l +","+ d +"," +phone + "," + ssn + "," + email
#files.write(record)





#appends new record to a new line
#f = "Logan"
#l = "Ellis"
#d = "08-20-1997"
#phone = "201-111-1111"
#ssn = "543-22-5099"
#email = "lellis5099@tuskegee.edu"
#record = '\n' + f + ","+ l +","+ d +"," +phone + "," + ssn + "," + email
#files.write(record)
#
#files.close()


files = open("pythontestwrite.csv", 'r+')
d = files.readlines()
files.seek(0)

data = []
x = []
#for i in d:
#    #print "i"
#    #i prints empty line iterates throughout each line
#    #print i
#    if i[0] == "#": #or (not line [0].isdigit()) :
#        pass
#    else:
#                #only gets items from date
#        data.append(i.split(","))
#    #print "d"
#    #print d
#    print "s"
#    #if i != "line you want to remove...":
#     #   f.write(i)
##f.truncate()



#/n spcaes
for i in files:
    x = []
    z = []
    #print "i"
    #i prints empty line iterates throughout each line
    #print i
    if i[0] == "#": #or (not line [0].isdigit()) :
        pass
    else:
                #only gets items from date
       # data.append(i.split(","))  #had to remove newliens from csv fiel
        x.append(i.strip()) #no, 1 whole array
        for item in x:
            if item == '':
                x.remove(item)
        print x
                
       # z.append(x[0].split(","))
       
#       0 first name
#       1 lastname
#       2 year
#       3 phone number
#       4 ssn
#       5 email
        if x[0].split(",")[0] != 'Logan':
            data.append(x[0].split(","))
            
#        data.append(z) [[['Kody', 'Ellis', '08-20-1997', '201-111-1111', '543-22-5099', 'kellis5099@tuskegee.edu']], ['sKody',] ] 
#data = [] each list element in data is another lsit which represents a record
#x = [] z.split = []
    #print "d"
    #print d
    print "s"
    #if i != "line you want to remove...":
     #   f.write(i)
#f.truncate()


files.close()


print data
#for item in data:
#   # item.remove('/n')
#    print item
#    if item == '\n':
#        print 222222222222
#     #   data.remove('/n')
        
#print data

#for item in data:
#    for i in item:
#        if i == 'Kody'
#        
header = "#FirstName, #LastName, #Year, #Phone Number, #SSN, #Email" + '\n'
files = open("pythonrewritetest.csv", 'w')
files.write(header)
for i in range(len(data)):
    string1 = ",".join(data[i])
    print string1, "33333333333333333333"
    string1 = string1 + '\n'
    files.write(string1)
    
files.close()