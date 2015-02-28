"""
game_dict: Game dictionary.

Authors: Mark Holmgren


Differs from a spelling dictionary in that looking up a string
has three possible outcomes:  The string matches a word exactly,
or it does not match exactly but is a prefix of a word, or there is
no word starting with that string.

Note: This has nothing to do with the Python data structure called a 'dict'
or 'dictionary'; we are using 'dictionary' in the common English meaning 
as a reference in which one searches for words. 
"""

words = [ ]  

# Codes for result of search
WORD = 1
PREFIX = 2
NO_MATCH = 0


def read(file, min_length=3):
    """Read the dictionary from a sorted list of words.
    Args:
        file: dictionary file (list of words, in alphabetical order), 
            already open 
        min_length: integer, minimum length of words to
            include in dictionary. Useful for games in
            which short words don't count.  For example,
            in Boggle the limit is usually 3, but in
            some variations of Boggle only words of 4 or
            more letters count.
    Returns:  nothing
    """  
    global words
    words = [ ]
    with file as dict_file:
        for line in dict_file:
            line = line.strip() # strip line from whitespace
            if len(line) < min_length:
                pass
            else:
                words.append(line)
    words.sort()
    return

def search( prefix ):
    """Search for a prefix string in the dictionary.
    Args:
        str:  A string to look for in the dictionary
    Returns:
        code WORD if str exactly matches a word in the dictionary,
            PREFIX if str does not match a word exactly but is a prefix
                of a word in the dictionary, or
        NO_MATCH if str is not a prefix of any word in the dictionary
    """
    
    '''
    ### LINEAR SEARCH ###
    if prefix in words:
        return WORD

    for word in words:
        if prefix == word[:len(prefix)]:
            return PREFIX

    return NO_MATCH

    ### LINEAR SEARCH END ###
    

    ### BINARY SEARCH ###

    '''
    low = 0
    high = len(words) -1

    while high >= low:
        mid = (low+high) // 2
        
        if prefix == words[mid]:
            return WORD

        if prefix < words[mid]:
            high = mid - 1

        #if prefix > words[mid]:
        else:
            low = mid + 1

    if prefix == words[mid][:len(prefix)]:
        return PREFIX

    low = 0
    high = len(words) -1

    while high >= low:
        mid = (low+high) // 2
        
        if prefix == words[mid][:len(prefix)]:
            return PREFIX

        if prefix < words[mid]:
            high = mid - 1

        #if prefix > words[mid]:
        else:
            low = mid + 1
    

    return NO_MATCH
    
    ### BINARY SEARCH END ###

    
    
    
######################################################
#  Test driver
#    for testing game_dict.py by itself,
#    separate from boggler.py
#   Note we will need shortdict.txt and dict.txt for
#    testing.  Using the module does not require those files,
#    but this suite of test cases requires exactly those files
#    with exactly those names. 
#   
#
#   To test your game_dict module, invoke it on the
#   command line:
#      python3  game_dict.py    (in MacOS), or
#      python  game_dict.py     (in Windows)
#
#######################################################


if __name__ == "__main__":
    # This code executes only if we execute game_dict.py by itself,
    # not if we import it into boggler.py
    from test_harness import testEQ
    read(open("shortdict.txt"),3)
    # shortdict contains "alpha", "beta","delta", "gamma", "omega"
    testEQ("First word in dictionary (alpha)", search("alpha"), WORD)
    testEQ("Last word in dictionary (omega)", search("omega"), WORD)
    testEQ("Within dictionary (beta)", search("beta"), WORD)
    testEQ("Within dictionary (delta)", search("delta"), WORD)
    testEQ("Within dictionary (gamma)", search("gamma"), WORD)
    testEQ("Prefix of first word (al)", search("al"), PREFIX)
    testEQ("Prefix of last word (om)", search("om"), PREFIX)
    testEQ("Prefix of interior word (bet)", search("bet"),PREFIX)
    testEQ("Prefix of interior word (gam)", search("gam"),PREFIX)
    testEQ("Prefix of interior word (del)", search("del"),PREFIX)
    testEQ("Before any word (aardvark)", search("aardvark"), NO_MATCH)
    testEQ("After all words (zephyr)", search("zephyr"), NO_MATCH)
    testEQ("Interior non-word (axe)", search("axe"), NO_MATCH)
    testEQ("Interior non-word (carrot)", search("carrot"), NO_MATCH)
    testEQ("Interior non-word (hagiography)",
        search("hagiography"), NO_MATCH)
    # Try again with only words of length at least 5
    # Now beta should be absent
    read(open("shortdict.txt"), 5)
    print("New dictionary: ", dict)
    testEQ("First word in dictionary (alpha)", search("alpha"), WORD)
    testEQ("Last word in dictionary (omega)", search("omega"), WORD)
    testEQ("Short word omitted (beta)", search("beta"), NO_MATCH)
    read(open("dict.txt"), 3)  # Long dictioanry
    testEQ("Can I find farm in long dictonary?", search("farm"), WORD)
    testEQ("Can I find bead in long dictionary?", search("bead"), WORD)

    
