#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:18:14 2020

@author: sumphys
"""


def Potentials(Theta1,Theta2,Position,Attachment):
    kf=0.16 #pN/nm
    ks=0.2 #pN/nm
    L=16 #nm
    Torsion=(kf*(L**2)/2)*(Theta1**2+Theta2**2)
    Spring=(ks/2)*((Position[0]-Attachment[0])**2+(Position[1]-Attachment[1])**2)
    G=Torsion+Spring
    return(G)

