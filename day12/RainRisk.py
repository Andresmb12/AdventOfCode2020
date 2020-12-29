
from recordclass import recordclass

import re
temp = re.compile("([a-zA-Z]+)([0-9]+)") 
 
action=recordclass('action', 'direction, value')
with open('input.txt') as file:
    data = [ action (*list(temp.match(line).groups() ) ) for line in file.read().splitlines() ]

EWposition = 0
NSposition = 0 
facing = 90
points = {'0':'N','90':'E','180':'S','270':'W'}

for d in data:
    if d.direction == 'F':
        d.direction = points[str(facing)]
    if d.direction == 'W':
        EWposition -= int(d.value)
    elif d.direction == 'E':
        EWposition += int(d.value)
    if d.direction == 'N':
        NSposition += int(d.value)
    elif d.direction == 'S':
        NSposition -= int(d.value)
    if d.direction == 'R':
        facing = ( facing + int(d.value) ) % 360
    elif d.direction == 'L':
        facing = ( facing - int(d.value) ) % 360

print(abs(EWposition) + abs(NSposition))

#PART 2
    
        