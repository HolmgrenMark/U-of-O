"""
How many distinct chambers in the cavern?

Authors: Mark Holmgren

CIS 210  Week 4 project
Determines the number of distinct chambers in a grid representation of 
a cavern by flood-filling each discovered air pocket. 

Usage:  python3 cavern.py cavedesc.txt

Requires grid.py, graphics.py  (for displaying cavern as grid of cells)
"""

import sys         # To increase default limit on frames for recursion
import argparse    # Command line argument parsing
import grid        # Instructor-provided module for drawing caves and other 2D grids 

sys.setrecursionlimit(10000) # Max cavern size 100 x 100 = 10,000 cells

# Symbols to represent what is in a particular cell of the cavern.
AIR = " "
STONE = "#"
WATER = "~"

def read_cave( cavern_file ):
    """Read a cave description from file at path.
    
    Args: 
        path:  file name path for cave description, e.g., 
               "/Users/bart/caves/cave1.txt" or "c:\caves\cave1.txt"
               or "cave1.txt" if the cave is in the current directory.
    Returns:  
        the cavern as a matrix (list of lists) of strings. 
    """
    cave_open = False
    for line in cavern_file:
        fields = line.split()
        command = fields[0]
        if command == "cave" :
            validate(len(fields) == 3, "Syntax 'cave rows cols'", line)
            nrows = int(fields[1])
            ncols = int(fields[2])
            validate(nrows > 0, "Rows should be a positive integer", line)
            validate(ncols > 0, "Columns should be a positive integer", line)
            cave = new_cave(nrows, ncols)
            cave_open = True
        elif command == "hwall" :
            validate(cave_open, "First line should be 'cave rows cols'", line)
            validate(len(fields) == 4, "Syntax 'hwall startrow startcol length'", line)
            validate(cave_open, "cave command must precede hwall command", line)
            start_row = int(fields[1])
            start_col = int(fields[2])
            length = int(fields[3])
            validate(start_row >= 0, "Start row must be integer, zero or greater", line)
            validate(start_col >= 0, "Start column must be integer, zero or greater", line)
            validate(length >= 1, "Length of wall must be integer, at least 1", line)
            validate(start_col + length <= ncols, "Wall cannot extend beyond right edge", line)
            hwall(cave, start_row, start_col, length)
        elif command == "vwall" :
            validate(cave_open, "First line should be 'cave rows cols'", line)
            validate(len(fields) == 4, "Syntax 'vwall startrow startcol length'", line)
            validate(cave_open, "cave command must precede vwall command", line)
            start_row = int(fields[1])
            start_col = int(fields[2])
            length = int(fields[3])
            validate(start_row >= 0, "Start row must be integer, zero or greater", line)
            validate(start_col >= 0, "Start column must be integer, zero or greater", line)
            validate(length >= 1, "Length of wall must be integer, at least 1", line)
            validate(start_row + length <= nrows, "Wall cannot extend through floor", line)
            vwall(cave, start_row, start_col, length)
        else:
            print("**Command not understood: ", line)
    return cave


def validate(condition, msg, line):
    """If condition (boolean value) is not true, give the error message and the
    line that violates the condition, and exit the program.
    (Otherwise no effect)
    
    Args: 
        condition:  A boolean value (typically written as an expression, e.g., "x > 12")
        msg:  Message to user if the condition is not true
        line:  An input line to display to the user to show where the error occurred
    Returns:
        Nothing if the condition is true.  If the condition is false, this 
        function also doesn't return because it stops the program. 
    """
    if condition:
        return
    print("*** Invalid command line:", msg)
    print("*** in line: ", line)
    exit(1)


def new_cave(nrows, ncols):
    """Create and return a new cave with
    nrows rows and ncols columns, initially filled
    entirely with air.
    
    Args: 
        nrows:  How many rows of cells in this cavern?  
                At most 50 recommended for reasonable performance. 
        ncols:  How many columns of cells in this cavern? 
                At most 50 recommended for reasonable performance. 
                
    Returns:  A matrix of cells in the form of a list of 
        nrows lists of ncols cells.  Each cell is represented as a 
        one-character string. 
    """
    cave = [ ]
    for row in range(nrows):
        newRow = [ ]
        cave.append(newRow)
        for col in range(ncols):
            newRow.append(AIR)
    return cave

def hwall(cave,row,col,length):
    """Build a horizontal wall of stone starting from (row,col) and
    extending length cells to the right.
    
    Example: hwall(cave,3,3,2) sets cells (3,3) and (3,4) of cave to STONE
    
    Args: 
        cave:  A matrix (list of lists) representing the cavern
        row:   Row in which the new wall will be built
        col:   Beginning column of the new wall
        length:   The new wall starts at (row, col) and extends length
               cells to (row, col + length - 1)
    """
    for i in range(length):
        cave[row][col+i] = STONE

