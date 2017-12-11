# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:37:18 2017

@author: Kody Ellis
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:33:36 2017

@author: Kody Ellis
"""

#def enterRecordsv2(record):
#	try: 
#		files = open("pythontestwrite.csv", 'a')
	
#	except:
#		#incase using the 'a' attribute accnot create the document is the document is not create yet.
#		open("pythontestwrite.csv", 'w')
		
	
#	files.write(record)
#	files.close()
	
	
	#appends new record to a new line
	#f = "Logan"
	#l = "Ellis"
	#d = "08-20-1997"
	#phone = "201-111-1111"
	#ssn = "543-22-5099"
	#email = "lellis5099@tuskegee.edu"
	#record = '\n' + f + ","+ l +","+ d +"," +phone + "," + ssn + "," + email



def deleteRecords(data_item,data_value):
	
    months = {"January" : "01","Febuary": "02","March": "03","April": "04","May": "05","June": "06","July": "07","August": "08","September": "09","October": "10","November": "11","December": "12"}
        
        #gets 01,12,10,etc
       # deletion_month = months[data_value
                                
    #ssn = "123456789"
	#print ssn
#SSN
    
    if data_item == "SSN":
		if len(data_value) == 9:
    #insert dashes
			data_value = data_value[:3] + '-' + data_value[3:5] + "-" + data_value[5:]
    
#print ssn




#phone = "1234567890"
#print phone
#phone
    if data_item == "phone-number":
        
        if len(data_value) == 10:
            
    #insert dashes
            data_value = data_value[:3] + '-' + data_value[3:6] + "-" + data_value[6:]
    
#print phone
	       
    #eleminates any records that meet the specification from delete records
    field = {"first-name": 0, "last-name": 1, "DOB": 2, "phone-number": 3, "SSN": 4, "email": 5 }
    
    #data_item = "first-name"
    
    
   # d = files.readlines()
    #goes to first position in file.

    files = open("pythontestwrite.csv", 'r+')
        #files = open("pythontestwrite.csv", 'r+')

    files.seek(0)
    
    data = []
    x = []
    #/n spcaes
    for i in files:
        #clears x array for every line
        x = []
        #print "i"
        #i prints empty line iterates throughout each line
        #this passes header line
        if i[0] == "#": #or (not line [0].isdigit()) :
            pass
        else:
                    #only gets items from date
           # data.append(i.split(","))  #had to remove newliens from csv fiel
           
           #appends 1 line to x.
           
            x.append(i.strip()) #no, 1 whole array
            for item in x:
                if item == '':
                    x.remove(item)
           # print "x:", x, type(x[0])
            
            #print x[0]
            
            #passes first name to dictionary, which returns 0, so we use 
            #0 index to search for first names
            
            #special case for month deletion
            
            try:
                #test = x[0]
                if data_item == "DOB":
                    deletion_month = 01
                    deletion_month = months[data_value]
    				
    				#gets first two chracters of birth string, which is the month
                    if x[0].split(",")[field[data_item]][0:2] != deletion_month:     #!= 'Logan':
                        data.append(x[0].split(","))
                        pass #???
                else:
                    if x[0].split(",")[field[data_item]] != data_value:     #!= 'Logan':
                        data.append(x[0].split(","))
                
            except:
                print " Current List element must be null, meanign there is a newline on the connected file."
    
    
    #        data.append(z) [[['Kody', 'Ellis', '08-20-1997', '201-111-1111', '543-22-5099', 'kellis5099@tuskegee.edu']], ['sKody',] ] 
    #data = [] each list element in data is another lsit which represents a record
    #x = [] z.split = []
    
    files.close()
    
    
    #print data
    #rewrites file with new data, overwriting previous data.
    header = "#FirstName, #LastName, #Year, #Phone Number, #SSN, #Email" + '\n'
    files = open("pythonrewritetest.csv", 'w')
    
    #writes header for file
    files.write(header)
    
    #obtains new file data from python data, and appends it to file
    for i in range(len(data)):
        string1 = ",".join(data[i])
        print '\n', string1, "33333333333333333333"
        string1 = string1 + '\n'
        files.write(string1)
        
        
    files.close()
    
    
    
#deleteRecordv2("first-name","Logan")
#confirmation of importation






print "importing delrec.py file.....done"
deleteRecords("DOB","August")