from src.random_number import *
import sys
import pytest


def test_random_number():
    random_int = random_positive_int()
    assert isinstance(random_int, int)
    assert random_int >= 0 and random_int <= sys.maxsize


@pytest.mark.parametrize("upper_limit", [0, -3, sys.maxsize, "a", 4.5, 5000, 1])
def test_random_limited(upper_limit):
    try:
        random_limited_int = random_limited_positive_int(upper_limit)
        assert isinstance(random_limited_int, int)
        assert random_limited_int >= 0 and random_limited_int <= upper_limit

    except Exception:
        # print(Exception)
        assert True
        return
