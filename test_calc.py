# test_calc.py
from calc import add, divide

def test_add():
    assert add(1, 1) == 2

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
