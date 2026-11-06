from src.sum import sum

def test_sum() -> None:
    assert sum(1, 2) == 3
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0
    assert sum(-5, -5) == -10

    assert isinstance(sum(1, 2), int)
