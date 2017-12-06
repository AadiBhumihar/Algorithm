#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 02:30:21 2017

@author: bhumihar
"""

import math


T = int(input().strip())
for a0 in range(T):
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    # your code goes here
    minv = (q[2]*(q[2]+1))/2
    maxv = (q[2]*(2*q[1]-q[2]+1))/2
    val = []
    if(q[0]>maxv or q[0]<minv) :
        print('-1')
        continue;
    else :
        val = [i+1 for i in range(q[2])]
        qui = math.floor((q[0]-minv)/q[2])
        rem = ((q[0]-minv)%q[2])
        val = list(map(lambda x:x+qui, val))
        j = len(val)-1
        while (j<=len(val)-1) and (j>=len(val)-rem) :
            val[j] = val[j] +1
            j = j-1
    print(" ".join(str(x) for x in val))