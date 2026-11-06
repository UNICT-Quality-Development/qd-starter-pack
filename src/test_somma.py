import sum
import pytest_mock
import pytest

def test_somma() -> None:
    assert sum.sum(1, 2) == 3
    assert sum.sum(-1, 1) == 0
    assert sum.sum(1, 4) == 5
    assert type(sum.sum(1, 2)) == int