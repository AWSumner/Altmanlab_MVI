#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:54:28 2020

@author: sumphys
"""

'''Notes: This is the bit of code where I determine the landing probabilities 
and pick a location.
'''
import random 
import numpy as np 
import math

def Boltzman(G):
    kbT=4.2 #pN/nm at room temperature
    Z=sum([math.exp(-g/(kbT)) for g in G])
    B=[(1/Z)*math.exp(-g/(kbT)) for g in G]
    #print(B)
    return B


#probability function
#postion shaple is [[],[], etc.]
def Landing_probability(Positions,Potentials):
    
    B=Boltzman(Potentials)
    total=sum(B)
    weighted_potentials=[b/total for b in B]
   # print(total)
    p=random.choices(Positions,weights=weighted_potentials,k=100)
   
    return p

'''
Testing
j=np.array([5,3,12,5])
pos=[0,1,2,3]
k=Landing_probability(pos,j)
zero= k.count(0)
one=k.count(1)
two=k.count(2)
three=k.count(3)
print(zero,one,two,three)
'''