#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:47:17 2020

@author: sumphys
"""
'''Overview: 


'''
'Imports & functions'
from PIL import Image #image processing import
import os.path #used in creation of final path


'File selection & naming'
Image_name='Test.png' #name of image to convert to map
End_name='Test_071020_3' #the final name you want to give the map 'Name_date_version'
start_path='./Reference/Images/' #path to origional file 
end_path='./Reference/Maps/' #Final location of the map just in case you want to change it
'Note: As this file is in Generators one dot take you up one directory to A_S_model. '


'Path creation'
Starting_location=os.path.join(start_path,Image_name) #creates path to image you are converting to a map
Final_location=os.path.join(end_path,End_name+'.txt') #creates path for saving the final file
'''This bit of code takes the strings given above and stiches them into paths for the files to 
save and load.'''


'Reading RGB and values'
im=Image.open(Starting_location) #what image are you opening?
pix    =im.load() #Actually loads the file of interest
width  =im.size[0] #x dimension in pixels
height =im.size[1] #y dimension in pixels
'Note: pix[x,y] is the RGB value of the pixel at a point (x,y)'


'Map construction'
c=0.008224 #this is the conversion constant between the sum of the RGB and the corrisponding angle 
        # tunes so a maxium sum of RGB minius one (764) produces 2 pi radians and also represents our resolution  

total_map=[] #reset for total map array
for n in range(0,height):
    row=[] #reset for the next row
    for i in range(0,width):
        RGB=sum(pix[i,n])
        
        if RGB==765:
            theta=-1 #sets theta to -1 to indicate pixel is not part of the actin network
        else:
            theta=c*RGB #converts RGB to the theta. 
               
        element=[i,n,theta] #storage of the angle at a specific point
        row.append(element) #adds the element to the row
        
    total_map.append(row) #adds the row to the final array


'Writing to a file'
with open(Final_location, 'x') as file: # the 'x' is what tell open to create the file
    file.writelines("%s\n" % k for k in total_map) #writes the list into the file
    file.close() #closes the file when it is done with it
print('Done') 