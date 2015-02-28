#
# zombie_reach.py
#
# This program takes in a floor plan, starting coordinates, and target coordinates then
# computes if the target is reachable from the start.

import sys
from math import *

# Constants to help with processing the floor plan
WALL='#'
OPEN='.'

def readMap(filename):
    """Returns a 2D list representing the floor plan in the file named filename"""
    map=list()
    mapfile=open(filename)
    for line in mapfile:
        line=line.strip()
        map.append(list(line))
    return map

def readLoc(map,x,y):
    """Returns the symbol to location x,y in the 2D list map"""

    # Since we shouldn't consider squares off of the map, treat them as walls
    if x<0 or x>len(map[0]):
        return WALL
    if y<0 or y>len(map):
        return WALL

    return map[y][x]

def setLoc(map,x,y,sym):
    """Sets the symbol at location x,y in the 2D list map to sym"""

    # Can't write to locations off of the map, don't write anything
    if x<0 or x>len(map[0]):
        return
    if y<0 or y>len(map):
        return

    map[y][x]=sym

def printMap(map):
    """Pretty prints a map to the console"""

    # print y grid at top
    print("   ",end="")
    for x in range(len(map[0])):
        if x >=10:
            print(floor(x/10),end="")
        else:
            print(' ',end="")
    print()
    print("   ",end="")
    for x in range(len(map[0])):
        print(x%10,sep="",end="");
    print()
    print("   ",end="")
    for x in range(len(map[0])):
        print('-',end="")
    print()

    # print x grid and map symbols
    for y in range(len(map)):
        print(format(y,"2d"),'|',sep="",end="")
        for x in range(len(map[0])):
            print(readLoc(map,x,y),end='')
        print('')

def zombieSearch(map,zombie_x,zombie_y,target_x,target_y):
    """Recursive function to search from zombie_x,zombie_y to target_x,target_y in map

       Returns True if the zombie can reach the target, false otherwise
    """
    if target_x == zombie_x and target_y == zombie_y:
        return True
    if readLoc(map,zombie_x,zombie_y) == WALL:
        return False
    if readLoc(map,zombie_x,zombie_y) == 'Z':
        return False

    setLoc(map,zombie_x,zombie_y,'Z')
    
    if zombieSearch(map,zombie_x,zombie_y+1,target_x,target_y):
        return True
    if zombieSearch(map,zombie_x,zombie_y-1,target_x,target_y):
        return True
    if zombieSearch(map,zombie_x+1,zombie_y,target_x,target_y):
        return True
    if zombieSearch(map,zombie_x-1,zombie_y,target_x,target_y):
        return True
    return False

def main():
    """Reads a map file and prints a message when there is a way to get from the start
       coordinates to the target coordinates.

       You don't need to make any changes to the main function this week."""

    #check the args, abort if their aren't enough
    if len(sys.argv) != 6:
        print("Usage: python3 "+sys.argv[0]+" <filename.map> <zombie x> <zombie y> <target x> <target y>")
        exit(1)

    # covert from sys.argv list to easier names
    mapfile=sys.argv[1]
    zombiex=int(sys.argv[2])
    zombiey=int(sys.argv[3])
    targetx=int(sys.argv[4])
    targety=int(sys.argv[5])

    # Read the map file
    map=readMap(mapfile)

   # Validate that coordinates are within the map and not located in a wall
    validated = True
    if readLoc(map,zombiex,zombiey) != OPEN:
        print("Invalid zombie coordinates!")
        validated = False 
    if readLoc(map,targetx,targety) != OPEN:
        print("Invalid target coordinates!")
        validated = False

    # Set initial locations and print map
    setLoc(map,zombiex,zombiey,'S')
    setLoc(map,targetx,targety,'T')
    printMap(map)

    if not validated:
        sys.exit()

    # Use the recursive function to complete the search
    canReach=zombieSearch(map,zombiex,zombiey,targetx,targety)

    # print final map
    print()
    printMap(map)

    # Print the correct message to the user based on the search results
    if canReach:
        print("**************************************************")
        print("* !!! DANGER - Zombie risk detected - DANGER !!! *")
        print("**************************************************")
    else:
        print("Floor plan appears safe.")

if __name__=="__main__":
    main()
