from src.sum import sum

def test_sum() -> None:
    assert sum(3,4) == 7
    assert sum(0,0) == 0
    assert sum(1.5,2) == 3.5
