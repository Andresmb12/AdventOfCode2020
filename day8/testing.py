# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 02:11:50 2020

@author: Andres
"""

from collections import namedtuple
with open('test1.txt','r') as file:
    data=file.read().splitlines()

instruction=namedtuple('instruction','op , n')
code = [ instruction(*d.split(' ')) for d in data]

nlines = len(code)

accumulator=0
def nop(n):
    return 1
def acc(n):
    global accumulator
    accumulator+=int(n)
    return 1
def jmp(n):
    return int(n)
    
    
operations = locals() #it contains the 3 operations above
executed=set()   
lastinstruction=code[-1]

def exec_code(c_to_modify,part):
    line=0
    while line < nlines and line not in executed:
        numarg = code[line].n
        nextop = code[line].op
        if part==2 and c_to_modify==code[line] and nextop in ['jmp','nop']:
            nextop='jmp' if nextop=='nop' else 'nop'
        executed.add(line)
        
        line += operations[ nextop ](numarg)
    return not( line in executed )

exec_code([],1)
print ( accumulator ) 

#Part 2


for c in code:
    executed.clear()
    accumulator = 0
    if exec_code(c, 2): #it finishes normally
        print(accumulator)
    