# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 10:09:41 2017

@author: Kody Ellis
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 16:23:36 2017

@author: Kody Ellis

#v3 not done rip

v7 ake everything right
"""
import string
shift = 5


old = string.ascii_lowercase
new = [0]*26
new_lc = []

def caesar_encrypt(textfile,shift):
    global old
    global new
    #Opens file
    file_connector = open(textfile, 'r')
    
    #reads the file and stores contents as a giant string
    data = file_connector.read()
    
    #data already has the contents of the file, so we can close the conenction.
    file_connector.close() 
    #traverses each character in the file
    #for char in data:

    #takes length of old, which is lentgh of alphabet, 26
    #i goes from 0 to 25, 26 items in total
    for i in range(len(old)):
        #If i can add the shift without looping(going over 25, the position of 
        #the last alphabet letter)
        if ((i + shift) < 26):
            new[i] = old[i+shift]
        #if it has to loop, then it will execute this line. So say i is 25 and shift is 1
        #26 %26 = 0 meanign z will go to the letter a
        else:
           new[i] = old[(i + shift) % 26]

    #old has alphabet and new has shifted alphabet. ALl the indexes match up
    #This replaces the correspongind alphabet letters in data with the new shifted chracters
    #.upper() is used for formatting reasons
    for i in range(len(new)):
        data = data.replace(old[i],  new[i].upper())
        
    #This makes all letters in data lowercase , for formatting reasons.
    data = data.lower()
       
    return data


#does not need shift number as it takes old vales from old and new and matches them up.
def caesar_decrypt(data): 
    global new
    global old
    #empty new1 string
    new1 = ""
    #Takes all the items in lsits and stores them in a string, with no spaces in between
    new1 = new1.join(new)
    
    data1 = ""

    x = 0

    #For the entire length of the encrypted string
    for i in range(len(data)):
        #If the current char selected in data is in the alphabet, this if 
        #statement executes
        if (data[x].isalpha):
            #With the curretnt char selcted from data, This will find the
            #corresponding letter in the new1 string and returns its index
            new_index = new1.find(data[x])
            
            #This finds the index in the shifted alphebet, and trasnlates it to
            #the original alphebet which is in old. After that it adds on to a new version
            #of the data1 string
            data1 = data1 + data[x].replace(new[new_index], old[new_index])
            
            #used as an easy counter instead of i for traversing the encrypted string
            x += 1

    #This makes all letters in data lowercase , for formatting reasons.
    data = data.lower()
    return data1



def infer_shift(textfile):

    list1 = " "
    highest = 0
    highest1 = 0
    alphaStringLow = string.lowercase


    for i in range(0,26):
        
        #Counts the number of occurences of a substring in list1 and returns it to freq
        freq = list1.count(alphaStringLow[i])
        if freq > highest:
            highest = freq
            #Adds current index of the highest number count recorded
            highest1 = i
       #Adds the next shift to the encrypt function that will returned a differennt
       #shifted string. This data is put inside the list1 string
        list1 = caesar_encrypt(sample_file, i+1)
        
        
    return highest1


def caesar_decrypt2(textfile, language = "english"):
    #Infers the shift of the decrypted file
    #line below not needed
    #shift = infer_shift(textfile)
    #Uses main decrypt function to get the unshifted message
    if language == "english" or language == "zulu" or language == "dutch":
        deshifted_msg = caesar_decrypt(textfile)
    return deshifted_msg




#function returns the value of the number of time an alphabet letter occurs in a file
def letter_count(file_name, top):
    global new_lc
    alphaStringLow = string.lowercase

    #Creates a file object that connects to a file for reading
    file_connector = open(file_name, 'r')
    
    #reads the file and stores contents as a giant string
    data = file_connector.read()
        
    #char in in alphabet
    for target_char in alphaStringLow:
        number_of_occurences = 0

        #traverses each character in the file
        for char in data:
            
    
            #Sees if the current characters selected is the chracter we are counting right now.
            #Counts the lower or upper case occurance of the target character.
            if char == target_char or char == target_char.upper():
                number_of_occurences += 1
                
#        for char in alphaStringLow:
#            print char, "=", number_of_occurences

        new_lc.append(number_of_occurences)

        
        #Closes file.
        file_connector.close()
        
        #gets teh index of where it fins the max number of new
        
        #gets max number
        max_number = list(sorted(set(new_lc))) 
        #max is now int type
        #gets the nhighest numebr from the list
        max_number = max_number[top]
        
        #gets index of max numebr
        max_index = new_lc.index(max_number)

        alphabet_index_max = alphaStringLow[max_index]
        
        
    return alphabet_index_max


def infer_language(textfile):
    # highest letter frequncies
#    English is "e" and "t"
#    Dutch is "a"
#    Zulu is "e"
#    Since Zulu and English both have "e" as their top frequinces, I am just 
#    goign to count the most frequenct characetr of english as the langauge_determiner
#    The other 2 langauegs don't have "t" in their top frequncy distributions, so it is okay
#    to use "t"
    



    highest = -1
    if letter_count(textfile, highest) == "a":
        return "zulu"
    
    #Uses a veration of the letter count function to get the numebr of the second highest frequency
    elif letter_count(textfile, highest) == "e":
        
        check = second_highest(letter_count_second())
        if check == "n":
            return "dutch"
        elif check == "t":
            return "english"
    #returns -1 if oepration failed
    else:
        return -1
    
    
#new functions because cant assign max_number[-2] or acces any of max_number using any index otehr than [0]
def letter_count_second():
    global new_lc
    max_number = list(sorted(set(new_lc))) # highest  
    return max_number[-2]

#variation of letetr count. gets the second higehst freq number from parameter
#finds out the correspondign letter to it
def second_highest(max_number):
    global new_lc
    low_string = string.lowercase
    max_index = new_lc.index(max_number)
    alphabet_index_max = low_string[max_index]
    return alphabet_index_max

    
def caesar_decrypt3(textfile):
    lang = infer_language(textfile)
    msg = caesar_decrypt2(textfile, lang)
    return msg
        
#file text not provided inside of the file
sample_file = "gettysburg_english.txt"
test = [caesar_encrypt(sample_file,shift)]

#testing various function
#decrpts
test.append(caesar_decrypt(test[0]))

#each time function call, can append function reposnse to list

#adds encrypted 
test.append(infer_shift(test[0]))
print test[2]
test.append(caesar_decrypt2(test[0]))
test.append(infer_language(sample_file))
print test[4]
test.append(caesar_decrypt3(sample_file))
print test[5]

#caesar_decrypt3(textfile, infer_language(textfile))
