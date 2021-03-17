#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:19:45 2020

@author: sumphys
"""

import numpy as np
import math

def Distance_Maps(size,dis,point,bound):
    ''' size: integer The size of the square matrix that will be produced
        dis: integer The distance from the point that you are looking for
        point: array The point you are attached at and there the reference point for the distance
        bound: array The extra +-n that is added onto the 
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
    This bit is building a companion matrix that has the same entries as Identity  
    except instaed of 1's has the distance at each point
    '''
    Distance=[[0 for t in range(size)] for u in range(size)]    
  
    for i in range(size): #y value
        for n in range(size): #x value
            distance=round(((n-xi)**2+(i-yi)**2)**.5)
            if dis-bound<=distance<=dis+bound:
                Distance[i][n]=distance
      
    return(np.array(Identity),np.array(Distance))


def Map_Cut(Map,point,dis): 
    '''
    Map: The map file that you are cutting a portion of
    point: The point where you are cutting around
    dis: the distance from the inital point you are cutting at
    '''
    x=int(point[0]) #turning the input points into integers to "santize" them to prevent errors. 
    y=int(point[1]) #should be integers coming in but just in case
    
    if  x<dis or x+dis>len(Map[0]) : #These checks are related to keeping the model "physical"
        return("Too close to an edge") #Becasue reality has no edges so when the motor get near an edge we don't want to deal with it
    
    if  y<dis or y+dis>len(Map): #So I added checks to check for hitting an edge before running the trim 
        return("Too close to an edge") 

    else:
        ymin= y-dis #Lower bound
        ymax=y+dis+1 #Upper bound adding the one so it is a square around the center point
        y_trim=Map[ymin:ymax] #removes all the rows that are not in the search window
        trimmed_map=[] #reset the trimmed map
        for n in y_trim:
            xmin=x-dis #Lower bound
            xmax=x+dis+1 #upper bound with +1 to make it square aound the center point
            x_trim=n[xmin:xmax] #removes elements from the rows that are outside the search window
            trimmed_map.append(x_trim) #adds it to the trimmed map
         
        return(np.array(trimmed_map),[xmin,ymin]) #returns the trimmed map and a ordered pair to convert back to the coordinates on the original map


def Landing_Sites(Map):
    ''' Map: The map you are going to pull out the locations from
    This bit of code takes the map and pulls out all the potential landing sites
    and pulls out their coordinates. what you need to feed in is a map that has zeros 
    at all non landing distance locations
    '''
    sites=[]

    for i in range(len(Map)): #y value
        for n in range(len(Map[i])): #x value
            if Map[i][n]>0:
                sites.append([n,i])
                
    return(sites)


def Conversion(site,transform):
    '''site: array with ordered pair to be converted to cut coordinates
        Transform: the corrisponding transform
    '''
    'Used for converting to cut map coordinates'
    #print(sites)
    new=list(np.array(site)-np.array(transform)) #for each x coordinate translates it with dis+bounds
      
    return(new)
 
    
def Inverse(site,transform):
    ''' Sites: array with ordered pair to be converted back to Map coordinates
        Transform: the corrisponding transform
    '''
    'Used for converting back to origional map coordinates'

    new=list(np.array(site)+np.array(transform)) #for each x coordinate translates it with dis+bounds
      #for each y coordinate translates it with dis+bounds
        
    return(new)


def Angle_Calc(H1,H2,Lstep):
    ''' H1: Array, location of the first head
        H2: Array, loaction of the second head
        Lstep: Integer, length of the lever arm
    '''
    Hx=H1[0]-H2[0] #difference in x
    Hy=H1[1]-H2[1] #difference in y
    theta=math.acos(Hx/Lstep) #computes the current angle 
    
    return(theta)


def Step(Map,point,dis,bound):
    Cut=Map_Cut(Map,point,dis+bound) #uses the cut command to cut a section of the map out around a point
    new_point=Conversion(point,Cut[1]) #converts the origional point to the new coordinates
    
    size=len(Cut) #definition that makes sure the Dis Map and Cut Map have the same size
    Dis_Map=Distance_Maps(size,dis,new_point,bound)
    Mult=np.multiply(Cut[0],Dis_Map[0]) #multiplies Cut and Dis_map entry by entry
    Converted_locations=Landing_Sites(Mult)
    
    locations=[]
    for item in Converted_locations: #Takes each point and converts it back to the original map coordinates
        new=Inverse(item,Cut[1])
        locations.append(new)
        
    return(locations) 



'''

#Dm=Distance_Maps(10,2,[5,5],1))
#M=[[0,1],[2,3],[4,5],[6,7]]
#print(M[0][0])

'''

