# PART 1
import numpy as np
with open('input.txt','r') as file:
    data = np.array([ int(d) for d in file])
    
nadapters = len(data)
difs=[]
def mindiff(n):
    m = np.argmin( abs(data-n) )
    difs.append( abs( data [m] - n) )
    temp=data[m]
    data[m]=10000 #I mark it so it won't be chosen again
    return temp
i=0
n=0
while i < nadapters:
    n = mindiff(n)
    i+=1
difs.append(3) #my device's built-in adapter is always 3 higher than the highest adapter
   
print( difs.count(1) * difs.count(3) )

print(difs)

#PART 2
#ver best solution

