#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:16:10 2017

@author: bhumihar
"""

'''It is a classic computer science problem, the basis of diff 
(a file comparison program that outputs the differences between two files),
 and has applications in bioinformatics.'''
 
 #### least optimal solution ######
 

def least_opt_sol(str1,str2) :    
    result_list = [];
    
    str1_len = len(str1) ;
    str2_len = len(str2)
    ix =0 
    
    while(ix<str1_len) :
        res = [] ;
        k =0
        for i in range(ix,str1_len):   
            for j in range(k,str2_len) :
                if str1[i] == str2[j] :
                    res.append(str1[i]);
                    k = j+1;
                    break ;
                    
        result_list.append(res)
        ix += 1;        
    
    val = len(result_list[0])
    
    result = []
    for x in result_list :
        if len(x)>val :
            val = len(x)
            result = x
    return None if not result else result ;
 
 #### Resursive optimal solution  ######

result_matrix  = []
def max_len(a,b) :
    return a if a>b else b ;
 
def recursive_sol(str1,str2) :
 
    
    if ((len(str1)==0) or (len(str2) == 0)):
        return 0;
     
    if ((str1[-1]==str2[-1])) :
        val = 1 + recursive_sol(str1[:-1],str2[:-1])
        
        return val
    
    else : 
        return max_len(recursive_sol(str1,str2[:-1]),recursive_sol(str1[:-1],str2))
     

 #### Dynamic optimal solution  ######

def dynamic_sol(str1,str2) :
    
    count_matrix = [];
    dup = [] ;
    str1_len = len(str1) ;
    str2_len = len(str2) ;
    
    count_matrix = [[0 for x in range(str1_len+1)] for y in range(str2_len+1)]
    
    for ix in range(str2_len) :
        for iy in range(str1_len) :
            if (str1[iy] == str2[ix]) :
                count_matrix[ix+1][iy+1] = count_matrix[ix][iy] +1
            elif (str1[iy] != str2[ix] ):
                count_matrix[ix+1][iy+1] = max_len(count_matrix[ix][iy+1],count_matrix[ix+1][iy])
            dup.append(count_matrix[ix+1][iy+1])
    
    
    max_v = max(dup)
    return max_v ;
    
    
    
 
     
str3 = "ABCDGH" 
str4 = "AEDFHR"
 
str1 = "AGGTAB"
str2 = "GXTXAYB"

result =  least_opt_sol(str1,str3)


if result :      
    print("".join([x for x in result ]))
else :
    print('None')
print(result)

print(recursive_sol(str4,str1))

print(dynamic_sol(str1,str2))