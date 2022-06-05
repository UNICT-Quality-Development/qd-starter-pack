from typing import List
import pytest
from pytest_mock import MockerFixture
from src import calculator

tests: List[dict] = [
{ "mock_value_1": 10, "mock_function_1": "first_number", 
    "mock_value_2": 20, "mock_function_2": "second_number", 
    "mock_value_3": 0, "mock_function_3": "randint", "res": calculator.calculate, "expected_res": 30 } ,

    { "mock_value_1": 10, "mock_function_1": "first_number", 
    "mock_value_2": 20, "mock_function_2": "second_number", 
    "mock_value_3": 1, "mock_function_3": "randint", "res": calculator.calculate, "expected_res": -10 } ,   

    { "mock_value_1": 10, "mock_function_1": "first_number", 
    "mock_value_2": 20, "mock_function_2": "second_number", 
    "mock_value_3": 2, "mock_function_3": "randint", "res": calculator.calculate, "expected_res": 200 } ,

    { "mock_value_1": 10, "mock_function_1": "first_number", 
    "mock_value_2": 20, "mock_function_2": "second_number", 
    "mock_value_3": 3, "mock_function_3": "randint", "res": calculator.calculate, "expected_res": 0.5 } ,    
]

@pytest.mark.parametrize("test", tests)
def test_generic(mocker: MockerFixture, test:dict) -> None:
    # arrange

    mocker.patch.object(calculator, test["mock_function_1"] , return_value = test["mock_value_1"])
    mocker.patch.object(calculator, test["mock_function_2"] , return_value = test["mock_value_2"])
    mocker.patch.object(calculator, test["mock_function_3"], return_value = test["mock_value_3"])

    # act
    res = test["res"]()

    # assert
    assert res == test["expected_res"]
    
