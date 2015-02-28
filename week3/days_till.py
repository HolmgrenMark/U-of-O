"""
How many days from yyyy mm dd until the next mm dd
Authors: Mark Holmgren

CIS 210 assignment 3, Winter 2014
Usage example: python days_till.py  2012 09 24 06 14
    (first day of fall classes until end of spring finals)

Checks for leap year in first date. Feb 29 can only be used is years as such.

"""

import sys  # For exit with a message
import argparse # Fancier command line parsing

MONTHLEN = [ 0, # No month zero
    31, # 1. January
    28, # 2. February (Depending on leap year this value will change)
    31, # 3. March
    30, # 4. April
    31, # 5. May
    30, # 6. June
    31, # 7. July
    31, # 8. August
    30, # 9. September
    31, #10. October
    30, #11. November
    31, #12. December
    ]

def leap_year(year):
    '''
    Checks if year is a leap year. If it is it returns True
    '''
    if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
        return True
    
def last_days_first_month(start_day, start_month, end_day, end_month,year):
    '''
    Checks if the dates are in the same month this year or with new year inbetween
    Returns the number of days in the first month. 
    '''
    if leap_year(year) == True: #changes FEB to leap year if year == leap year
        MONTHLEN[2]=29
    else:
        MONTHLEN[2]=28

    if start_month == end_month: 
        if start_day > end_day: # if start_day is a lager number then the second date is in the next year
            days_in_first_month = MONTHLEN[start_month] - start_day 
        else: # if start_day is a smaller number then the second date is in the same month the same year
            days_in_first_month = end_day - start_day 
    else:
        days_in_first_month = MONTHLEN[start_month] - start_day
    
    return days_in_first_month

def months(start_month, end_month):
    '''
    returns the number of months starting at value 0 

    To be clear 0 = one month
    '''
    if start_month > end_month:
        number_of_months = (12 - start_month) + end_month
    else:
        number_of_months = end_month - start_month
    return number_of_months

def counting_days(number_of_months,start_month, days_in_first_month, end_day, year):
    '''
    Adding function to calculate the sum of the days. 

    '''
    counter = days_in_first_month # first month value added to the counter
    start_month += 1
    
    for i in range(number_of_months): # if number_of_months = 0 (one month), it wont enter this loop  
        
        if i == (number_of_months -1): # if the function loops to the last month is adds the end day to the counter
            counter += end_day

        else:    
            counter += MONTHLEN[start_month] # if the loop is not in the last month it ads the lenth of the month to the counter
        
        start_month += 1 # incrementing the month as we go to keep track of the number of days
        
        if start_month == 13: # when we hit month 13 it turns to 1 och increments the year
            start_month = 1
            year += 1
            MONTHLEN[2]=28
    return counter

def is_valid(year, start_month, start_day, end_month, end_day):
    '''
    Checks for leap year in first date.
    Sets feb 29 in second date as march 1.

    '''

    if year < 1800 or year > 2500:
        sys.exit("Must start on a valid date between 1800 and 2500")

    if leap_year(year) == True:
        MONTHLEN[2]=29
    

    if start_month < 1 or start_month > 12 or start_day < 1 or start_day > MONTHLEN[start_month]:
        sys.exit("Starting month and day must be part of a valid date")

    MONTHLEN[2]=28 # reseting FEB 

    if end_month == 2 and end_day == 29: # change feb 29 as march 1 
         end_month = 3
         end_day = 1

    if end_month < 1 or end_month > 12 or end_day < 1 or end_day > MONTHLEN[end_month]:
        sys.exit("Ending month and day must be part of a valid date")     

def main():
    """
    Main program gets year number from command line, 
    invokes computation, reports result on output. 
    args: none (reads from command line)
    returns: none (write to standard output)
    effects: message or result printed on standard output
    """
    ## The standard way to get arguments from the command line, 
    ##    make sure they are the right type, and print help messages
    parser = argparse.ArgumentParser(description="Compute days from yyyy-mm-dd to next mm-dd.")
    parser.add_argument('year', type=int, help="Start year, between 1800 and 2500")
    parser.add_argument('start_month', type=int, help="Starting month, integer 1..12")
    parser.add_argument('start_day', type=int, help="Starting day, integer 1..31")
    parser.add_argument('end_month', type=int, help="Ending month, integer 1..12")
    parser.add_argument('end_day', type=int, help="Ending day, integer 1..12")
    args = parser.parse_args()  # will get arguments from command line and validate them
    year = args.year
    start_month = args.start_month
    start_day = args.start_day
    end_month = args.end_month
    end_day = args.end_day
    is_valid(year, start_month, start_day, end_month, end_day)
    days_in_first_month = last_days_first_month(start_day, start_month, end_day, end_month,year)
    number_of_months = months(start_month, end_month)
    counting_days(number_of_months,start_month, days_in_first_month, end_day, year)
    print(counting_days(number_of_months,start_month, days_in_first_month, end_day, year))
if __name__ == "__main__":
    main()
        
