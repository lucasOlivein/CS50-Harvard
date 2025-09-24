from numb3rs import validate



def test_dots():
    assert validate("127.0.0.1") == True
    assert validate("127..0.0.1") == False
    assert validate("127.0..1.0") == False
    assert validate("127.0.0..0") == False
    assert validate("127.0.0.1.") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False