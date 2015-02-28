"""
Assignment 2, counts.py, CIS 210
Authors: Mark Holmgren
Credits: None

Count the number of occurrences of each major code in a file.

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    The function strips, sorts and counts replicas in any txt file, and prints the
    number of replicas for each diffetent string.  
    """
    majors = [ ]

    for line in majors_file:
        majors.append(line.strip())
    
    majors = sorted(majors)

    majors.append('Running counts.py') 
    prior = majors[len(majors) - 1]
    count = 0
    for major in majors:     
        if major != prior:

            if count == 0:  # The count will be 0 once and then prints the last string in the list.
                print(prior)

            else:
                print(prior, count)
                count = 0

        count += 1
        prior = major

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
