#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:21:11 2017

@author: bhumihar
"""

inp1 = 6;
inp2 = 4 ;
inp3 = [[1,2],[1,3],[1,4],[5,6]]

#path_dict = {} ;

path = inp2
inp33 = inp3
i =0 ;
while(i<3) :
    result = []
    inp22 =0 ;
    for ix in range(path-1) :
        for jx in range(ix+1,path) :
            a = inp33[ix];
            b = inp33[jx] ;
           # print(a,ix,jx,i)
            #print(b,ix,jx,i)
            if(set(a) & set(b)) :
                inp22 +=1
                #print('val',(set(a) & set(b)))
                result.append([ix+1,jx+1])
                #print(result)
                
    inp33 = result
    path = inp22
    i += 1
            
print(len(result))