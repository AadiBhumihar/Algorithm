#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:56:58 2017

@author: bhumihar
"""

def unique_v(str1) :
    unique = []
    for char in str1[::]:
        if char not in unique:
            unique.append(char)
    return len(unique);

def unique_val(str1):
    sdict = {}
    for j in range(1,len(str1)+1) :
        for i in range(0,len(str1)) :
            if(i+j<=len(str1)) :
                #print(str1[i:i+j])
                sdict[str1[i:i+j]] = unique_v(str1[i:i+j])
    return sdict
        
str1 = input()
#print(str1)
val = unique_v(str1)
print(val)
dictv = unique_val(str1)
for i in range(1,val+1) :
    d = filter(lambda x:x==i,dictv.values())
    print(len(list(d)))
    
    
    
def unique_v(str1) :
    unique = []
    for char in str1[::]:
        if char not in unique:
            unique.append(char)
    return len(unique);

def unique_val(str1):
    count = 0
    unval = []
    for j in range(1,len(str1)+1) :
        for i in range(0,len(str1)) :
            if(i+j<=len(str1)) :
                count += 1
                #print(str1[i:i+j])
                unval.append(unique_v(str1[i:i+j]))
    #print(count)
    return unval
        
str1 = input()
#print(str1)
val = unique_v(str1)
print(val)
univ = unique_val(str1)
for i in range(1,val+1) :
    d = filter(lambda x:x==i,univ)
    print(len(list(d)))
    
    
def unique_val(str1):
    count = 0
    unval = []
    for j in range(1,len(str1)+1) :
        for i in range(0,len(str1)) :
            if(i+j<=len(str1)) :
                count += 1
                #print(str1[i:i+j])
                unval.append(len(set(str1[i:i+j])))
    #print(count)
    return unval
        
str1 = input()
#print(str1)
val = len(set(str1))
print(val)
univ = unique_val(str1)
for i in range(1,val+1) :
    print(univ.count(i))