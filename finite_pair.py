#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 01:09:55 2017

@author: bhumihar
"""

a = input().strip()
a = list(map(int, a.split(' ')))
a_size=a[0]
k=a[1]
b = input().strip()
b = list(map(int, b.split(' ')))
i,j =0 ,0
count =0

#b = [int(num) for num in b]
b.sort()
p=1
for i in range(a_size-1) :
    for j in range(p,a_size):
        if((b[j]-b[i])<k):
            continue ;
        elif ((b[j]-b[i])==k):
            count = count+1;
            p  = j+1
            break;
        elif ((b[j]-b[i])>k):
            break ;
print(count)