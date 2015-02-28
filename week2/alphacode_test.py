def alphacode(pin):
    """
    Convert numeric pin code to an
    easily pronounced mnemonic.
    args:
        pin:  code as positive integer
    returns:
        mnemonic as string
    """
     for i in range(2):
          x = pin 

    
    mnemonic = "This can't be right"
    return mnemonic

def run_tests():
    """
    This function runs a set of tests to help you debug your
    program as you develop it.
    """
    print("**** TESTING --- examples from course assignment page")
    testEQ("4327 => lohi", alphacode(4327), "lohi")
    testEQ("1298 => dizo", alphacode(1298), "dizo")
    print("***** Longer PIN codes ****")
    testEQ("1234567 => begomari?", alphacode(1234567), "begomari")
    testEQ("42424242 => lililili ?", alphacode(42424242), "lililili")
    testEQ("98765 => cuwira?", alphacode(98765), "cuwira")
    testEQ("987654 => zotenu?", alphacode(987654), "zotenu")
    testEQ("(same digit pairs, reverse order) 547698 => nutezo ?", alphacode(547698), "nutezo")
    print("**** Edge cases (robustness testing) ****")
    testEQ("0 => empty mnemonic ?", alphacode(0), "")
    testEQ("-42 and all negative numbers => empty mnemonic? ", alphacode(-42), "")
    print("*** End of provided test cases.  Add some of your own? ****")
