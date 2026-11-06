from typing import List

import pytest
from pytest_mock import MockerFixture

from src import random_number

tests: List[dict] = [
    {
        "mock_value": 4,
        "mock_function": "randint",
        "res": random_number.get_random_number,
        "expected_res": 4,
    },
    {
        "mock_value": 9,
        "mock_function": "randint",
        "res": random_number.get_random_number,
        "expected_res": 9,
    },
]


@pytest.mark.parametrize("test", tests)
def test_get_random_number(mocker: MockerFixture, test: dict) -> None:
    # arrange
    mocker.patch.object(
        random_number,
        test["mock_function"],
        return_value=test["mock_value"],
    )
    spy = mocker.spy(random_number, test["mock_function"])

    # act
    res = test["res"]()

    # assert
    assert res == test["expected_res"]
    assert spy.call_count == 1
    assert spy.spy_return == test["mock_value"]