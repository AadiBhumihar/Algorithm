#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:21:00 2017

@author: bhumihar
"""

def appendAtbegin(x,l) :
    return [x + element for element in l] ;

def bitString(n) :
    if n==0 : return [] ;
    if n==1 : return ['0','1'] ;
    else :
        return (appendAtbegin('0',bitString(n-1)) + appendAtbegin('1',bitString(n-1)))
    
    
print(bitString(40))