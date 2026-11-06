import random
from src import verify
import pytest

@pytest.mark.parametrize("input", [ random.randint(0,16) for _ in range(0,4) ])
@pytest.mark.parametrize("array", [ [random.randint(0,16) for _ in range(0,16)] for _ in range(0,4) ])
def test_verify(input: int, array: list[int]) -> None:
    result = verify.is_in_array(input, array)
    assert result == ( input in array )
    assert isinstance(result, bool)