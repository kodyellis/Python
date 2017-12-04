# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 15:20:06 2017

@author: Kody Ellis
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 14:39:21 2017

@author: Kody Ellis
"""

name = []
number = []
count = 0
testFile = "lab 9 test case notepad.csv"
fileConnector = open(testFile,'r')
for item in fileConnector:

#skips first line
    if count == 0:
        count+=1
        pass
    else:
        name.append(item.split(",")[0])
        
        #contains number with /n
        faulty_number = item.split(",")[1]
        #Gets index of first occurence
        fn_index = faulty_number.index('\n')
        #makes new string without \n
        number_appending = faulty_number[0:fn_index]
        
        number.append(number_appending)

fileConnector.close()

combo = {}
#makes dictionary of name and card number
for i in range(0,len(name)):
    combo[name[i]] = [number[i]]
    



################################################
#############################


    
    
#checks for valid card number
def DoubleEverySecond(aString):
    #had to use index 0 to get string from lsit that was passed in
    list_of_digits = list(aString[0])

    
    res = list(map(int, list_of_digits))
    for i in range(len(res)-2,-1,-2):
        res[i] = 2* res[i]
        
    res = sum(res)
    
    if res % 10 == 0:
        return "Valid"
    else:
        return "Invalid"
    
    
for name in combo.keys():
    x =  DoubleEverySecond(combo[name])
    combo[name].append(x)
    
    




###############
###############################

AmericanExpress = ["34","37"]
DinerClubCarteBlanche = ["300","301","302","303","304","305"]
DinerClubInternational = ["36"]
DiscoverCard = ["65","6011","644","645","646","647","648","649"]
InstaPayment = ["637","638","639"]
JCB = []
Maestro = ["5018", "5020", "5038", "6304", "6759", "6761", "6762", "6763"]
Mastercard = ["51","52","53","54","55"]
Visa = ["4"]
VisaElectron = ["4026","4508","4844","4913","4917","417500"]


#company name, card number, "Visa"
def company_name(numbers,card,name):
    len1 = len(numbers)
    for i in range(0,len1):
       # print i
        if card.startswith(numbers[i]):
            return True

def make_numbers(name, x, y):
    for i in range(x,y):    
        name.append(str(i))

#appends strings, 3528 to 3589
make_numbers(JCB,3528,3590)
#appends strings, 622126 to 622925
make_numbers(DiscoverCard,622126,622926)


def assign_bank(card_number):
    cn_len = len(card_number)
    bank_name = "n/a"
    
    if cn_len == 12 or cn_len == 17 or cn_len == 18 or cn_len == 19:
        #maestro
        #if card.startswith()
        if company_name(Maestro,card_number,"Maestro"):
            bank_name = "Maestro"
    
    elif cn_len == 13:
            #maestro
         #visa
        if  company_name(Maestro,card_number,"Maestro"):
            bank_name = "Maestro"
    
    
         
        if company_name(Visa,card_number,"Visa"):
             bank_name = "Visa"
    
    
    elif cn_len == 14:
        #diner club blanche
        #diners club international
        #maestro
        if company_name(DinerClubCarteBlanche,card_number,"DinerClubCarteBlanche"):
             bank_name = "DinerClubCarteBlanche"
        elif company_name(DinerClubInternational,card_number,"DinerClubInternational"):
             bank_name = "DinerClubInternational"
        elif company_name(Maestro,card_number,"Maestro"):
             bank_name = "Maestro"
             
    elif cn_len == 15:
        #american express
        #maestro
        if company_name(AmericanExpress,card_number,"AmericanExpress"):
             bank_name = "AmericanExpress"
        elif company_name(Maestro,card_number,"Maestro"):
             bank_name = "Maestro"
        
    elif cn_len == 16:
        #discover card
        #instap payment
        #JCB
        #maestro
        #mastercard
        #visa
        #visa electron
    #
        if company_name(DiscoverCard,card_number,"DiscoverCard"):
             bank_name = "DiscoverCard"
        elif company_name(InstaPayment,card_number,"InstaPayment"):
             bank_name = "InstaPayment"
        elif company_name(JCB,card_number,"JCB"):
             bank_name = "JCB"
        elif company_name(Maestro,card_number,"Maestro"):
             bank_name = "Maestro"
        elif company_name(Mastercard,card_number,"Mastercard"):
             bank_name = "Mastercard"
        #All VisaElectron card numebrs start with 4. So if visa was listed before visaelctron, 
        #the system will automatically think visa is the correct card numebr and will
        #not consider visa electron. That is why visa electron is above visa.
        elif company_name(VisaElectron,card_number,"VisaElectron"):
             bank_name = "VisaElectron"
        elif company_name(Visa,card_number,"Visa"):
             bank_name = "Visa"

    return bank_name



    
for name in combo.keys():
    #appends corresponding bank or n/a to all dictionary keys
    y = assign_bank(combo[name][0])
    combo[name].append(y)
    

for (name,array) in combo.items():
    #if a number does not have a corresponding bank number, the numebr is still valid
    #as my code does not cover all of the banks in the world
    print name, ":",array[1], ",", array[2] 
 

        
    
    


