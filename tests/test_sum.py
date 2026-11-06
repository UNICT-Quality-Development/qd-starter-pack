from src.sum import sum


def test_sum() -> None:
    assert sum(3, 4) == 7
    assert sum(0, 0) == 0
    assert sum(1, 2) == 3
    assert sum(1, 4) == 5
    assert type(sum(1, 2)) == int

