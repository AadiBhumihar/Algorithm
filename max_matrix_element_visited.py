#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 02:13:03 2017

@author: bhumihar
"""

inp = [[1,2,3],[2,3,1],[3,1,2]]; #input();

no_rows = len(inp)

no_cols = len(inp[0])

count_matrix =  [[0 for i in range(no_rows)] for j in range(no_cols)] ;

for i in range(no_rows-1,-1,-1) :
    for j in range(no_cols-1,-1,-1) :
        val = inp[i][j]
        
        if ((i+1 < no_rows and j+1 < no_cols) and (val>inp[i+1][j] and val>inp[i][j+1])) :
            #print(i,j,1)
            count_matrix[i][j]  = count_matrix[i+1][j] + count_matrix[i][j+1] + 1
            #print(count_matrix[i][j])
        elif ((i+1 < no_rows and j+1 < no_cols) and (val>inp[i+1][j] and val<inp[i][j+1])) :
            #print(i,j,2)
            count_matrix[i][j]  = count_matrix[i+1][j] + 1
            #print(count_matrix[i][j])
        elif ((i+1 < no_rows and j+1 < no_cols) and (val<inp[i+1][j] and val>inp[i][j+1])) :
            #print(i,j,3)
            count_matrix[i][j]  = count_matrix[i][j+1] + 1
            #print(count_matrix[i][j])
        elif ((i+1 >= no_rows and j+1 < no_cols) and (val>inp[i][j+1])):
            #print(i,j,4)
            count_matrix[i][j]  = count_matrix[i][j+1] + 1
            #print(count_matrix[i][j])
        elif ((i+1 < no_rows and j+1 >= no_cols) and (val>inp[i+1][j])):
            count_matrix[i][j]  = count_matrix[i+1][j]  +1 
            #print(i,j,5)
            #print(count_matrix[i][j])
        else:
            #print(i,j,6)
            count_matrix[i][j]  = 1
            #print(count_matrix[i][j])
    #print('')
        

for i in range(no_rows) :
    for j in range(no_cols) :
        val = count_matrix[i][j]
        print(val,end='')
        
        
    print('')
