import numpy as np
with open('input.txt') as file:
    buses = [ b for b in file.read().split(',')  ]
    
offsets=np.array([i for i,x in enumerate( [ b.isdigit() for b in buses] ) if x])

b=np.array([int(i) for i in buses if i.isdigit()])

l=len(b)

s=max(b)
i=np.ones(l)*s + offsets

com= i % b

while any(com!=0):
    i=np.ones(l)*s + offsets
    com= i % b
    s*=


print(i)
print(i[0])
    
def mcm(n):
    aux = np.array(n)
    return min([e for e in range( np.max(aux), np.prod(aux)+1 ) if all(e%aux == 0)])
    
    
    




    