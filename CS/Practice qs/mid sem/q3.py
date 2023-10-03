# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:56:55 2023

@author: garvi
"""

def func(a,n):
    sum=0
    for i in range(1,n+1):
        sum+= (a**i)/factorial(i-1)
    return sum
        
def factorial(x):
    if(x<1):
        return 1
    else:
        return x*factorial(x-1)
    
a1=int(input())
n1=int(input())
print(func(a1,n1))