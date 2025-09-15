import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_sub():
    assert calculator.sub(5, 0) == 5
    assert calculator.sub(9, 4) == 5
    assert calculator.sub(4, 7) == -3

def test_mul():
    assert calculator.mul(4, 0) == 0
    assert calculator.mul(3, 2) == 6
    assert calculator.mul(1, 3) == 3

def test_div():
    assert calculator.div(10, 5) == 2
    assert calculator.div(3, 1) == 3

def test_div_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by Zero!"):
        calculator.div(10, 0)
