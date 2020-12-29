#PART 2
with open('test3.txt') as file:
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
mybag="shiny gold"
for d in data:
    rules.update( ruletodict(d,2) )

b=mybag

def getcols(b):
    if b not in rules.keys():
        return []
    if rules[b]==['no other']:
        return []
    else:
        return rules[b]

def reccols(mybag,tot,n):
    itscolors=getcols(mybag)
    for c in itscolors:
        nb=int( str( [i for i in c[0] if i.isdigit()][0] ) )
        col=''.join( filter(lambda x: not x.isdigit(), c) )
        col=col.strip()
        nbags_from_this_color=nb*n
        tot+=nbags_from_this_color
        tot=reccols(col,tot,nbags_from_this_color)  
    return tot

print ( reccols(b,0,1) )
