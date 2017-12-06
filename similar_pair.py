#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 04:02:33 2017

@author: bhumihar
"""

import math

val = input().split();
val = list(map(int,val))

dict1 = {}
count = 0
for ix in range(val[0]-1) :
    node = input().split();
    node = list(map(int,val))
    print(node)
    c = node[1]
    p = node[0]
    dict1[str(c)] =  p;
    keyv = p;
    while (keyv!=None) :
        if(c-p<=val[1]) :
            count = count +1;
            #print(c,p)
         
        c = int(keyv)
        keyv = dict1.get(str(keyv));
        if (keyv != None) :
            p = int(keyv)
        #print(count)
        
  