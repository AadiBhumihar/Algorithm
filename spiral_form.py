#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:43:02 2017

@author: bhumihar
"""

import numpy as np 

spi_mat1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]);
#spi_mat1 = np.array([[1,2,3],[5,6,7],[9,10,11],[13,14,15]]);
#spi_mat1 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
r,c = np.shape(spi_mat1)
i,j =0,0
k,l = 0,0
sr, sc = 0,0
lr,lc=r-1,c-1
while(True) :

    if(sc>lc):
       break;
    for j in range(sc,lc+1) :
        print('1:',spi_mat1[i][j],)    
    sr = sr+1
    
    if(sr>lr):
       break;
    for i in range(sr,lr+1):
        print('2:',spi_mat1[i][j],)   
    lc = lc-1
    
    
    if(lc<sc):
       break;
    for j in range(lc,sc-1,-1):
        print('3:',spi_mat1[i][j],)        
    lr = lr-1;
    
    if(lr<sr):
       break;
    for i in range(lr,sr-1,-1):
        print('4:',spi_mat1[i][j],)
    
    sc = sc+1
       