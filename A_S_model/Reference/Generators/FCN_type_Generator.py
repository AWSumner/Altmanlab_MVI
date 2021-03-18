#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:14:28 2021

@author: sumphys
"""
'Imports'
import os.path #used in creation of final path
import numpy as np  
import random 
from sympy import *

z=symbols('z')#symbol used in the functions

'inputs'
x_dim=3 #number of entries per row
y_dim=3 #number of rows
Func=[sin(z),cos(z)] # the function(s) you are mapping Note: if you are using a non cont. and/or non diff.able function this code can produce errors (also what is wrong with you?! )
Map_name='SL_test_1' #name of map file you want
Directionality=True #check that determines if you want a 'backwards direction' to be possible ((theta can be (pi/2->pi->-pi/2))) from arctan codomain

'Save paths'
end_path='./Reference/Maps/' #Final location of the map just in case you want to change it
'Note: you are running this is A_S model the . represents the path the the running directory '
Final_location=os.path.join(end_path,Map_name+'.csv') #creates path for saving the final file

'Map'
Matrix=np.zeros((y_dim,x_dim))

'Creating the map'



R=0 #reset the R counter **left over for the reverse list method at the bottom
for Fcn in Func: #does the mapping for each function

    if Directionality: #checks if you want directionality for a given function
        reverse=random.choice([True,False]) #if you want it to randomly choose for each function
       #reverse=True  #if you want to fix it True
       #reverse=False #if you want to fix it False
       
    y=0 # y position index reset
    for row in Matrix: # seperates out each row
    
        x=0 # x position indexing reset
        for item in row: # looks at each item in that row
        
            if (y-1<=Fcn.subs(z,x)<=y+1) or (Fcn.subs(z,(x-1))<=y<=Fcn.subs(z,(x+1)) or (Fcn.subs(z,(x+1))<=y<=Fcn.subs(z,(x-1)))): # check to see if the function (+-1) bound the y value or the y(+-1) values bound the function values 
                deriv=diff(Fcn,z,1) #Takes derivative with respect to z once
                slp=deriv.subs(z,x) # evaluates the slope of the function by subing in the x value
                theta=np.arctan(slp)
                
                if theta <=0: #converts the angle to match the reqirements for the model
                    theta+=2*np.pi #adds two pi
                
                if reverse: 
                    theta+=(-np.pi) # takes the calculated theta and converts it to its reverse
                
                if item==0: #checks to see if the entry is empty
                    Matrix[y,x]=theta #if empty it fills the position with
                
                if item !=0: #check to see if it is not Note: Not an else because it could lead to an error with two ifs above it. 
                    rand=[theta,item] #makes a list of potential values
                    Matrix[y,x]=random.choice(rand) #randomly chooses which value to use at that intersection
                    
                    
            x+=1    #increase index by one
        y+=1 #increase y index by one
    R+=1 #increase R  by one **left over for the reverse list method at the bottom
    

#print(Matrix) #testing




#np.savetxt(Final_location,Matrix)

print('Done')
'''
reverse=[] #reverse list reset
if Directionality: #checks if you want directionailty
    for i in range(len(Func)):  #makes a value for each function
        rev=random.choice([True,False]) # chooses the function
        reverse.append(rev) #adds the rev value to the reverse list

#reverse=[] #Here for if you want to set the reverse list manually
'''