#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:20:58 2020

@author: sumphys
"""

import random 
import numpy as np 
import math

def Boltzmann(G):
    kbT=4.2 #pN/nm at room temperature
    Z=sum(([math.exp(-g/(kbT)) for g in G]))
    if Z==0:
        return('No')
    else:
        B=[(1/Z)*math.exp(-g/(kbT)) for g in G]
        #print(B)
        return B

#probability function
#postion shaple is [[],[]]
def Landing_probability(Positions,Potentials):
    
    B=Boltzmann(Potentials)
    if B=='No':
        return('Error in Boltzmann')
    else:
        total=sum(B)
        weighted_potentials=[b/total for b in B]
        p=random.choices(Positions,weights=weighted_potentials,k=1)
        return p

def MIV_Potential(Theta1,Theta2,Phi,Position,Attachment,kf,ks,kps):
    #kf=0.16 #pN/nm
    #ks=0.2 #pN/nm
    stall_check=ks*((Position[0]-Attachment[0])**2+(Position[1]-Attachment[1])**2)**.5 #calculates the force 
    stall_force=2 #pN, the stall foce of the motor
    if stall_check > stall_force: #Checks if the position would exceed the stall force and if so give it a potental that will make the boltzmann return zero so it cannot land there
        G=1e20000 #biiiig number
        
    else:   #if it doesn't exceed stall force
        L=16 #nm
        Torsion=(kf*(L**2)/2)*(Theta1**2+Theta2**2)
        Spring=(ks/2)*((Position[0]-Attachment[0])**2+(Position[1]-Attachment[1])**2)
        Power_stroke=(kps/2)*(Phi**2)
        G=Torsion+Spring+Power_stroke
        
    return(G)




