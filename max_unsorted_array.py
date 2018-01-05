#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:33:11 2018

@author: bhumihar
"""


''' 
   Sample Input 
'''
   
t = 2
test_case_len = ('11',
                 '9')

test_case = ('10 12 20 30 25 40 32 31 35 50 60',
             '0 1 15 25 6 7 30 40 50')

''' 
   Code
'''
   
tn = 0
while(tn<t) :
    mar1 = 0
    mar2 =0

    mar1_in = -1
    mar2_in = -1
    
    res1 = -1
    res2 = -1
    
    val_len = int(test_case_len[tn])
    val = test_case[tn]
    val = list(map(int,val.split(' ')))
    for i in range(1,val_len) :
        prev = val[i-1]
        curr = val[i]
        if curr < prev :
            mar1 = prev
            mar1_in = i-1
            break ;

    for i in range(mar1_in,val_len) :
        prev = val[i-1]
        curr = val[i]
        if curr < prev :
            mar2 = curr
            mar2_in = i
    
    ind_arr = val[mar1_in:mar2_in+1]        
    val1 = min(ind_arr)
    val2 = max(ind_arr)
    
    for i in range(0,mar1_in):
        if val1 < val[i] :
            res1 = i
    
    for i in range(mar2_in,val_len):
        if val2 > val[i] :
            res2 = i

    if (res1 == -1) : res1 = mar1_in
    if (res2 == -1) : res2 = mar2_in            
            
    
    print(str(res1) +' '+ str(res2))
    
    tn = tn +1       
    