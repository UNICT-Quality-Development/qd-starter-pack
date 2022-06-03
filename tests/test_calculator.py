from src.calculator import Calculator

def test_calculator() -> None:
    assert Calculator(15, 3) == (18, 12, 45, 5)
    assert Calculator(12, 4) == (16, 8, 48, 3)
    assert Calculator(100,10) == (110, 90, 1000, 10)
