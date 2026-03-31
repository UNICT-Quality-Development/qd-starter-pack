from src.verify import contains


def test_contains() -> None:
    assert contains(5) is False
    assert contains(1) is True
