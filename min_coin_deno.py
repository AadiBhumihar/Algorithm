#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:21:39 2017

@author: bhumihar
"""


def coin_deno(change_list,rupee):
    
    min_change = rupee;
    
    if rupee in change_list :
        min_change = 1 ;
        return min_change ;
    else :
        for change in [c for c in change_list if c<= rupee] :
            val = 1+coin_deno(change_list,rupee-change);
            if val < min_change :
                min_change = val;
                
        return min_change ;


print(coin_deno([1,5,10,25],30))