#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:24:38 2017

@author: bhumihar
"""

space_str = []
step =0
def str_space(inp) :
    global step
    space_str = []   
    inp_len = len(inp)
    if(inp_len<=1) :
        return list(inp);
    for i in range(inp_len) :
        step =step+1
        st = str_space(inp[:i]) 
        if not st:
            val = inp[i:];
            space_str.append(val)
        else :
            for item in st: 
                step = step+1
                val = item + ' ' + inp[i:]
                space_str.append(val)
    return space_str;
    
inp = "ABCDE"
inp_len = len(inp)


#print(str_space(inp))
for i in range(inp_len) :
    print(step)