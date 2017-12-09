#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:25:41 2017

@author: bhumihar
"""

import random

class Heap :
    
    def __init__(self,size):
        self.heap_list = [0]*size;
        self.size = size
        self.index = -1;
        
    def get_data(self,index):
        if index<self.size :
            return self.heap_list[index]
        else :
            return None ;
    
    def get_parent(self,index):
        if index/2 >0 :
            return index/2 ;
        
    def get_left_child(self,index) :
        if 2*index+1 < self.size :
            return 2*index+1 ;
        
    def get_right_child(self,index) :
        if 2*index+2 <self.size :
            return 2*index+2 ;
    
    def insert_data(self,data) :
       for item in data :
           self.index += 1;
           self.heap_list[self.index] = item;
           
       return self.heap_list;

    def heap_size(self) :
        return len(self.heap_list)

   
     
def max_heapify(result,size):
     
    l_child = 2*size + 1;
    r_child = 2*size + 2;
    h_len = len(result) ;
    largest = size ;
    if (l_child < h_len and result[l_child]>result[size] ) :
        largest = l_child ;
    if(r_child < h_len and result[r_child]>result[largest]) :
        largest = r_child ;
        
    if  (largest != size) :
        result[largest] , result[size] = result[size] , result[largest]
        max_heapify(result,largest)
        
    return result
    
        
    return result;

def build_max_heapify(result) :
    
    result_size = len(result) // 2
    
    for i in range(result_size,-1,-1):
        max_heapify(result,i);
        
    return result
    

def heap_sort(result) :
    val = [];
    result_len = len(result)
    result = build_max_heapify(result);
    for i in range(result_len-1) :
        val.insert(0,result.pop(0))
        result = build_max_heapify(result);
    return val   

heap = Heap(11);
result = [int(10*random.uniform(0,1)) for i in range(11) ]
result = heap.insert_data(result)
print(result)

result = build_max_heapify(result);
print(result)


print(heap_sort(result))  