
"""start by counting all the trees you would encounter for the slope 
right 3, down 1:
From your starting position at the top-left, 
check the position that is right 3 and down 1. 
Then, check the position that is right 3 and down 1 from there, 
and so on until you go past the bottom of the map. """


with open('input.txt','r') as file:
    data=[line.strip() for line in file]

lastline=len(data) 

width=len(data[0]) #width of the forest

def isATree(c):
    return int(c=='#')

def TreesCounter(rightsteps,downsteps):
    ntrees=0
    row=col=0
    while row < lastline:
        
        location=data[row][col]
        ntrees += isATree(location)
        row+=downsteps
        col=(col+rightsteps)%width
    return ntrees

#Part 1:
n=TreesCounter(3, 1)

print("%i trees encountered" % n)

#Part 2:

slopes=[ [1,1],[3,1],[5,1],[7,1],[1,2] ]

"""The star(*) operator unpacks the sequence/collection into positional arguments. 
So if you have a list and want to pass the items of that list as arguments for each 
position as they are there in the list, instead of indexing each element individually, 
you could just use the * operator"""

results = [ TreesCounter(*slope) for slope in slopes ] 

#I use this instead of np.prod because it overflows
from functools import reduce 
import operator
print("result="+ str(reduce(operator.mul, results, 1)))


        
        
        
        
    
    




