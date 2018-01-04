#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 03:08:37 2018

@author: bhumihar
"""

import re 

def break_up() :
    msg_len = int(input()) ;
    score = 0
    for i in range(msg_len) :
        msg_ = input().strip();
        val = re.findall(r'\d{1,2}',msg_)
        val = [int(i) for i in val ]
        if not val:
            continue
        else :
           for v in val :
               if v == 19 or v == 20 :
                   score = score + v*4;
               else :
                   score = score - v*3
  
    if (score>0):
        print('Date');
    else :
        print('No Date')
            
break_up()