# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 02:39:22 2020

@author: Andres
"""

def op(a,b,c):
        return (a==c and b!=c) or (a!=c and b==c)
    
x=2
y=3
z=2
a=op(x,y,z)
print(a)
