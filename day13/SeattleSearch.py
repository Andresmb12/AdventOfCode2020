import math

with open('input.txt') as file:
    timestamp = int(file.readline())
    buses = [ int (b) for b in file.readline().split(',') if b != 'x' ]

bestbus=0
besttstamp=math.inf
for b in buses:
    dist = 0
    i=0
    while i*b < timestamp:
        i+=1
    if(i*b < besttstamp):
        besttstamp=i*b
        bestbus=b

print( (besttstamp-timestamp) * bestbus )
    
    
    