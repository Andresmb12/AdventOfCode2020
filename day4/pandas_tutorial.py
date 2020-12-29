# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 01:15:35 2020

@author: Andres
"""

import pandas as pd

def per_section(it, is_delimiter=lambda x: x.isspace()):
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ''.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())
    if ret:
        yield ''.join(ret)
        

        
with open("testbl.txt") as f:
    s = list(per_section(f))
    df = pd.DataFrame({'data':s})
    print (df)

#bl='\n\s*\n'
#a=pd.read_csv('testbl.txt',sep=bl,engine='python')