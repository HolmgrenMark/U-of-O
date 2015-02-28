"""
Tactics and checks for Sudoku.

Authors: Mark Holmgren

A tactic is a rule that can be used to determine and/or constrain the
possible choices for a Sudoku tile.

A check determines whether a given Sudoku board
(whether complete or incomplete) is legal.  A board is
legal if it contains only digits and open spaces, and
if all of the digits are unique in each row, column,
and 3x3 block.
"""
import sdkboard

# The following variables are private but global to the module
global groups
global progress

def prepare(board):
    """ 
    Prepare for checking and solving a sudoku board.
    Args:
       board:  An sdkboard.Board object
    Returns:
       nothing
    Effects:
       prepared for check(board) and solve(board)
    """
    global groups  # rows, columns, and blocks
    groups = [ ]
    
    # Rows  (we can reuse them from the board)    
    for row in range(9):
        groups.append(board.tiles[row])
        cols = [ ]
        for col in range(9):
            ch = board.tiles[col][row] 
            cols.append(ch)
        groups.append(cols)

    # Blocks  (we need new lists for these, too)
    for start_row in [0, 3, 6]:
        for start_col in [0, 3, 6]:
            sq_tiles = [ ] 
            for row in range(3):
                for col in range(3): 
                    t = board.tiles[start_row + row][start_col+col]
                    sq_tiles.append(t)
            groups.append(sq_tiles)

    # We need to know when we are making progress 
    for row in board.tiles:
        for tile in row:
            tile.register(progress_listener)


def progress_listener(tile, event):
    """
    An event listener, used to determine whether we have made
    some progress in solving a Sudoku puzzle.  This listener
    will be attached to Sudoku Tile objects, and informed when
    "determined" and "constrained" events occur.
    Args:
       tile:  The tile on which an event occurred
       event: What happened.  The events we listen for are "determined"
         and "constrained"
    Returns:  nothing
    Effects: module-global variable progress may be set to True
    """
    global progress 
    if event == "determined" or event == "constrained":
       progress = True
       # print("Notified of progress!")

def good_board(): 
        """Check that every group (row, column, and block)
        contains unique elements (no duplicate digits).
        Args:
           none  (implicit through prepare_board)
        Returns:
           Boolean True iff all groups contain unique elements
        Effects:
           Will announce "duplicate" event on tiles that are
           not unique in a group.
        Requires:
           prepare(board) must be called before good_board

        """
        symbols = ['1','2','3','4','5','6','7','8','9']
        duplicates = set()
        for obj in groups:
            avaliable = set(symbols)
            for item in obj:
                if item.symbol == '.':
                    pass
                elif item.symbol in avaliable:
                    avaliable.remove(item.symbol)     
                else:
                    for duplicate in obj:
                        if duplicate.symbol == item.symbol and duplicate not in duplicates:                            
                            duplicates.add(duplicate)
                            print('*** Tile at ', duplicate.row, duplicate.col,'is a duplicate of ', duplicate.symbol)
                            duplicate.announce('duplicate')     
        return True

def solve():
    """
    Keep applying naked_single and hidden_single tactics to every
    group (row, column, and block) as long as there is progress.
    Args: 
        none
    Requires:
        prepare(board) must be called once before solve()
        use only if good_board() returns True
    Effects: 
        May modify tiles in the board passed to prepare(board), 
        setting symbols in open tiles, and reducing the possible
        sets in some tiles. 
    """
    global progress
    progress = True
    while(progress):
        # print("***Starting solution round***")
        progress = False
        # Note that naked_single and hidden_single may indirectly
        # set the progress flag by causing the progress listener to be
        # triggered.  
        for group in groups:
            naked_single(group)
            hidden_single(group)

def naked_single(group):
        """Constrain each tile to not contain any of the digits 
        that have already been used in the group.
        Args: 
            group: a list of 9 tiles in a row, column, or block
        Returns:
            nothing
        Effects:
            For each tile in the group, eliminates "possible" elements
            that match a digit used by another tile in the group.  If 
            this reduces it to one possibility, the selection will be 
            made (Tile.remove_choices does this), and progress may be 
            signaled.
        """
    
        
        taken = set()
        for tile in group:
            if tile.symbol == '.':
                pass
            elif tile.symbol not in taken:
                taken.add(tile.symbol)
            for tile in group:
                if tile.symbol == '.':
                    tile.remove_choices(taken)

        return
        
        
def hidden_single(group):
        """Each digit has to go somewhere.  For each digit, 
        see if there is only one place that digit should 
        go.  If there is, put it there. 
        Args: 
           group:  a list of 9 tiles in a row, column, or block
        Returns: 
           nothing
        Effects: 
           For each tile, if it is the only tile that can accept a 
           particular digit (according to its "possible" set), 
           
        """
        # print("Trying hidden single (required element) tactic")
        # FIXME - this tactic needs to be written
        # Hints: 
        # First, determine which digits still need to be placed 
        # somewhere.  Start with a set of all the digits, and 
        # remove those that are already placed in the group. 
        # Then, for each digit that needs a place, count how 
        # many tiles can take it, while also remembering the last
        # tile that can take it.  If there is only one, use the 
        # "determine" method of a tile to set it. 
        

        '''

        
        not_used = set(['1','2','3','4','5','6','7','8','9'])
        
        for tile in group:

            if tile.symbol != '.' and tile.symbol in not_used:
                not_used.remove(tile.symbol)
            
        for tile in group:
            full_set = set(['1','2','3','4','5','6','7','8','9'])
            for not_used_symbol in not_used:

                if tile.symbol == '.':
                    


                    if not_used_symbol in tile.possible:
                                count += 1
                                one_poss_symbol = not_used_symbol
                                one_poss = tile
                if count == 1:
                    full_set.remove(one_poss_symbol)
                    one_poss.remove_choices(full_set)

                    count = 0
                else: 
                    count = 0
            
                    

        '''
        count = 0
        not_used = set(['1','2','3','4','5','6','7','8','9'])
        full_set = set(['1','2','3','4','5','6','7','8','9'])
        for tile in group:

            if tile.symbol in not_used:
                   not_used.remove(tile.symbol)
                        
        for not_used_symbol in not_used:
            for tile in group:

                if tile.symbol == '.':
                    if not_used_symbol in tile.possible:
                        count += 1
                        one_poss_symbol = not_used_symbol
                        one_poss = tile
            
            if count == 1:
                full_set.remove(one_poss_symbol)
                one_poss.remove_choices(full_set)
                count = 0
            else:
                count = 0


      












        return


        