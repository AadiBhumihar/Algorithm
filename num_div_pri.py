#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:06:41 2017

@author: bhumihar
"""
import math;


def find_prime(inp1) :
    
    res = []
    
    for i in range(inp1[0]+1,inp1[1]) :
        flag = 1
        if (i==1) :
            continue ;
        if(i==2 or i==3) :
            res.append(i)
            continue ;
        if(i%2==0 or i %3==0) :
            continue ;
        for j in range(5,int(math.sqrt(i))+1,6) :
            if(i%j==0) or (i%(j+2)==0) :
                flag =0
        if(flag) :
            res.append(i);
            
    return res ;


def return_count(prime_list,n):
    count =0 ;
    for i in range(2,n+1):
        for j in prime_list :
            if (i%j==0):
                count +=1
                break;
    
    return count;

  
l_m = [1,6]

n = 100
result = find_prime(l_m)
if (result) :
    print(return_count(result,n))