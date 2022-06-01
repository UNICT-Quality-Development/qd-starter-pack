# TEST PARAMETRIZATION
from typing import List
import pytest
from pytest_mock import MockerFixture
from src import calculator

# dict = dictionary (is a set of key:value pairs)
tests: List[dict] = [
    { "res": calculator.calculate(10.0,5.0,"S"), "expected_res": 15.0},
    { "res": calculator.calculate(10.0,5.0,"D"), "expected_res": 5.0},
    { "res": calculator.calculate(10.0,5.0,"M"), "expected_res": 50.0},
    { "res": calculator.calculate(10.0,5.0,"d"), "expected_res": 2.0},
    { "res": calculator.calculate(10.0,0,"d"), "expected_res": 0}    
]

# enables parametrization of arguments for a test function
@pytest.mark.parametrize("test", tests)
def test_generic(test: dict) -> None:
    # arrange
    # act
    res = test["res"]
    # assert
    assert res == test["expected_res"]