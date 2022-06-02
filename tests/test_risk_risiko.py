import pytest
from typing import List
from pytest_mock import MockerFixture
from src.risk_risiko import risiko
from src import risk_risiko


tests: List[dict] = [
    {"mock_return" : 0, "param1" : 3, "param2" : 3},
    {"mock_return" : 1, "param1" : 6, "param2" : 4},
    {"mock_return" : 0, "param1" : 5, "param2" : 6},
]

@pytest.mark.parametrize("test", tests)
def test_risiko(mocker: MockerFixture, test: dict) -> None:
    #arrange
    mocker.patch.object(risk_risiko, "risiko", return_value=test["mock_return"])

    #act
    ret: bool = risiko(test["param1"], test["param2"])

    #assert
    assert (ret == test["mock_return"])