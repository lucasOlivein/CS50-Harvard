from plates import is_valid


#Testing the len of min 2 and max of 6
def test_len():
    assert is_valid("") == False
    assert is_valid("H") == False
    assert is_valid("CS") == True
    assert is_valid("CS5010") == True
    assert is_valid("OUTATIME") == False

# Testing the 2 letter at the start condition
def test_start():
    assert is_valid(" CS50") == False
    assert is_valid("1CS50") == False
    assert is_valid("C1S50") == False
    assert is_valid("1CSS") == False
    assert is_valid("12ABCD1") == False
    assert is_valid("5CSSS") == False

#Testing the condition of number at middle not be allowed and
#the first number cannot be zero
def test_middler():
    assert is_valid("CS50P") == False
    assert is_valid("CS500P") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS05") == False

#Testing periods, spaces, or punctuation marks
def test_pontuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS500.") == False
    assert is_valid("CS...") == False
    assert is_valid(".CS50") == False
    assert is_valid("CS50") == True

def test_start_alphabetical():
    assert is_valid("12345") == False


