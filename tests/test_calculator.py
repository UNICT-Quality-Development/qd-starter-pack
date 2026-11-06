from src import calculator

def test_sum() -> None:
    assert calculator.sum(3, 4) == 7
    assert calculator.sum(0, 0) == 0
    assert calculator.sum(1, 2) == 3
    assert calculator.sum(-1, 1) == 0
    assert calculator.sum(-5, -5) == -10

def test_subtract() -> None:
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(1, 2) == -1
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(-5, -5) == 0

def test_multiply() -> None:
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(1, 2) == 2
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-5, -5) == 25

def test_divide() -> None:
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(-4, 2) == -2
    assert calculator.divide(-6, -3) == 2
    assert calculator.divide(0, 5) == 0
    assert calculator.divide(5, 0) == 0
