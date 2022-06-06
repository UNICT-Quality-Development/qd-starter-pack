from typing import List
import pytest
from pytest_mock import MockerFixture
from src import calculator

tests: List[dict] = [
{ "value_1": 10, "function_1": "first_number", 
    "value_2": 20, "function_2": "second_number", 
    "value_3": 0, "function_3": "randint", "res": calculator.calculate, "expected_res": 30 } ,

    { "value_1": 10, "function_1": "first_number", 
    "value_2": 20, "function_2": "second_number", 
    "value_3": 1, "function_3": "randint", "res": calculator.calculate, "expected_res": -10 } ,   

    { "value_1": 10, "function_1": "first_number", 
    "value_2": 20, "function_2": "second_number", 
    "value_3": 2, "function_3": "randint", "res": calculator.calculate, "expected_res": 200 } ,

    { "value_1": 10, "function_1": "first_number", 
    "value_2": 20, "function_2": "second_number", 
    "value_3": 3, "function_3": "randint", "res": calculator.calculate, "expected_res": 0.5 } ,    
]

@pytest.mark.parametrize("test", tests)
def test_generic(mocker: MockerFixture, test:dict) -> None:
    # arrange
    mocker.patch.object(calculator, test["function_1"] , return_value = test["value_1"])
    mocker.patch.object(calculator, test["function_2"] , return_value = test["value_2"])
    mocker.patch.object(calculator, test["function_3"], return_value = test["value_3"])

    # act
    res = test["res"]()

    # assert
    assert res == test["expected_res"]
    