def vwall(cave,row,col,length):
    """Build a vertical wall of stone starting from (row,col) and
    extending length cells down.
    
    Args: 
        cave:  A matrix (list of lists) representing the cavern
        row:   Beginning row of the new wall
        col:   Column in which the new wall will be built
        length:   The new wall starts at (row, col) and extends length
               cells to (row + length - 1, col)
    Returns: nothing
    """
    for i in range(length):
        cave[row +i][col] = STONE
    
        
def dump_cave(cave):
    """Print a simple textual representation of the cave, for debugging.

    Args: 
        cave:  A matrix (list of lists) representing the cavern
    Returns: 
        nothing, but prints a textual representation of the cavern
    """
    ### Not used in the final program, but potentially useful for debugging
    ### because it's faster than displaying the graphics, and less likely to 
    ### crash if there is a problem in the cavern contents
    for row in cave :
        print("|", end="")
        for col in row :
            print( col, end="")
        print("|")

def display(cave):
    """Create a graphical representation of cave using the grid.
    This graphical representation can be further manipulated
    (e.g., filling cave cells with water of various colors)
    using the fill_cell method of module grid.
    
    Args: 
        cave: A matrix (list of lists) representing the cavern
    Returns: 
        Nothing, but has the side effect of creating a graphical 
        grid representation of the cavern in a 500x500 pixel window. 
    """
    nrows = len(cave)
    ncols = len(cave[0])
    grid.make(nrows, ncols, 500, 500)
    for row in range(nrows):
        for col in range(ncols):
            if cave[row][col] == STONE :
                grid.fill_cell(row, col, grid.black)

def fill(cave, row, col, color):
    """Fill a chamber of the cave with water, starting
    at row, col. Water can spread in all four cardinal
    directions, but cannot penetrate stone.  No effect
    if row or col are not inside the cave.
    
    Attempting to pour water where there is already WATER or STONE
    has no effect.  Attempting to pour water outside the cavern has
    no effect.  Attempting to pour water in a cell containing AIR 
    not only places colored water in that cell, but also spreads it
    in all directions by causing it to be poured in the cell to the 
    left and right and above and below. 
    
    Args: 
        cave: A matrix (list of lists) representing the cavern. Each 
            cell in the cave may hold AIR, STONE, or WATER.
        row: Starting row of the grid cell where we pour water
        col: Starting column of the grid cell where we pour water
        color: color of the water we try to pour in.
    """

    if row < 0: # Basecase! Cant fill outside the cave
    	return False
    if col < 0: # Basecase! Cant fill outside the cave
    	return False
    if row > len(cave)-1: # Basecase! Cant fill outside the the width of the cave
    	return False
    if col > len(cave[0])-1: # Basecase! Cant fill outside the height of the cave
    	return False
    if cave[row][col] == WATER: # Basecase! Cant fill space that has already been filled
    	return False
    if cave[row][col] == STONE: # Basecase! Cant fill stone
    	return False
    
    if cave[row][col] == AIR:  # Progress! If we hit air we fill till the cave is full
        cave[row][col] = WATER
        grid.fill_cell(row, col, color)
        
    if fill(cave,row,col+1,color): # we fill in one direction tills the functions returns falls bacause one of the basecases have been set off
    	return True
    if fill(cave,row+1,col,color): # then we go on to the next one, same process here
    	return True
    if fill(cave,row-1,col,color): # and here
    	return True
    if fill(cave,row,col-1,color): # and here
    	return True


   	
    '''
    if cave[row][col] == AIR : 
        cave[row][col] = WATER
        grid.fill_cell(row, col, color)
        if col > 0:
            fill(cave,row,col-1,color) # fills up
        if row < nrows-1: 
            fill(cave,row+1,col,color) # fills right
        if row > 0:
            fill(cave,row-1,col,color) # fills left
        if col < ncols-1:
            fill(cave,row,col+1,color) # fills down
    '''

def explore(cave):
    """
    Counts how many chambers the cavern has.
    When the function hits AIR its increments the count.
    Calls fill() to fill up the cave so it wont be counted again.

    """
    count = 0
    for row in range( len(cave)) :
        for col in range( len(cave[0])):
            if cave[row][col] == AIR: 
                count += 1
            color = grid.get_cur_color()
            fill(cave, row, col, color)
            grid.get_next_color()
    return count


def main():
    """Reads a cave from a specified configuration file, 
    displays it, and fills each chamber with a different color
    of water while counting chambers. 
    
    Args (from command line):
        Cave description file, example, "cave.txt"
        
    Usage: python3 cavern.py cave.txt
    """
    parser = argparse.ArgumentParser(description="How many chambers in the cavern?")
    parser.add_argument("cavern", type=argparse.FileType('r'), 
                        help="Cavern description file, e.g., cave.txt")
    args = parser.parse_args()  
    cave_desc = args.cavern

    cave =  read_cave(cave_desc)
    display(cave)
    count = explore(cave)
    #dump_cave(cave)  ## May be useful for debugging

    
    print("{} chambers in cavern".format(count))
    input("Press enter to close display")

if __name__ == "__main__":
    main()
