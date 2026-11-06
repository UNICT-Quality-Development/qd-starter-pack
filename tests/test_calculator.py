from src.calculator import sum

def test_sum() -> None:
    assert sum(2,11) == 13
    assert sum(0.12,0.35) == 0.47
    assert type(sum(2,9)) is float
    assert type(sum(0.12,0.35)) is float