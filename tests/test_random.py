from src.random_number import generate

def test_random() -> None:
    assert generate() <= 10 and generate() >= 1
