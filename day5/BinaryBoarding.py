# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:16:24 2020

@author: Andres
"""
#PART 1

with open('seats.txt','r') as file:
    data=file.readlines()
    
from math import *

def FindRow(code,i,beg,end):
    if i<6:
        if code[i]=='F':
            return FindRow(code,i+1, beg , beg+ floor( (end-beg) /2 ) )
        else:
            return FindRow(code, i+1, beg+round ( (end-beg) /2), end)
    else:
        if code[i]=='F':
            return min(beg,end)
        if code[i]=='B':
            return max(beg,end)
        

def FindCol(code,i,fcol,lcol):
    if i<2:
        if code[i]=='R':
            return FindCol( code,i+1, round( (lcol-fcol)/2) , lcol )  
        else:
            return FindCol(code, i+1, fcol, fcol+floor( (lcol-fcol)/2 ) )
    else:
        if code[i]=='R':
            return max(fcol,lcol)
        if code[i]=='L':
            return min(fcol,lcol)

def getIDs(beg,end):
    seatID=set()            
    for d in data:
        row=FindRow(d[0:7], 0, beg, end)
        col=FindCol(d[7:10], 0, 0, 7)
        seatID.add(row*8+col)
 #Calculo mal los ids no me salen los mismos que al pro
    return seatID

ids2=getIDs( 0, 127)
ids2.sort()
maxid=max(ids2) 

print(maxid)              
        
#PART 2
found=False
for id in ids2:
    if id+1 not in ids2 and id+2 in ids2:
        myid=id+1
        break
    
print(myid)
        
seatID=lambda s: int(s.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2)
ids=set(map(seatID,open('seats.txt').read().splitlines()))
print(max(ids), (set(range(min(ids),max(ids)))-ids).pop())
    
print(all(i in ids for i in ids2))





       
    
                
            
            
        