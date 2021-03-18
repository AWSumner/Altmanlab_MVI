#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:09:02 2021

@author: sumphys
"""
'Imports'
import os.path #used in creation of final path
import numpy as np  
import random

total_map=0
'File selection & naming'
Map_name='SL_test_1' #name of map file you want
end_path='./Reference/Maps/' #Final location of the map just in case you want to change it
'Note: you are running this is A_S model the . represents the path the the running directory '
Final_location=os.path.join(end_path,Map_name+'.csv') #creates path for saving the final file


'Type of map'
dim_x=100 # number of entires per row
dim_y=100 # number of rows 

Matrix=np.zeros((dim_y,dim_x)) # Creates an empty map we can iterate on to make the actin network


'Line'
def Line(x,y):  # a function of creating a line
    
    if y==50:  # line you wish to populate 
        slope=2*np.pi#slope of the line you are entering 
        return([True,slope]) #says in network and returns the slope of the graph
    else: 
        return([False]) #not in network
    
'Grid'

def Grid(x,y): #function for creating a grid
    Grid_x=3 # seperation between the cols of the grid
    Grid_y=2 # seperation between the rows of the grid
    
    if x % Grid_x==0: #checks to see if the x position is divisable by the grid speration
    
          if y % Grid_y==0: #checks to see if the y position is divisable by the grid seperation
              val=random.choice([np.pi/2,np.pi]) #randomly chooses the angle at the intesection
              return([True,val]) #tells the code it is in network and that the angle is the random choice above
          
          else: 
              return([True,np.pi]) #tells the code it is in newtork and the the angle is pi
        
    else:
        
        if y % Grid_y==0: #checks to see if the y position is divisable by the grid seperation
              return([True,np.pi/2]) #tells the code it is in network and that the angle is pi/2
          
        else: 
            return([False]) #tells the code it isn't in newtork
     

'Sine'
'to be filled in later'



'Creating the map'

y=0 # y position index reset
for row in Matrix: # seperates out each row
    
    x=0 # x position indexing reset
    for item in row: # looksat each item in that row
       
        Shape=Line(x,y) #Criteria for shape goes here
        if Shape[0]: #sees if it meets the cirteria
            Matrix[y,x]=Shape[1] # changes value
        x+=1    #increase inex by one
        
    y+=1 #increase y index by one

    
#print(Matrix) #testing

np.savetxt(Final_location,Matrix)

print('Done') 


