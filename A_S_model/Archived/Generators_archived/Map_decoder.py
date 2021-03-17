#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:37:46 2021

@author: sumphys
"""

'Imports & functions'
from PIL import Image #image processing import
import os.path #used in creation of final path
import numpy as np  
import csv 
import pandas as pd
import cv2
import utils
import os 

'File selection & naming'
Image_name='16_Test.png' #name of image to convert to map
End_name='Test_031620_1' #the final name you want to give the map 'Name_date_version'
start_path='./Reference/Maps/' #path to origional map 
end_path='./Reference/Images/' #Final location of the image just in case you want to change it
'Note: As this file is in Generators one dot take you up one directory to A_S_model. '

Map_file=os.path.join(start_path,Image_name)

with open(Map_file, newline='') as f:
    reader = csv.reader(f)
    Map = list(reader) #creates an array Map that holds the values for each pixel. 

