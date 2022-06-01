from typing import List
import pytest
from pytest_mock import MockerFixture
from src.randnum import rand
from src import randnum


tests: List[dict] = [
    {"mock_return" : 34, "seed" : 49509864, "param1" : 0, "param2" : 100},
    {"mock_return" : 307, "seed" : 6539490, "param1" : 10, "param2" : 567},
    {"mock_return" : 9172017, "seed" : 584893905, "param1" : 500000, "param2" : 21596848}
]

@pytest.mark.parametrize("test", tests)
def test_binary(mocker: MockerFixture, test: dict) -> None:
    #arrange
    mocker.patch.object(randnum, "rand", return_value = test["mock_return"])

    #act
    ret : str = rand(test["seed"], test["param1"], test["param2"])

    #assert
    assert (ret == test["mock_return"]) is True
