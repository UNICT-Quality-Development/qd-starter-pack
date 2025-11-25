from src.calculator import add, sub, mul, div


def test_add() -> None:
    assert add(5, 4) == 9
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_sub() -> None:
    assert sub(1, 1) == 0
    assert sub(0, 5) == -5


def test_mul() -> None:
    assert mul(5, 1) == 5
    assert mul(0, 5) == 0
    assert mul(-2, 3) == -6


def test_div() -> None:
    assert div(5, 1) == 5
    assert div(0, 5) == 0
    assert div(5, 0) == "You can't divide by 0"
    assert div(-6, 2) == -3
