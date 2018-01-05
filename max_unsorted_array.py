#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:33:11 2018

@author: bhumihar
"""

t = int(input())
print(t)
tn = 0
while(tn<=t) :
    mar2 =0
    tn = tn +1
    #print(input())
    val_len = 11
    val = input()
    val = list(map(int,val.split(' ')))
    for i in range(1,val_len) :
        prev = val[i-1]
        curr = val[i]
        if curr < prev :
            mar2 = prev
    print(tn)        
    