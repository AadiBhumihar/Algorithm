#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:17:45 2017

@author: bhumihar
"""

inp = input().strip()
inp = int(inp)

count = 0
#arr = [i for i in range(inp)]
varr = [2 for i in range(inp)]

result = []
for i in range(0,inp,2) :    
    for j in range(i+1,inp) :
        n = inp-i-j
        if ((0<=n <inp) and (varr[n] ==2)and (varr[j] ==2)and (varr[i] ==2)) :            
            result.append((i,j,n))
            count = count+1
            varr[i] = 0
            varr[j] = 0
            varr[n] = 0

i=0   
count = count*3         
print(count)

for i in range(len(result))  :
    sub_result = []
    print(" ".join(str(x) for x in result[i]))
    print(result[i][2],result[i][0],result[i][1])
    print(result[i][1],result[i][2],result[i][0])
    