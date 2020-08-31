# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:39:13 2020

@author: APARNA
"""

""" We are going to print a table of a number which is input from user """
 
t= int(input(" Please enter any number of your choice.")) 
print("The table of number ",t," will be printed.")
for i in range (1,11):
    print(t, "X", i, "=", t*i)