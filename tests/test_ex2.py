from pytest_mock import MockerFixture
import pytest
from typing import List
from src import ex2

tests: List[dict] = [
    { "mock_value": '1', "mock_function": "input", "res": ex2.week_number, "expected_res": 'Monday' },
    { "mock_value": '2', "mock_function": "input", "res": ex2.week_number, "expected_res": 'Tuesday' },
    { "mock_value": '3', "mock_function": "input", "res": ex2.week_number, "expected_res": 'Wednesday' },
    { "mock_value": '4', "mock_function": "input", "res": ex2.week_number, "expected_res": 'Thursday' },
    { "mock_value": '5', "mock_function": "input", "res": ex2.week_number, "expected_res": 'Friday' },
    { "mock_value": '6', "mock_function": "input", "res": ex2.week_number, "expected_res": 'Saturday' },
    { "mock_value": '7', "mock_function": "input", "res": ex2.week_number, "expected_res": 'Sunday' },
    { "mock_value": '9', "mock_function": "input", "res": ex2.week_number, "expected_res": '' }
]

@pytest.mark.parametrize("test", tests)
def test_week_number(mocker: MockerFixture, test: dict) -> None:

    #arrange 
    mocker.patch.object(ex2, test['mock_function'], return_value=test["mock_value"])

    #act
    res = test["res"]()

    #assert
    assert res == test["expected_res"]
    assert type(res) is str
