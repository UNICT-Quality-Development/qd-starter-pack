from typing import List
import pytest
from pytest_mock import MockerFixture
from src.ex4 import months
from src import ex4


tests: List[dict] = [
    {"mock_return" : "31 days", "month" : 5},
    {"mock_return" : "30 days", "month" : 9},
    {"mock_return" : "28-29 days", "month" : 2}
]

@pytest.mark.parametrize("test", tests)
def test_binary(mocker: MockerFixture, test: dict) -> None:
    #arrange
    mocker.patch.object(ex4, "months", return_value = test["mock_return"])

    #act
    ret : str = months(test["month"])

    #assert
    assert (ret == test["mock_return"]) is True