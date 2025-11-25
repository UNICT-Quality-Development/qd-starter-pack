from src.calculator import div, diff, mult, sum


def test_sum() -> None:
    assert sum(6, 4) == 10


def test_diff() -> None:
    assert diff(4, 5) == -1


def test_mult() -> None:
    assert mult(5, 5) == 25


def test_div() -> None:
    assert div(2, 2) == 1
    assert div(4, 0) == "Cannot divide by 0"
