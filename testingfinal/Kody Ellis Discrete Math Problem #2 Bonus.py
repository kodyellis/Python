# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 21:23:22 2017

@author: Kody Ellis
"""
# Sarah Alexander
# Dr.Nirang
#assignment2-relations
#Intiliaze the relations


####
#problem 2 word
#https://docs.google.com/document/d/1xEwMFk3GHXgD7Y4WhzGNIrHlrRhf0EV3eHAFZv7l20I/edit?usp=sharing
#



#Reflexive
def reflexive(R):
    '''
    @param R : set containing homogenous elements
    '''
    result = []
    a = []
    y = []

    for a1, a2 in R:
        if (a1 == a2):
            result.append((a1,a2))
            y.append(a1)

        if (a1 not in a):
            a.append(a1) #contains list of a0

    if (set(a) == set(y)):
        print("Reflexive")
        return (result, True)

    print("Not Reflexive")
    return ([] , False)
R1=reflexive([(1,1),(2,2),(3,3),(4,4)])
print(R1)
#Symmetric
def Symmetric(Relation):
    if all(tup[::-1] in Relation for tup in Relation):
        return True


    return False
S1=Symmetric([(1,2),(2,1),(3,3)])
print("Symmetric:",S1)
#Transitive
def Transitive(relation):
    for a,b in relation:
        for c,d in relation:
            if b == c and ((a,d) not in relation):

                    return False
    return True
T1=Transitive([(1,2),(2,3),(1,3)])
print("Transitive:",T1)
#AntiSymmetric
def Antisymmetric(relation):
    for a,b in relation:
      if (a,b) in relation:
         return False
         return True
A1=Antisymmetric([(2,1),(3,2),(1,2),(2,3)])
print( "Antisymmetric",A1)
#Equivalence
def equivalence(relation):
       return reflexive(relation) and Symmetric(relation) and Transitive(relation)
E1=equivalence([(2,4),(1,2),(3,2),(2,1),(1,3)])
print("Equivalence",E1)
#Partial order
def partial_order(relation):

      return  reflexive(relation) and Transitive(relation) and Antisymmetric(relation)

P1=partial_order([(2,4),(3,2),(3,4),(1,2),(1,3)])
print("Partial order",P1)