#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:25:41 2017

@author: bhumihar
"""
import BinaryTree ;

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
     
       
binary_tree = BinaryTree.BinaryTree(31)
binary_tree.insert_data(1)
binary_tree.insert_data(21)
binary_tree.insert_data(9)
binary_tree.insert_data(10)
binary_tree.insert_data(12)
binary_tree.insert_data(18)
binary_tree.insert_data(3)
binary_tree.insert_data(2)
binary_tree.insert_data(8)
binary_tree.insert_data(7)
root = binary_tree.get_root()
result = binary_tree.levelorder_wr_transversal(root)

heap = Heap(11);
result = heap.insert_data(result)
print(result)

def max_heapify(result):
    
    print(len(result))
    heap_size = len(result)//2;
    print(heap_size)
    for indx in range(heap_size) :
        
        max_v = result[indx]
        max_indx = indx
        
        if (2*indx+1<heap_size) :
            #print('okkk:',indx)
            if (result[heap.get_left_child(indx)]>max_v) :
                max_v = result[heap.get_left_child(indx)] ;
                max_indx = heap.get_left_child(indx)
            
        if (2*indx+2<heap_size) :
            #print('okkk:',indx)
            if (result[heap.get_right_child(indx)]>max_v) :
                max_v= result[heap.get_right_child(indx)]
                max_indx = heap.get_right_child(indx) ;
        #print(indx,max_indx)    
        result[max_indx] = result[indx];
        result[indx] = max_v
        
        
    return result;
  
print(max_heapify(result))  

def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y

def heap_sort(result) :
    result[0],result[-1] = swap(result[0],result[-1])
    print(result)
    result[:-1] =max_heapify(result[:-1])
    print("result:",result)
    result[0],result[-2] = swap(result[0],result[-2])
    print(result)
    result[:-2] =max_heapify(result[:-2])
    
    result[0],result[-3] = swap(result[0],result[-3])
    print(result)
    result[:-3] =max_heapify(result[:-3])

    result[0],result[-4] = swap(result[0],result[-4])
    print(result)
    result[:-4] =max_heapify(result[:-4])

    result[0],result[-5] = swap(result[0],result[-5])
    print(result)
    result[:-5] =max_heapify(result[:-5])

    result[0],result[-6] = swap(result[0],result[-6])
    print(result)
    result[:-6] =max_heapify(result[:-6])

    result[0],result[-7] = swap(result[0],result[-7])
    print(result)
    result[:-7] =max_heapify(result[:-7])
    
    result[0],result[-8] = swap(result[0],result[-8])
    print(result)
    result[:-8] =max_heapify(result[:-8])
    
    result[0],result[-9] = swap(result[0],result[-9])
    print(result)
    result[:-9] =max_heapify(result[:-9])

    return result


#print(heap_sort(result))  