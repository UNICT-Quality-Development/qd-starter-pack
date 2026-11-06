import pytest
from typing import List
from pytest_mock import MockerFixture
from src.calculator import sum, diff, mult, div


tests: List[dict] = [
    {"value1": 1, "value2": 2, "res": sum, "expected_result": 3},
    {"value1": 7, "value2": 2, "res": diff, "expected_result": 5},
    {"value1": 7, "value2": 2, "res": mult, "expected_result": 14},
    {"value1": 7, "value2": 2, "res": div, "expected_result": 3.5}
]

@pytest.mark.parametrize("test", tests)
def test_sum(mocker: MockerFixture, test: dict) -> None:    
    
    a = test["value1"]
    b = test["value2"]

    res = test["res"](a, b)

    assert res == test["expected_result"]

