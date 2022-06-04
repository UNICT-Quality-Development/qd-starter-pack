from typing import List
import pytest
from pytest_mock import MockerFixture
from src.binary_converter import bin_conv
from src import binary_converter


tests: List[dict] = [
    {"mock_return" : "110", "param" : 6},
    {"mock_return" : "1111111", "param" : 127},
    {"mock_return" : "11010010010011", "param" : 13459},
    {"mock_return" : "0", "param" : 0}
]

@pytest.mark.parametrize("test", tests)
def test_binary(mocker: MockerFixture, test: dict) -> None:
    #arrange
    mocker.patch.object(binary_converter, "bin_conv", return_value = test["mock_return"])

    #act
    ret : str = bin_conv(test["param"])

    #assert
    assert (ret == test["mock_return"]) is True

