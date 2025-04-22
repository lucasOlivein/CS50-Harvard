from um import count

def test_num():
    assert count("um, um, dois") == 2
    assert count("Hello, um, world") == 1
    assert count("Hello dear") == 0

def test_case_insensitive():
    assert count("UM, um, dois") == 2
    assert count("Hello, UM, world") == 1

def test_similar_world():
    assert count("Yummi, umm, uma") == 0
    assert count("UMm, Umn, yum") == 0