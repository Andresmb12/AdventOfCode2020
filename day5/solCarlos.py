# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:18:52 2020

@author: Andres
"""

def binstr2dec(string,zero):
    return int(''.join( map( str, (0 if c==zero else 1 for c in string)) ), 2)
#int('11',2) lo pasa a decimal
#join simplemente une cadenas
#map aplica la funcion de su primer argumento a cada uno
#de los elementos de el segundo
#lo que devuelve se puede pasar a list mismo

with open('seats.txt','r') as file:
    seats=file.read().splitlines() #remove \n

ids=[]
for s in seats:
    row=binstr2dec(s[:7], 'F')
    col=binstr2dec(s[7:], 'L')
    ids.append(row*8+col)
    
#Part one
print(max(ids))

#Part two

x= set( range( min(ids),max(ids)+1 ) )
y= set(ids)

print(x-y)
