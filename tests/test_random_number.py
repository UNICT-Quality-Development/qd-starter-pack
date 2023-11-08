from src.random_number import random_number

def test_random_number() -> None:
    t = random_number(0, 100)
    assert t >= 0 and t <= 100
