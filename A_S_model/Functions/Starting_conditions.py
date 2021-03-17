#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:19:52 2020

@author: sumphys
"""

import numpy as np 
import math 
import random
from Functions import Stepping_Functions as SF


def Heads_Placement(P_C,Map,dis,bound):
    '''P_C: False or array. Determines if randomly placed 
       Map: The map you are placing the motor on
       dis: integer Distance of step length
       bound: integer error bars on step size
    '''
    if P_C == False: 
        H1=0
    
    else: 
        H1=P_C

    
    'H2 position'
    
    locations=SF.Step(Map,H1,dis,bound)  
    H2=random.choice(locations) #chooses a random landing site
    
     #call H2_hunt to find a second position
        
    return(H1,H2)
    
     
def Bead_Placement(H1,H2,Number_of_Motors,Radial_Placment,r,Lspring,Lstep):
    ''' H1: array with position of H1
        H2: array with position of H2
        Number of motors: int 
        Radial_placement: boolean
        r: radius of bead
        Lspring: float rest length of spring 
    '''
    
    'angle of attachments'
    phi=[] #reset of the angle list
    if Radial_Placment ==True and Number_of_Motors>1: 
        for i in range(Number_of_Motors):
            if i==0: #this check makes sure the first angle is the zero angle origin
                temp=0
            else:
                temp=random.uniform(0,2*np.pi) #random choice of angles between 0-2*pi for other motors
            phi.append(temp)  #add it to the list!
            
    else:
        for i in range(Number_of_Motors): #creates an incrimenting series of angles for radial placement
            temp=i*2*np.pi/Number_of_Motors
            phi.append(temp) #add it to the list
    
    theta=SF.Angle_Calc(H1,H2,Lstep) #Computes the total angle of the system 
    

    CM=[(H1[0]+H2[0])/2,(H1[1]+H2[1])/2] #compute the center of mass for the motor
    
    'determining origin point location'
    px=CM[0]+Lspring*math.sin(theta)
    py=CM[1]-Lspring*math.cos(theta)
    origin=[px,py]
    bead_center=[px+r*np.sin(theta),py+r*np.cos(theta)]
    #print(point)
    
    'Creating placements'
    attachment_list=[]
    
    for i in range(Number_of_Motors): #this loop finds the locations of attachment points based off the first
       x=r-r*math.cos(phi[i]) 
       y=r*math.sin(phi[i])
       #print(x,y)
       dx=x*math.cos(theta)-y*math.sin(theta) #compute offset in x
       dy=x*math.sin(theta)+y*math.cos(theta) #compute offset in y
       
       location=[origin[0]+dx,origin[1]+dy]
       attachment_list.append(location)
          
    
    return(attachment_list,phi,bead_center)


'VVV Still needs work VVV'
def Other_Heads(Map,attachment_list,angle,Lstep,Lspring,Heads,bound):
    number_of_motors=len(attachment_list)
    phi=angle.pop(0)
    Attachments=attachment_list.pop(0) #removes the first element of the list that is attachment for the first motor
    
    theta=SF.Angle_Calc(Heads[0],Heads[1],Lstep)
    
    Heads=[]
    for item in Attachments:
        
        dx=item[0]+5
        dy=item[1]+4
        point=[dx,dy]
        
        H1_locations=SF.Step(Map,point,round(Lstep/2),bound)
        H1=random.choice(H1_locations)
        H2_locations=SF.Step(Map,H1,Lstep,bound)
        H2=random.choices(H2_locations)
        
        H=[H1,H2]
        Heads.append(H)
        
    return(Heads)







