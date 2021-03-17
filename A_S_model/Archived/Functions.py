#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:00:13 2020

@author: sumphys
"""

import random 
import numpy as np 
import math


def Potentials(Theta1,Theta2,Position,Attachment):
    kf=0.16 #pN/nm
    ks=0.2 #pN/nm
    L=16 #nm
    Torsion=(kf*(L**2)/2)*(Theta1**2+Theta2**2)
    Spring=(ks/2)*((Position[0]-Attachment[0])**2+(Position[1]-Attachment[1])**2)
    G=Torsion+Spring
    return(G)


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

print("done")