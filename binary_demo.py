#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:03:03 2017

@author: bhumihar
"""

import BinaryTree ;

binary_tree = BinaryTree.BinaryTree(1)
binary_tree.insert_data(2)
binary_tree.insert_data(3)
binary_tree.insert_data(4)
binary_tree.insert_data(5)
binary_tree.insert_data(6)
binary_tree.insert_data(7)
#binary_tree.insert_data(8)
#binary_tree.insert_data(9)
#binary_tree.insert_data(10)
#binary_tree.insert_data(11)
#binary_tree.insert_data(12)
#binary_tree.insert_data(13)

root = binary_tree.get_root()

print('####Preorder Recursion Transversal####')
print(binary_tree.preorder_transversal(root))
print('####Preorder Without Recursion Transversal####')
print(binary_tree.preorder_wr_transversal(root))

print('####Inorder Recursion Transversal####')
print(binary_tree.inorder_transversal(root))
print('####Inorder Without Recursion Transversal####')
print(binary_tree.inorder_wr_transversal(root))

print('####Postorder Recursion Transversal####')
print(binary_tree.postorder_transversal(root))
print('####Postorder Without Recursion Transversal####')
print(binary_tree.postorder_wr_transversal(root))

print('####Postorder Without Recursion Transversal####')
print(binary_tree.levelorder_wr_transversal(root))
