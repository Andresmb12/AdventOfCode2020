# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:00:52 2020

@author: Andres
"""
import re
import numpy as np

def op(a,b,c):
        return int ( (a==c and b!=c) or (a!=c and b==c) )

class Line:
    
    def __init__(self,string):
        temp1=string.split(sep=' ')
        noccs=temp1[0].split(sep='-')
        self.min=int(noccs[0])
        self.max=int(noccs[1])
        self.letter=temp1[1].replace(":","")
        self.pw=temp1[2]
        
    
    def checkLine1(self):
        policy=re.compile( r'%s' % self.letter)
        check = len(policy.findall(self.pw))
        return int(check <= self.max and check >= self.min)
    

    def checkLine2(self):
        a=self.pw[self.max-1]
        b=self.pw[self.min-1]
        c=self.letter
        return op(a,b,c)
        
        
                
with open('passwords.txt','r') as file:
    predata=file.readlines()

valid_pw1=0
valid_pw2=0

valid_pw1=np.sum( [ Line(l).checkLine1() for l in predata] )
valid_pw2=np.sum( [ Line(l).checkLine2() for l in predata] )


    
print("Part 1, there are %i valid passwords" % valid_pw1 )
print("Part 2, there are %i valid passwords" % valid_pw2 )   

        
        

