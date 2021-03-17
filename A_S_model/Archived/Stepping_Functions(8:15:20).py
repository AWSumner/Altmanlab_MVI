#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:19:45 2020

@author: sumphys
"""

import numpy as np


def Map_Cut(Map,point,dis):
    '''
    Map: The map file that you are cutting a portion of
    point: The point where you are cutting around
    dis: the distance from the inital point you are cutting at
    '''
    x=point[0]
    y=point[1]
    
    if  x<dis or x+dis>len(Map[0]) : #These checks are related to keeping the model "physical"
        return("Too close to an edge") #Becasue reality has no edges so when the motor get near an edge we don't want to deal with it
    
    if  y<dis or y+dis>len(Map): #So I added checks to check for hitting an edge before running the trim 
        return("Too close to an edge") 

    else:
        y_trim=Map[y-dis:y+dis] #removes all the rows that are not in the search window
        trimmed_map=[] #reset the trimmed map
        for n in len(y_trim):
            trim=y_trim[n] #renaming for clairity
            x_trim=trim[x-dis:x+dis] #removes elements from the rows that are outside the search window
            trimmed_map.append(x_trim) #adds it to the trimmed map
         
        inverse=[len(Map[:y-dis+1]),len(Map[0][:x-dis+1])]   
        return(np.array(trimmed_map),inverse) 
    
    

def Distance_Maps(size,dis,point,bound):
    ''' size: The size of the square matrix that will be produced
        dis: The distance from the point that you are looking for
        point: The point you are attached at and there the reference point for the distance
        bound: The extra +-n that is added onto the 
        note: Point must be scaled for this matrix not the same as location on the proper map 
    '''
    xi=point[0]
    yi=point[1]
    
    'Building Identity'
    ''' This bit of code is to build a matrix with 1's in the postions of interest 
    aka points with distance within the range of dis-bound<x<dis+bound
    ''' 
    Identity=[[0 for q in range(size)] for r in range(size)] #makes an maxis with all zeros
    
    for i in range(size): #y value
        for n in range(size): #x value
            distance=round(((n-xi)**2+(i-yi)**2)**.5)
            if dis-bound<=distance<=dis+bound:
                Identity[i][n]=1
                
    'Building Distance'
    ''' 
    This bit is building a companion matrix that has the same non zero entries as Identity  
    but instaed of ones has the ditance at each point recorded 
    '''
    Distance=[[0 for t in range(size)] for u in range(size)]    
  
    for i in range(size): #y value
        for n in range(size): #x value
            distance=round(((n-xi)**2+(i-yi)**2)**.5)
            if dis-bound<=distance<=dis+bound:
                Distance[i][n]=distance
      
    return(np.array(Identity),np.array(Distance))
    
def Landing_Sites(Map,dis):
    ''' Map: THe map you are going to pull out the locations from
        dis: The desired distance to pull stuff out from. 
    This bit of code takes the map and pulls out all the potential landing sites
    and pulls out their coordinates. what you need to feed in is a map that has zeros 
    at all non landing site locations
    '''
    sites=[]
    
    for i in range(len(Map)): #y value
        for n in range(len(Map[0])): #x value
            if Map[i][n]>0:
                sites.append([[n,i]])
                
    return(sites)

def Map_conversion(sites,inverse):
    ''' This bit of code converts from the smaller map use of site selection 
    into coordinates on the big map. This isn't strictly nessisary but if in future 
    a more cleaver/interesting transform comes along just want to have this here
    '''
    
    for item in sites:
       item[0]+=inverse[0] #for each x coordinate translates it with dis+bounds
       item[1]+=inverse[1] #for each y coordinate translates it with dis+bound
        
            
    return(sites)



Dm=Distance_Maps(10,2,[5,5],1)





