from working import convert
import pytest

def test_base():
    assert convert("10 PM to 5 AM") == "22:00 to 05:00"
    assert convert("5 PM to 8 PM") == "17:00 to 20:00"
    assert convert("10 AM to 1 PM") == "10:00 to 13:00"
    assert convert("10 AM to 12 AM") == "10:00 to 00:00"
        

def test_firt_hour():
    assert convert("10:39 PM to 5 AM") == "22:39 to 05:00"
    assert convert("5:01 PM to 8 PM") == "17:01 to 20:00"
    assert convert("10:25 AM to 1 PM") == "10:25 to 13:00"
    assert convert("10:45 AM to 12 AM") == "10:45 to 00:00"
        


def test_sec_hour():
    assert convert("10 PM to 5:40 AM") == "22:00 to 05:40"
    assert convert("5 PM to 8:31 PM") == "17:00 to 20:31"
    assert convert("10 AM to 1:50 PM") == "10:00 to 13:50"
    assert convert("10 AM to 12:11 AM") == "10:00 to 00:11"
        

def test_errors():
    with pytest.raises(ValueError):
        assert convert("10 PM - 5 AM")
    with pytest.raises(ValueError):
        assert convert("10 PM to 0 AM")
    with pytest.raises(ValueError):
        assert convert("10 PM to Five AM")
    with pytest.raises(ValueError):
        assert convert("10 PM to 14 AM")
    with pytest.raises(ValueError):
        assert convert("10:70 AM to 12 AM")
    with pytest.raises(ValueError):
        assert convert("0 to 12 AM")
    with pytest.raises(ValueError):
        assert convert("Ten to 12 AM")
    with pytest.raises(ValueError):
        assert convert("13 PM to 12 AM")
    with pytest.raises(ValueError):
        assert convert("13 PM to 14 PM")