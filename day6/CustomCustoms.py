with open('plane.txt','r') as file:
    plane=file.read().split("\n\n")
#PART 1
groups=[p.replace('\n','') for p in plane]
print ( sum( [ len( set(g) ) for g in groups] ) )
#PART 2 
groups=[p.split('\n') for p in plane]
print ( sum( [ len(set.intersection(* [set(p) for p in g] ) ) for g in groups ] ) )

"""Cojo cada grupo y hago que cada persona sea un conjunto
convierto cada grupo en una lista de conjuntos, luego calculo las intersecciones de cada 
grupo y su longitud"""


"""Sol Carlos:
            
with open('plane.txt','r') as file:
    groups=file.read().split("\n\n")

def count(set_op):
    return sum( len ( set_op( *[set(person) for person in plane.splitlines() ] ) ) for group in groups )

print( count(set.union) )

print( count(set.intersection) )

"""