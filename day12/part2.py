from recordclass import recordclass
 
coordinate=recordclass('coordinate','x y')
with open('input.txt') as file:
    data = file.read().split()
 
facing = 90
points = {'0':'N','90':'E','180':'S','270':'W'}
waypoint=coordinate(10,-1) #initial position relative the ship
ship=coordinate(0,0)

for d in data:
    action,value=d[0],int(d[1:])
    if action == 'N':
        waypoint.y-=value
    elif action == 'S':
        waypoint.y+=value
    elif action =='E':
        waypoint.x+=value
    elif action == 'W':
        waypoint.x-=value
    elif action == 'L':
        for i in range(0, int(value/90) ):
            waypoint.x,waypoint.y= waypoint.y,-waypoint.x
    elif action == 'R':
        for i in range(0, int(value/90) ):
            waypoint.x,waypoint.y= -waypoint.y,waypoint.x
    elif action == 'F':
        ship.x+=(waypoint.x * value)
        ship.y+=(waypoint.y * value)

print(abs(ship.x)+abs(ship.y))
            
