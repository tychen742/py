# test_math.py
def test_add():
    assert 1 + 1 == 2

def test_divide():
    assert 10 / 2 == 5.0

def test_divide_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        1 / 0