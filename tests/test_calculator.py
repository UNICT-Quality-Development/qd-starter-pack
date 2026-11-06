from typing import List

import pytest

from src import calculator

tests: List[dict] = [
    {"func": calculator.add, "a": 4.0, "b": 2.0, "expected": 6.0},
    {"func": calculator.add, "a": -1.0, "b": 5.0, "expected": 4.0},
    {"func": calculator.subtract, "a": 4.0, "b": 2.0, "expected": 2.0},
    {"func": calculator.subtract, "a": 2.0, "b": 5.0, "expected": -3.0},
    {"func": calculator.multiply, "a": 4.0, "b": 2.0, "expected": 8.0},
    {"func": calculator.multiply, "a": 3.0, "b": 0.0, "expected": 0.0},
    {"func": calculator.divide, "a": 4.0, "b": 2.0, "expected": 2.0},
    {"func": calculator.divide, "a": 5.0, "b": 2.0, "expected": 2.5},
]


@pytest.mark.parametrize("test", tests)
def test_operations(test: dict) -> None:
    # arrange
    func = test["func"]
    val_a = test["a"]
    val_b = test["b"]
    expected = test["expected"]

    # act
    result = func(val_a, val_b)

    # assert
    assert result == expected


def test_divide_by_zero() -> None:
    # arrange
    val_a = 4.0
    val_b = 0.0

    # act & assert
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calculator.divide(val_a, val_b)