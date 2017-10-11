# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 17:41:17 2017

@author: Kody Ellis
"""

print "=================================="
print "PASSWORD IS DEFAULT" #which is mypassword

KEY = 283
#hashing file
attempt = 0
prime_number = 541

def encrypt(string1):
        trial_key = hash(string1) % prime_number
        return trial_key

print "You get 3 total tries:"
while(attempt < 3):
    print ""
    attempt_key = raw_input("Please enter your password:")
    if encrypt(attempt_key) == KEY:
        print "Sucessful login"
        break;
    else:
        print "Your password has failed...please try again."
        attempt = attempt + 1
        
if attempt >= 3:
    print "You have been locked out."
        
