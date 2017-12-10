# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:19:25 2017

@author: Kody Ellis
"""

files = open("pythontestwrite.csv",'a')

try: 
    for line in files:
        pass

except:
    print "hi"        
files.close()