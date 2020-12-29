"""If a seat is empty (L) and there are no occupied seats adjacent to it, the seat 
becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
                       the seat becomes empty.
Otherwise, the seat's state does not change.

"""
import numpy as np

with open('test1.txt') as file:
    data = file.read().splitlines()

def eval_seat(row,col): #return number of occuped adjacent seats
    adjacents=[]
    topleft=data[row-1][col-1]
    topcenter=data[row-1][col]
    topright=data[row-1][col+1]
    right=data[row][col+1]
    left=data[row][col-1]
    downleft=data[row+1][col-1]
    downcenter=data[row+1][col]
    downright=data[row+1][col+1]
    adjacents.append(topleft)
    adjacents.append(topcenter)
    adjacents.append(topright)
    adjacents.append(left)
    adjacents.append(right)
    adjacents.append(downleft)
    adjacents.append(downcenter)
    adjacents.append(downright)
    temp=np.array(adjacents)
    temp2=temp=='#'
    return np.count_nonzero(temp2)

print( eval_seat(0, 0) )
    
     
    
    
