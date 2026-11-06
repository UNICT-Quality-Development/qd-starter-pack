from src.calculator import calc, sum, diff, mul, div

import pytest 

from pytest_mock import MockerFixture

CALC_CASES = [
    (2, 4, (6, -2, 8, 0.5)),
    (0, 0, (0, 0, 0, None)),  
    (3, 2, (5, 1, 6, 1.5)),
    (5, 5, (10, 0, 25, 1.0)),
]

@pytest.mark.parametrize("num1, num2, expected", CALC_CASES)
def test_sum(num1: int, num2: int, expected: int) -> None:
    assert sum(num1, num2) == expected[0]

@pytest.mark.parametrize("num1, num2, expected", CALC_CASES)
def test_diff(num1: int, num2: int, expected: int) -> None:
    assert diff(num1, num2) == expected[1]

@pytest.mark.parametrize("num1, num2, expected", CALC_CASES)
def test_mul(num1: int, num2: int, expected: int) -> None:
    assert mul(num1, num2) == expected[2]

@pytest.mark.parametrize("num1, num2, expected", CALC_CASES)
def test_div(num1: int, num2: int, expected: float) -> None:
    assert div(num1, num2) == expected[3]

@pytest.mark.parametrize("num1, num2, expected", CALC_CASES)
def test_calc(mocker: MockerFixture, num1: int, num2: int, expected: tuple) -> None:
    mocker.patch("src.calculator.sum", return_value=expected[0])
    mocker.patch("src.calculator.diff", return_value=expected[1])
    mocker.patch("src.calculator.mul", return_value=expected[2])
    mocker.patch("src.calculator.div", return_value=expected[3])

    result = calc(num1, num2)

    assert result == expected

