# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:49:38 2020

@author: Andres
"""
with open('input.txt','r') as file:
    data=[int(number) for number in file]
    
l=len(data)-1

def findset1(n,p1,p2):
    s=sum( data[p1:p2] )

    if s==n or p1==l-1: #it ends
        return data[p1:p2]
    if p2==l: #change both pointers
        return findset1( n, p1+1,p1+2 )
    if s < n: #it catches one more number to sum
        return findset1(n , p1, p2+1)
    else:
        return findset1(n, p1+1, p1+2)

def findset2(n , p1, p2):
    p1=0
    p2=2
    s=data[p1:p2]
    while s != n and p1!=l-1:
        s = sum( data[p1:p2] )
        #print(data[p1:p2])
        #print("sum="+str(s)+'\n')
        if p2==l or s > n:
            p2=p1+2
            p1+=1   
        elif s < n:
            p2+=1
            
        
    return data[p1:p2]
            
sol_range=findset2(177777905, 0, 2)
print( min(sol_range) + max(sol_range) )
        
        
    
    