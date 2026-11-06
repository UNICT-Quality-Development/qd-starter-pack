from pytest_mock import MockerFixture
from src.calculator import func_sum, difference, multiplication, division
 

def test_func_sum() -> None:
    assert func_sum(3, 8) == 11
    assert func_sum(-1, 8) == 7
    assert type(func_sum(3, 4)) is int


def test_difference() -> None:
    assert difference(3, 8) == -5
    assert difference(-1, 8) == -9
    assert type(difference(3, 4)) is int


def test_multiplication() -> None:
    assert multiplication(3, 8) == 24
    assert multiplication(-1, 8) == -8
    assert type(multiplication(3, 4)) is int


def test_division() -> None:
    assert division(3, 8) == 0
    assert division(-1, 8) == 0
    assert type(division(3, 4)) is int
