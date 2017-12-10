#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:14:34 2017

@author: bhumihar
"""

def valid_sudstr(str1) :
    
    str_len = len(str1);
    str_list = [0 for i in range(str_len)] ;
    for i in range(str_len) :
        strs = str1[:i] ;
        strs_len = len(strs)
        if ((i==0) and ((str1[i]=='a') or (str1[i]=='z'))) :
            str_list[i] = 1;
        elif ((str1[i]=='a') or (str1[i]=='z')) :
            str_list[i] =  strs_len + str_list[i-1]+ 1 ;
        elif((str1[i]!='a') and (str1[i]!='z')) :            
            if (str_list[i-1]==0) :
                str_list[i] = str_list[i-1];
            else :
                rstr = list(reversed(strs));
                
                rstr_a = strs_len
                rstr_z = strs_len
                if 'a' in rstr:
                    rstr_a = rstr.index('a');
                if 'z' in rstr :
                    rstr_z = rstr.index('z');
                if ((strs_len-1-rstr_a) > (strs_len-1-rstr_z)):
                     str_list[i] = str_list[i-1] + (strs_len-1-rstr_a) +1;
                else :
                    str_list[i] = str_list[i-1] + (strs_len-1-rstr_z) +1;
                
    return str_list[-1]                


str2 = 'abbzbba' ;
print(valid_sudstr(str2))