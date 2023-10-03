# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:04:25 2023

@author: garvi
"""

def hcf(a,b):
    if(a%b==0):
        return b
    else:
        return hcf(b,a%b)
    
    
a1=int(input())
b1=int(input())
print(hcf(a1,b1))