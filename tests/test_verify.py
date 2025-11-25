from src.verify import contains


def test_contains() -> None:
    assert contains(5) == False
    assert contains(1) == True
    assert contains("1") == False
    assert contains(1.0) == True
