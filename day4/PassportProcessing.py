#part 1

fields=['byr','iyr','eyr','hgt','hcl','ecl','pid']

with open('passports.txt','r') as file:
    data=file.read().split("\n\n")
    
def ArePresent(p):
    return ( all(f in p for f in fields) )

import numpy as np
valids=np.sum( [ int(ArePresent(p)) for p in data ] )

print(valids)

#part 2

def checkYear(y,limi,lims):
    return y.isdigit() and len(y)==4 and limi <= int(y) <= lims

def hgt(h):
    return ('cm' in h and len(h) == 5 and 150 <= int(h[0:3]) <=193) or ('in' in h and 59 <= int(h[0:2]) <= 76 )

import re
def hcl(h):
    pat=r'#[0-9a-f]{6}'
    return bool( re.match(pat, h) )

def ecl(e):
    colors=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return e in colors

def pid(p):
    return len(p)==9 and p.isdigit()

def AreValid(pd):
    temp1= checkYear(pd['byr'], 1920, 2002) and checkYear(pd['iyr'], 2010,2020 ) and checkYear(pd['eyr'], 2020, 2030)
    temp2=hcl(pd['hcl'] ) and hgt(pd['hgt']) and ecl(pd['ecl']) and pid(pd['pid'])
    return temp1 and temp2

def psp_to_dict(p):
    return { f.split(':')[0] : f.split(':')[1] for f in re.split('\n| ',p) }
    """
    psp=re.split('\n| ',p)
    a={}
    for f in psp:
        temp=f.split(':')
        a[temp[0]]=temp[1]
        #a[f.split(':')[0] = a[f.split(':')[1]]
        return a"""
     
nvalids=0
for d in data:
    pd=psp_to_dict(d)
    nvalids += int( ArePresent(d) and AreValid(pd) )
        
print(nvalids)
            
            
            
            
            
            

    

    
    
    

