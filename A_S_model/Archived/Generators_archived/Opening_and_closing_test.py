#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:06:32 2020

@author: sumphys
"""

import numpy as np 
import csv 
from PIL import Image #image processing import
import os.path #used in creation of final path


l=[5,8,7,6,5,5,6,5,54,4,4,5,6]


row_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)


with open('protagonist.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



x=[False,0]

if x==False: 
    print('yes')
    
else: 
    print('no')

