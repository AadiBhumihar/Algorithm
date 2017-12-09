#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:00:53 2017

@author: bhumihar
"""

#### least optimal solution ######
 

def least_opt_sol(inp1) :    
    
    inp_len = len(inp1)
    result_list = []
    for ix in range(inp_len) :
        val_list = []
        val = inp1[ix]
        val_list.append(val)
        for iy in range(ix,inp_len) :
            if (val<inp1[iy]) :
                val = inp1[iy]
                val_list.append(inp1[iy])
        if val_list:
            result_list.append(val_list)
    
    vall = len(result_list[0])    
    for x in result_list :
        if len(x)>vall :
            vall = len(x)
            result = x
    return (None,0) if not result else (result,vall) ;
        
 
 #### Resursive optimal solution  ######

def recursive_opt_sol(inp1) :  
    
    inp_len = len(inp1) ;
    
    if (inp_len==1) :
        return 1 ;
    
    maxend = 1;
    
    for i in range(inp_len-1) :
        val = recursive_opt_sol(inp1[:i+1])
        if (inp1[i]<inp1[inp_len-1]) :
            val =2 ;
            
    return val
    

inp1 = [50, 3, 10, 7, 40, 80]
inp2 = [3,10,20,1,2,3,4,1,25,26]
#print(least_opt_sol(inp1))
inp3 = [10,22,25]
print(recursive_opt_sol(inp3))