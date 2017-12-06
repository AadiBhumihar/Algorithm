#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:20:55 2017

@author: bhumihar
"""

step =0
step1 =0
step_result = [0 for i in range(63)]

def min_coin(c,n) :
    global step
    step = step +1
    mincoin = n 
    if step_result[n-1]!=0:
        return step_result[n-1]
    elif (mincoin in c):
        return 1;
    else :
        for i in [coin for coin in c if (coin<= n)] :
            numcoin = 1 + min_coin(c,n-i)
            if (numcoin<mincoin) :
                mincoin = numcoin;
    return mincoin


def dyn_min_coin(c,n) :
    for i in range(1,n+1) :
        step_result[i-1] = min_coin(c,i)
    return step_result[n-1]

    
print(dyn_min_coin([1,5,10,25],63))
print(step)
print(step_result)