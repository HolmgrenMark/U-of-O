CONSONANTS = "bcdfghjklmnpqrstvwyz" 
VOWELS = "aeiou"  
global mnemonic
mnemonic = ''

def alphacode(pin):
    """
    Convert numeric pin code to an
    easily pronounced mnemonic.
    args:
        pin:  code as positive integer
    returns:
        mnemonic as string
    """
    #FIXME: Your code replaces the next line
    
    while(pin > 0):
       sub = pin % 100

       VOWELS_location = sub % 5
       CONSONANTS_location = sub // 5
       global mnemonic

       if (mnemonic == ''):
           mnemonic = CONSONANTS[CONSONANTS_location] + VOWELS[VOWELS_location]

       else:
           mnemonic = CONSONANTS[CONSONANTS_location] + VOWELS[VOWELS_location] + mnemonic       
       
       pin = pin // 100

       print(mnemonic)
alphacode(1234)
