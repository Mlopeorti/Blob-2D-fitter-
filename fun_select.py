# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 12:55:08 2016

@author: mlopezo
"""

def point_ans(p):
    if p <=  5 and p >= 0:
        return "No"
    if p >= 5 and p <= 10:
        return "Yes"
        

def frame(p):    
    x1= min(int(p[0]),int(p[2]))
    x2= max(int(p[0]),int(p[2]))
    y1= min(int(p[1]),int(p[3]))
    y2= max(int(p[1]),int(p[3]))
    c_points= [x1,x2,y1,y2]    
    return c_points
    
def center(corners):
    c=[int(0.5*(corners[0]+corners[1])),int(0.5*(corners[2]+corners[3]))]
    return c

def select_image(corner_index,image):
    zoom=image[corner_index[2]:corner_index[3],corner_index[0]:corner_index[1]]
    return zoom  
