#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 18:12:00 2017

@author: bhumihar
"""
class Node:
    def __init__(self):
        self.data = None # contains the data
        self.right = None # contains the reference to the right node
        self.left = None # contains the reference to the right node
        
class BinaryTree :
    def __init__(self,data):
        self.root = None
        node = Node()
        node.data = data
        node.left = None
        node.right = None
        self.root = node
    def get_data(self) :
        return self.root.data;
     
    def get_left(self) :
        return self.root.left ;
    
    def get_right(self) :
        return self.root.right;

    def get_root(self) :
        return self.root;
         
    def insert_data(self,data) :
        node_que = []
        tail = None
        node_que.append(self.root)
        while(node_que):
            
            tail = node_que.pop(0)
            if(tail.left):
                
                node_que.append(tail.left)
            else :
                
                new_node = Node()
                new_node.data = data
                new_node.left = None
                new_node.right = None
                tail.left = new_node
                return ;
            
            if(tail.right):
                
                node_que.append(tail.right)
            else :
                
                new_node = Node()
                new_node.data = data
                new_node.left = None
                new_node.right = None
                tail.right = new_node
                return
            
    def preorder_transversal(self,root,result=[]):
        
        if not root :
            return ;
        result.append(root.data);
        self.preorder_transversal(root.left,result)
        self.preorder_transversal(root.right,result)
        return result
    
    def inorder_transversal(self,root,result=[]):
        
        if not root :
            return ;
        self.inorder_transversal(root.left,result)
        result.append(root.data);
        self.inorder_transversal(root.right,result)
        return result
    
    def postorder_transversal(self,root,result=[]):
        
        if not root :
            return ;
        self.postorder_transversal(root.left,result)
        self.postorder_transversal(root.right,result)
        result.append(root.data);
        return result
    
    def preorder_wr_transversal(self,root,result=[]):
        node_que = []
        node_que.insert(0,root)
        while(node_que) :
            tail = node_que.pop(0)
            result.append(tail.data)
            if (tail.left) :
                node_que.insert(0,tail.left)
            if(tail.right) :
                node_que.insert(1,tail.right)
        return result

    def postorder_wr_transversal(self,root,result=[]):
        if not root :
            return
        node_que = []
        visited = []
        tail = root
        while(node_que or tail) :
            if(tail!=None) :
                node_que.append(tail)
                tail = tail.left
            else :
                tail = node_que.pop()
                if(tail.right and not tail.right in visited):
                    node_que.append(tail)
                    tail =tail.right
                else:
                    visited.append(tail)
                    result.append(tail.data)
                    tail = None
        return result
    
    def inorder_wr_transversal(self,root,result=[]):
        if not root :
            return
        node_que = []
        tail = root
        while(node_que or tail) :
            if(tail!=None) :
                node_que.append(tail)
                tail = tail.left
            else :
                tail = node_que.pop()
                result.append(tail.data)
                tail =tail.right
        return result
    
    def levelorder_wr_transversal(self,root,result=[]):
        if not root :
            return
        node_que = []
        node_que.append(root)
        while(node_que) :
            tail = node_que.pop(0)
            result.append(tail.data)
            if tail.left :
                node_que.append(tail.left)
            if tail.right :
                node_que.append(tail.right)
        return result

