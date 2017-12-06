#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:09:11 2017

@author: bhumihar
"""

def RobinKarp(text,pattern) :
    if pattern == None or text == None :
        return -1;
    if pattern == '' or text == '' :
        return -1;
    
    if len(text) < len(pattern) :
        return -1
    
    hashtext = Hash(text,len(pattern));
    hashpattern = Hash(pattern,len(pattern));
    
    hashpattern.updatehash();

    for i in range(len(text)-len(pattern) +1) :
        if (hashtext.hashedvalue()==hashpattern.hashedvalue()) :
            if(hashtext.text()==pattern) :
                return i;
        hashtext.updatehash();
        
    return -1
    
    
class Hash :
    
    def __init__(self,text,size) :
        self.str = text ;
        self.hash = 0 ;
        
        for i in range(0,size) :
            self.hash += ord(self.str[i]);
            
        self.init =0
        self.end = size;
        
    def hashedvalue(self) :
        return self.hash;
    
    def text(self) :
        return self.str[self.init:self.end];
    
    def updatehash(self) :
        
        if self.end <= len(self.str) -1 :
            self.hash -= ord(self.str[self.init]) ;
            self.hash += ord(self.str[self.end]) ;
            self.init += 1 ;
            self.end += 1;
            
print(RobinKarp('asdfghjk','fg'))