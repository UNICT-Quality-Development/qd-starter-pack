from calculator import add,subtract,multiply,divide,read_integer
import pytest

def test_add() -> None:

    assert add(3,5) == 8
    assert type(sum(3,5)) is int

def test_sub() -> None:

    assert subtract(3,5) == -2
    assert type(subtract(3,5)) is int

def test_mul() -> None:

    assert multiply(4,0) == 0

def test_div() -> None:

    with pytest.raises(ZeroDivisionError):
        divide(4,0)

