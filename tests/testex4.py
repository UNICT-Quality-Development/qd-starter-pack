import src.ex4 as ex4
import pytest
from pytest_mock import MockerFixture

test_a = [
    { "mock_value":1, "output":"31 days"}
    ]


@pytest.mark.parametrize("test", test_a)
def test_ex4(test : dict)->None:
    mock_value = test["mock_value"]

    output = ex4.func(mock_value)
    assert output == test["output"]

