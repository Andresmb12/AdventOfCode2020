with open('input.txt','r') as file:
    data = [ int(number) for number in file ]
    
def findpair(data,n):
    found=False
    for d in data:
        if found:
            break
        if n-d in data:
            found = True
    return found

nnumbers = len(data)
i = 25
invalid_number=0
# PART 1
while i<nnumbers:
    if not findpair( data[i-25:i], data[i] ):
        invalid_number = (data[i])
    i += 1
print(invalid_number)
   
# PART 2
def findset2(n , p1, p2):
    p1=0
    p2=2
    s=data[p1:p2]
    while s != n and p1!=nnumbers-1:
        s = sum( data[p1:p2] )
        if p2==nnumbers or s > n:
            p2=p1+2
            p1+=1   
        elif s < n:
            p2+=1
    
    return data[p1:p2]
            
sol_range=findset2(invalid_number, 0, 2)
print( min(sol_range) + max(sol_range) )