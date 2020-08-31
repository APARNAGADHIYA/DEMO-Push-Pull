# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 22:53:36 2020

@author: APARNA
"""

s=0
for i in range(2,11,1):
    s=s+i
    print(s)
print("Sum = ",s)    
print("-------------------------------------------")
print("-------------------------------------------")
s=0
for i in range(11):
    s=s+i
    print("First ",i,"numbers gives sum as", s)
print("-------------------------------------------")
print("-------------------------------------------")
s=0
""" It starts counting from 0 to 1000 """
for i in range(1001):
    s=s+i
    print("First ",i,"numbers gives sum as", s)    
    