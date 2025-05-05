from fuel import convert
from fuel import gauge
import pytest

#Testing convert
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/5") == 20
    assert convert("1/1") == 100
    assert convert("0/5") == 0

#Testing gauge
def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(20) == "20%"
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

def test_value_error():
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("4/3")

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

