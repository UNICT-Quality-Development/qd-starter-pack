import pytest
from typing import List
from pytest_mock import MockerFixture
from src.risk_risiko import risiko
from src import risk_risiko


tests: List[dict] = [
    {"mock_return" : [0,0,1], "param1" : [5, 4, 3], "param2" : [5, 4, 2]},
    {"mock_return" : [0,0,0], "param1" : [0, 0, 0], "param2" : [0, 0, 0]},
    {"mock_return" : [0,1,1], "param1" : [5, 4, 3], "param2" : [6, 2, 1]},
]

@pytest.mark.parametrize("test", tests)
def test_risiko(mocker: MockerFixture, test: dict) -> None:
    #arrange
    mocker.patch.object(risk_risiko, "risiko", return_value=test["mock_return"])

    #act
    ret: bool = risiko(test["param1"], test["param2"])

    #assert
    assert (ret == test["mock_return"])