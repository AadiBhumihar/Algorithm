#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:09:26 2017

@author: bhumihar
"""

import re ;

str1 = 'foo is a boy.\nfoo is man.\nfoo is a child'
                
str2 = 'foo1\nfoo2\n'

val1 = re.findall(r'^foo',str1,re.M);

print(val1)

val2 = re.findall(r'foo.$',str2,re.M);

print(val2)

str3 = '<a> b <c>';

val3 = re.findall(r'<.*?>',str3);

print(val3)

str4 = 'bba ba1 ba1t';

val4 = re.findall(r'ba1\b',str4);

print(val4)