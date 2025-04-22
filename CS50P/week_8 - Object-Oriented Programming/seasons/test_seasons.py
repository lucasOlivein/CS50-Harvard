from seasons import convert_date_to_min, convert_num_to_words
from datetime import date



def test_words():
    assert convert_num_to_words(1) == "One minute"
    assert convert_num_to_words(2) == "Two minutes"
    assert convert_num_to_words(100) == "One hundred minutes"

def test_convert_date_to_min():
    assert convert_date_to_min(birth= date(2024,4,11), today= date(2025,4,11)) == 525600
