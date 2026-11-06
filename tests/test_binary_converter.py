import pytest
from src.binary_converter import dec_to_bin

@pytest.mark.parametrize("num, expected", [(0, "0"), (3, "11"), (10, "1010")])
def test_dec_to_bin(num: int, expected: str) -> None:
    assert dec_to_bin(num) == expected

def test_dec_to_bin_negative() -> None:
    with pytest.raises(AssertionError):
        dec_to_bin(-1)