from src import ex3
import pytest

tests_a = [
    { "mock_value": "MathmaGandi", "output_value": "Bapu"  },
    { "mock_value": "BarackObama", "output_value": "44th president of the United States" },
]

@pytest.mark.parametrize("test", tests_a)
def test_ex3(test: dict)->None:
    mock_value = test["mock_value"]
    assert ex3.func(mock_value) == test["output_value"]
