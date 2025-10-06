from src.calculator import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 1) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1