# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:46:54 2023

@author: garvi
"""

def pythogorean(n):
    for i in range(3,n+1):
        for j in range(i,n+1):
            for k in range(j,n+1):
                if(i**2 + j**2 == k**2):
                    print(i,",",j,",",k)

n1=int(input())
pythogorean(n1)