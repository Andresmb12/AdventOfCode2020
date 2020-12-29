# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:57:32 2020

@author: Andres
"""

with open('expense_report.txt','r') as file:
    expenses={int(number) for number in file}


# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
expenses=list(expenses)
ndata=len(expenses)
def findPair(exp, ndata, target):
    s=set()
    i=0
    Found=False
    while i < ndata and  not Found:
        temp=target-exp[i]
        if temp in s:
            Found=True
            solution=[exp[i],temp]
        s.add(exp[i])
        i+=1
    
    return solution

""" Complexity time O(n)"""

def findTriplet(exp, ndata, target):
    exp.sort()
    for i in range(0,ndata-2):
        #I use two pointers left and right
        l = i + 1 
          
        # index of the last element 
        r = ndata-1
        
        if( exp[i] + exp[l] + exp[r] == target): 
                print("Triplet is", exp[i],  
                     ', ', exp[l], ', ', exp[r]); 
                return True
              
        elif (exp[i] + exp[l] + exp[r] < target): 
                l += 1
        else: # exp[i] + exp[l] + exp[r] > target 
                r -= 1
  
    # If we reach here, then 
    # no triplet was found 
    return False
  
    
solution=findPair(expenses, ndata, 2020)
print("Pair that sum 2020: "+str(solution[0])+" , "+str(solution[1]) ) 
print(solution[0]*solution[1])    
def find3Numbers(A, arr_size, sum): 
    for i in range(0, arr_size-1): 
        # Find pair in subarray A[i + 1..n-1]  
        # with sum equal to sum - A[i] 
        s = set() 
        curr_sum = sum - A[i] 
        for j in range(i + 1, arr_size): 
            if (curr_sum - A[j]) in s: 
                
                print("Triplet is", A[i],  
                        ", ", A[j], ", ", curr_sum-A[j]) 
                return [A[i],A[j],curr_sum-A[j]]
            s.add(A[j]) 
           
    
"""Complexity Analysis: 
Time complexity: O(N^2). 
There are only two nested loops traversing the array, so time complexity is O(n^2). Two pointers algorithm takes O(n) time and the first element can be fixed using another nested traversal.
Space Complexity: O(n). 
As no extra space is required. """     


#solution=findTriplet(expenses,ndata,2020) #no me ha funcionado
solution=find3Numbers(expenses, ndata, 2020)

sol=solution[0]*solution[1]*solution[2]
print(sol)




