#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 03:14:04 2017

@author: bhumihar
"""


import re
import sys


def ext_fib() :
    inp = input().split()
    inp = list(map(int, inp))
    fib = [None] * int(inp[2])
    fib[0],fib[1] = inp[0] ,inp[1]
    for i in range(2,len(fib)) :
        fib[i] = fib[i-2] + (fib[i-1]*fib[i-1])
    print(int(fib[-1]))

def abb_pro() :
    remove_lower = lambda text: re.sub('[a-z]', '', text) 
    inp = int(input())
    ix = 0
    while(ix<inp) :
        i=0
        indx = []
        val =-1
        found =1 
        ix =ix+1
        a = input()
        b = input();
        al = a.lower();
        bl = b.lower();
        for i in range(len(b)) :
            if(a.find(b[i],val+1)!=-1) :
                val = a.find(b[i],val+1)
            else :
                val = al.find(bl[i],val+1)
            if(val==-1) :
                found = 0
                break ;
            indx.append(val)
        a = "".join(c.upper() if i in indx else c for i, c in enumerate(a))
        a = remove_lower(a)
        if(a!=b) :
            found = 0
        print(a)
        print(indx)
        if(found) :
            print('YES')
        else :
            print('NO')
        


q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    r = [None] *x
    
    
inp = int(input())
ix = 0
while(ix<inp) :
    i=0
    indx = 0
    found =1 
    ix =ix+1
    a = input().lower();
    b = input().lower();
    for i in range(len(b)) :
        indx = a.find(b[i],indx)
        if(indx==-1) :
            found = 0
            break ;
    if(found) :
        print('YES')
    else :
        print('NO')
























