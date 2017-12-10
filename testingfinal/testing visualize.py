# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:25:21 2017

@author: Kody Ellis
"""


def visualizeRecords():
    print "visualizing.."
    file_connector = open("pythontestwrite.csv","r")
    for line in file_connector:
        if line[0] == '#':
            print "#First,#Last,   #Year,   #Phone Number,    #SSN,      #Email"
        else:
            print line
    file_connector.close()

visualizeRecords()
