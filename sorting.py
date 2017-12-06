#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 21:46:30 2017

@author: bhumihar
"""
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp
        
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while (position > 0) and (a_list[position - 1] > current_value) :
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
        
def merge_sort(a_list):
     print("Splitting ", a_list)
     if len(a_list) > 1:
          mid = len(a_list) // 2
          left_half = a_list[:mid]
          right_half = a_list[mid:]
          merge_sort(left_half)
          merge_sort(right_half)
          i = 0
          j = 0
          k = 0
          while i < len(left_half) and j < len(right_half):
             if left_half[i] < right_half[j]:
                 a_list[k] = left_half[i]
                 i = i + 1
             else:
                 a_list[k] = right_half[j]
                 j = j + 1
                 k = k + 1
          while i < len(left_half):
             a_list[k] = left_half[i]
             i = i + 1
             k = k + 1
          while j < len(right_half):
             a_list[k] = right_half[j]
             j = j + 1
             k = k + 1
     print("Merging ", a_list)
    
            
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubble_sort(a_list)
print(a_list)


selection_sort(a_list)
print(a_list)

insertion_sort(a_list)
print(a_list)

merge_sort(a_list)
print(a_list)
