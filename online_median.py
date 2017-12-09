#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:20:00 2017

@author: bhumihar
"""

def bubble_sort(a) :
    
    a_len = len(a) 
    
    for i in range(a_len-1) :
        for j in range(a_len-i-1) :
            if (a[j]>=a[j+1]) :
                a[j+1],a[j] = a[j],a[j+1]
    
    return a

def selection_sort(a) :
    a_len = len(a);
    for i in range(a_len) :
        temp = a[i]
        min_inx = i
        for j in range(i+1,a_len):
            if(temp>a[j]):
                temp= a[j]
                min_inx = j
        
        a[i],a[min_inx] = a[min_inx],a[i]

    return a

def insertion_sort(a) :
    
    a_len = len(a);
    
    for i in range(1,a_len) :
        temp = a[i]
        j=i-1
        while(temp<a[j] and j>=0) :
            a[j+1] = a[j];
            j =j-1
        a[j+1]=temp
        
    return a
    

a1 = [4,3,2,1]
print(bubble_sort(a1))
print(selection_sort(a1))
print(insertion_sort(a1))