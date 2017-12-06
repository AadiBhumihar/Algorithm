#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:17:30 2017

@author: bhumihar
"""
step = 0
class Sorting :
        
    def BubbleSort(self,arr) :
        global step
        for i in range(len(arr)) :
            for j in range(len(arr)-1-i) :
                if (arr[j]>arr[j+1]) :
                    step = step +1
                    temp = arr[j] ;
                    arr[j] = arr[j+1];
                    arr[j+1] = temp ;
                    
                    
        return arr;
    
    
sorting = Sorting();
arr = [5,1,3,2,4]
print(sorting.BubbleSort(arr))
print(step)