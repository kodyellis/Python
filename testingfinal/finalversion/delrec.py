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

def deleteRecords(data_item,data_value):
	
    months = {"January" : "01","Febuary": "02","March": "03","April": "04","May": "05","June": "06","July": "07","August": "08","September": "09","October": "10","November": "11","December": "12"}
        
    
                                
#SSN
#parses a dash-less SSN format and inserts dashes so we can compare it to normal SSN strings on file.    
    if data_item == "SSN":
		if len(data_value) == 9:
    #insert dashes
			data_value = data_value[:3] + '-' + data_value[3:5] + "-" + data_value[5:]




#parses a dash-less phone format and inserts dashes so we can compare it to normal SSN strings on file.    
    if data_item == "phone-number":        
        if len(data_value) == 10:            
    #insert dashes
            data_value = data_value[:3] + '-' + data_value[3:6] + "-" + data_value[6:]
    
	       
    #this code eleminates any records that meet the specification from delete records
    field = {"first-name": 0, "last-name": 1, "DOB": 2, "phone-number": 3, "SSN": 4, "email": 5 }
    
    
    

    files = open("pythontestwrite.csv", 'r+')

    files.seek(0)
    
    data = []
    x = []
    for i in files:
        #clears x array for every line
        x = []
        #print "i"
        #i prints empty line iterates throughout each line
        #so this code passes header line
        if i[0] == "#": #or (not line [0].isdigit()) :
            pass
        else:
           #appends 1 line to x. 
            x.append(i.strip()) #no, 1 whole array
            for item in x:
                if item == '':
                    x.remove(item)

            #passes first name to dictionary, which returns 0, so we use 
            #0 index to search for first names 
            #special case for month deletion
            
            try:
                #test = x[0]
                if data_item == "DOB":
                    #gets 01,12,10,etc
                    #default value there to prevent crash
                    deletion_month = 01
                    deletion_month = months[data_value]
    				
    				#gets first two chracters of birth string, which is the month
                    if x[0].split(",")[field[data_item]][0:2] != deletion_month:     
                        data.append(x[0].split(","))
                        pass #???
                else:
                    #x is a list with index 0, 1 item. We get it to split everythign in that element
                    #which splits the data items inside that element.
                    #field gets the index number of the element, which correlates to a data field the
                    #item is in. so [0] correlates to the first name, [5] correlats to email field
                    #data item is the matching item
                    # data value is the item we dont want in the array.
                    #if it matches with the current item, then the line won't be real.
                    if x[0].split(",")[field[data_item]] != data_value:     
                        data.append(x[0].split(","))
                
            except:
                print " Current List element must be null, meanign there is a newline on the connected file."
    
    files.close()




    
    #print data
    #rewrites file with new data, overwriting previous data.
    header = "#FirstName, #LastName, #Year, #Phone Number, #SSN, #Email" + '\n'
    files = open("pythontestwrite.csv", 'w')
    
    #writes header for file
    files.write(header)
    
    #obtains new file data from python data, and appends it to file
    for i in range(len(data)):
        string1 = ",".join(data[i])
        string1 = string1 + '\n'
        files.write(string1)
    files.close()
    




    
print "importing delrec.py file.....done"