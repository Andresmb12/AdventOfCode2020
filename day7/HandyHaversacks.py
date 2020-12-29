with open('input.txt') as file:
    data=file.read().splitlines()
    
def ruletodict(r,part):
    head=r.split('bags')[0].strip()
    body=''.join( [ i for i in ( r.split('contain')[1].split(',') ) ] )
    if part==1:
        body=''.join( filter(lambda x: not x.isdigit(), body) )
    body.strip()
    body=body.split('  ')
    body=[b.replace('bags','').replace('bag','').replace('.','').strip() for b in body]
    if part==2:
        body=body[0].split('  ')
    return {head:body}

rules=dict()

for d in data:
    rules.update( ruletodict(d,1) )
    
#PART 1            
mybag="shiny gold"
cols=[]
cols+=[r for r in rules.keys() if mybag in rules[r] ]

for c in cols:
    cols+=[r for r in rules.keys() if c in rules[r] and r not in cols]
    
print(len(cols))

#PART 2
rules=dict()
for d in data:
    rules.update( ruletodict(d,2) ) 
    
def getcols(b):
    if b not in rules.keys() or rules[b]==['no other']:
        return []
    else:
        return rules[b]
    
def reccols(mybag,tot,n):
    itscolours=getcols(mybag)
    for c in itscolours:
        nb=int( str( [i for i in c[0] if i.isdigit()][0] ) ) #gets the number
        col=''.join( filter(lambda x: not x.isdigit(), c) ) #gets the colour
        col=col.strip()
        nbags_from_this_colour=nb*n
        tot+=nbags_from_this_colour
        tot=reccols(col,tot,nbags_from_this_colour)  
    return tot

print ( reccols(mybag,0,1) )


