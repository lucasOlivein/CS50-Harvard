from twttr import shorten


def test_upper_case():
    assert shorten('TEST') == 'TST'
    assert shorten('MY NAME IS CHROME') == 'MY NM S CHRM'
    assert shorten('MY NAME IS VS CODE') == 'MY NM S VS CD'


def test_lower_case():
    assert shorten('test') == 'tst'
    assert shorten('my name is chrome') == 'my nm s chrm'
    assert shorten('my name is vs code') == 'my nm s vs cd'


def test_ponctuation():
    assert shorten('This is the answer: 42.') == 'Ths s th nswr: 42.'
