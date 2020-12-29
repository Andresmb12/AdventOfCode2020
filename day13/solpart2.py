from math import ceil

with open('test.txt') as file:
    file.readline()
    buses_list=file.read().split(',')
    offsets={int(id): buses_list.index(id) for id in buses_list if id!='x'}

    
sorted_ids=sorted(offsets.keys())
lowest=sorted_ids[0]    

print(buses_list)
t = ceil( offsets[lowest] / lowest ) * lowest - offsets[lowest] 

inc=lowest

for i in range(1,len(sorted_ids)):
    id=sorted_ids[i]
    print("nuevo id: "+str(id))
    print("inc="+str(inc))
    while ((t + offsets[id]) % id != 0):
        print("t="+str(t))
        t+=inc
    print(t)
    inc*=id
    print("nuevo inc: "+str(inc))

print(t)



