#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:14:56 2017

@author: bhumihar
"""

inp = input().strip()
count = 1
for i in range(len(inp)) :
    if (inp[i].isupper()) :
        count = count+1
        
print(count)