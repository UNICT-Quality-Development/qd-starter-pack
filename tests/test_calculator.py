from src.calculator import sum, difference, multiplication, division


def test_sum() -> None:

    assert sum(3, 4) == 7
    assert sum(0, 1) == 1
    assert sum(1, 2) == 3


def test_difference() -> None:

    assert difference(3, 4) == -1
    assert difference(0, 1) == -1
    assert difference(5, 1) == 4


def test_multiplication() -> None:

    assert multiplication(3, 4) == 12
    assert multiplication(0, 1) == 0
    assert multiplication(3, 2) == 6


def test_division() -> None:

    assert division(8, 4) == 2
    assert division(5, 1) == 5
    assert division(-8, 4) == -2
    assert division(4, -2) == -2
