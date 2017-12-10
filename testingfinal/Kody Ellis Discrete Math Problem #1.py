# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 22:32:31 2017

@author: Kody Ellis
"""

# Program 1. Set operations
#Using Python to create a program that can identify and complete set operations:
#    Set Operations:
#        
#        Union
#        Intersect
#        Difference
#        Cross product
#        Equality
#        Subset
#        Proper SUbset
#        Complement

#import intertools, so we can use set oeprations methods
import itertools


A={1,2,3,4,7}
B={5,6,7,8,9}
#A U B = U
U={1,2,3,4,5,6,7,8,9,10}


#note to self, experiement and refactor this using tkinter(gui library) durign my christmas break

input1 = raw_input("Enter a command to continue: Union, Intersect, Difference, Cross product, Equality, Subset, Proper SUbset, Complement: ")

if input1.lower() == "union":
    

    # using set operators
    #union
    print("Union=",A.union(B))
    
elif input1.lower() == "intersection":
    #Intersection
    print("Intersection",A.intersection(B))
    
elif input1.lower() == "difference":    
    #Difference
    print("Difference A",A.difference(B))
    print("Difference B",B.difference(A))

elif input1.lower() == "crossproduct":
    ##Crossproduct in a loop
    for i in itertools.product(A,B):
       print("Crossproduct",i)
   
elif input1.lower() == "equality":
    #Equality,
    print("Equality A",A==B)
    print("Equality B",B==A)

elif input1.lower() == "subset":
    #Returns True or False for subsest
    print("SubsetA",A.issubset(B))
    print("Subset B",B.issubset(A))
    
elif input1.lower() == "proper subset" or input1.lower() == "propersubset":
    #Returns True or False for proper subset
    print("Proper subset A",A.issuperset(B))
    print("Proper subset B",B.issuperset(A))

elif input1.lower() == "complement":
    #Complement
    print("Complement of A",U-A)
    print("Complement of B",U-B)

