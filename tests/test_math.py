from src.math import add, subtract, multiply, divide


def test_add():
    assert add(3, 2) == 5


def test_subtract():
    assert subtract(3, 2) == 1


def test_multiply():
    assert multiply(3, 2) == 6


def test_divide_int():
    assert divide(1,1) == 1

def test_divide_float():
    assert divide(3,2) == 1.5
