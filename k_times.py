#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:40:37 2017

@author: bhumihar
"""

inp_len = int(input()) ;

inp = list(map(int,input().split(' '))) ;

result = []; 
k = int(input())
inp_dict = {} 
for i in inp :
    if  i in inp_dict.keys() and inp_dict[i] < k:
        inp_dict[i] += 1
    else :
        inp_dict[i] = 1


for key in inp_dict.keys():
    if inp_dict[key] == k :
        print(key)
        break ;