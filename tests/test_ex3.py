from typing import List
import pytest
from pytest_mock import MockerFixture
from src.ex3 import famous_names
from src import ex3


tests: List[dict] = [
    {"mock_return" : "Creator of C", "name" : "DennisRitchie"},
    {"mock_return" : "44th president of the United States", "name" : "BarackObama"},
    {"mock_return" : "Bapu", "name" : "MahatmaGandhi"}
]

@pytest.mark.parametrize("test", tests)
def test_ex3(mocker: MockerFixture, test: dict) -> None:
    #arrange
    mocker.patch.object(ex3, "famous_names", return_value = test["mock_return"])

    #act
    ret : str = famous_names(test["name"])

    #assert
    assert (ret == test["mock_return"])