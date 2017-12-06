#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 19:04:50 2017

@author: bhumihar
"""

def rep_character(struct) :
    str_len = len(struct);
    count = [0]*256;
    for i in range(str_len) :
        if(count[ord(struct[i])]==1) :
            return True,i ;
        else :
            print("Enter:",ord(struct[i]))
            count[ord(struct[i])] = 1
    if(i==str_len-1):
        return False;
    

word = "abcdefvn"
a = rep_character(word)
if(a) :
    print("First Repeating Character:")
else :
    print("Non-Repeating Character")