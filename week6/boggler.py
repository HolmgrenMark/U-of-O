"""
Boggle solver finds words on a boggle board. 
Authors:  Mark Holmgren

Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical order
    
"""

from boggle_board import BoggleBoard   
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words

def main():
    """
    Main program: 
    Find all words of length 3 or greater on a boggle 
    board. 
    Args:
        none (but expect two arguments on command line)
    Returns: 
        Nothing (but prints found words in alphabetical
        order, without duplicates, one word per line)
    """


    dict_file, board_text = getargs()
    game_dict.read( dict_file )
    board = BoggleBoard(board_text)
    
    results = [ ] 
    row = 0
    col = 0 
    prefix = ''
    total = 0
    prev = ''

    for letter in board_text:
        if col > 3:
            row += 1
            col = 0
        find_words(board, row, col, prefix, results)
        col +=1

    results.sort()   
    for word in results:
        if prev == word:
            pass
        else:
            points = score(word)
            total += points
            print(word, points)
        prev = word
    print('Total score: ', total)


def getargs():
    """
    Get command line arguments.
    Args:
       none (but expects two arguments on program command line)
    Returns:
       pair (dictfile, text)
         where dictfile is a file containing dictionary words (the words boggler will look for)
         and   text is 16 characters of text that form a board
    Effects:
       also prints meaningful error messages when the command line does not have the right arguments
   """
    parser = argparse.ArgumentParser(description="Find boggle words")
    parser.add_argument('board', type=str, help="A 16 character string to represent 4 rows of 4 letters. Q represents QU.")
    parser.add_argument('dict', type=argparse.FileType('r'),
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # will get arguments from command line and validate them
    text = args.board
    dictfile = args.dict
    if len(text) != 16 :
        print("Board text must be exactly 16 alphabetic characters")
        exit(1)
    return dictfile, text


        
def find_words(board, row, col, prefix, results):
    """Find all words starting with prefix that
    can be completed from row,col of board.
    Args:
        row:  row of position to continue from (need not be on board)
        col:  col of position to continue from (need not be on board)
        prefix: looking for words that start with this prefix
        results: list of words found so far
    Returns: nothing
        (side effect is filling results list)
    Effects:
        inserts found words (not necessarily unique) into results
    """

    if BoggleBoard.available(board, row, col):
        position = BoggleBoard.get_char(board, row, col)
        BoggleBoard.mark_taken(board, row, col)
        prefix += position
        res = game_dict.search(prefix)   

        if res == game_dict.WORD:
            results.append(prefix)
            pass

        if res == game_dict.PREFIX or res == game_dict.WORD:
            if find_words(board, row, col+1, prefix, results):
                return 
            elif find_words(board, row+1, col, prefix, results):
                return 
            elif find_words(board, row-1, col, prefix, results):
                return 
            elif find_words(board, row, col-1, prefix, results):
                return         
            elif find_words(board, row+1, col+1, prefix, results):
                return 
            elif find_words(board, row+1, col-1, prefix, results):
                return 
            elif find_words(board, row-1, col+1, prefix, results):
                return         
            elif find_words(board, row-1, col-1, prefix, results):
                return
            else:
                BoggleBoard.unmark_taken(board, row, col)

        if res == game_dict.NO_MATCH:
            BoggleBoard.unmark_taken(board, row, col)
            return 
    return
    
    
    
def score(word):
    """
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle. 

    Args:
        a string
    Returns:
        The number of points that wordlength represents

          ||  Word length ||  Points ||
          ||  3, 4        ||   1     ||
          ||  5           ||   2     ||
          ||  6           ||   3     ||
          ||  7           ||   5     ||
          ||  8+          ||   11    ||

     """

    if len(word)<=4:
        return 1
    if len(word)==5:
        return 2
    if len(word)==6:
        return 3
    if len(word)==7:
        return 5
    if len(word)>8:
        return 11




####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")

