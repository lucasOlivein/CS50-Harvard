from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("Hello dear") == 0
    assert value('hello my friend') == 0

def test_h():
    assert value("Hey, what's up?") == 20
    assert value ("Hi, how are you?") == 20
    assert value("hey man") == 20

def test_():
    assert value("What's up?") == 100
    assert value("Morning") == 100
    assert value("Nice to meet you!")