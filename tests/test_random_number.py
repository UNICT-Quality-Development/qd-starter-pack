from typing import List

import pytest
from pytest_mock import MockerFixture

from src import random_number

tests: List[dict] = [
    {
        "mock_value": 4,
        "expected_res": 4,
    },
    {
        "mock_value": 9,
        "expected_res": 9,
    },
]


@pytest.mark.parametrize("test", tests)
def test_get_random_number(mocker: MockerFixture, test: dict) -> None:
    # arrange
    mocker.patch.object(
        random_number,
        "randint",
        return_value=test["mock_value"],
    )
    spy = mocker.spy(random_number, "randint")

    # act
    res = random_number.get_random_number()

    # assert
    assert res == test["expected_res"]
    assert spy.call_count == 1
    assert spy.spy_return == test["mock_value"]
