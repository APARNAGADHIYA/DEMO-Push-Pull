# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:02:29 2020

@author: APARNA
"""
name= input("What is your Name ")
print("My name is ",name)
amount=int(input("Enter the price of the item "))
print("The price is",amount)
print("The type of amount is ",type(amount))
discount= 0.1*amount
print("The discount offered is ",discount)
sp= amount-discount
print("The final selling price of the product is ", sp)
num =int(10.45)
print(num)
"""This gives error num1= int("10.45") print(num1)"""