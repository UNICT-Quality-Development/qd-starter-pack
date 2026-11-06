import pytest

from src import calculator


@pytest.mark.parametrize("values", [
    { "x": 3, "y": 2, "res": 5},
    { "x": -5, "y": 7, "res": 2},
    { "x": "8", "y": "2", "res": 10},
    { "x": "8", "y": 2, "res": 10},
    { "x": 1.5, "y": 2, "res": 3.5},
])
def test_sum(values: dict) -> None:
    sum_result: float = calculator.sum(values["x"], values["y"])

    assert sum_result == values["res"]


@pytest.mark.parametrize("values", [
    { "x": 3, "y": 2, "res": 1 },
    { "x": -5, "y": 7, "res": -12 },
    { "x": "8", "y": "2", "res": 6 },
    { "x": "8", "y": 2, "res": 6 },
    { "x": 1.5, "y": 2, "res": -0.5 },
])
def test_difference(values: dict) -> None:
    difference_result: float = calculator.difference(values["x"], values["y"])

    assert difference_result == values["res"]


@pytest.mark.parametrize("values", [
    { "x": 3, "y": 2, "res": 6 },
    { "x": -5, "y": 7, "res": -35 },
    { "x": "8", "y": "2", "res": 16 },
    { "x": "8", "y": 2, "res": 16 },
    { "x": 1.5, "y": 2, "res": 3.0 },
])
def test_multiplication(values: dict) -> None:
    multiplication_result: float = calculator.multiplication(values["x"], values["y"])

    assert multiplication_result == values["res"]


@pytest.mark.parametrize("values", [
    { "x": 3, "y": 2, "res": 1.5 },
    { "x": "8", "y": "2", "res": 4 },
    { "x": "8", "y": 2, "res": 4 },
    { "x": -5, "y": 2, "res": -2.5 },
    { "x": 10, "y": 0, "res": 0 },
])
def test_division(values: dict) -> None:
    division_result: float = calculator.division(values["x"], values["y"])

    assert division_result == values["res"]
