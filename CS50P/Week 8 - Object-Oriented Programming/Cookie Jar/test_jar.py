from jar import Jar
import pytest

def test_init():
    assert Jar(1).capacity == 1
    assert Jar(2).capacity == 2
    assert Jar().capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(1)
    assert jar.size == 2
    jar.deposit(5)
    assert jar.size == 7
    jar.deposit(5)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)
    


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(5)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)