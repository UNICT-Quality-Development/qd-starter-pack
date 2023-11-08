from src.calculator import calculator

def test_calculator()->None:
    assert calculator(3, 5) == 'SUM: 8, Difference: -2, Multiplication: 15, Division: 0.6'
    assert calculator(5, 9) == 'SUM: 14, Difference: -4, Multiplication: 45, Division: 0.5555555555555556'
    assert calculator(6, 3) == 'SUM: 9, Difference: 3, Multiplication: 18, Division: 2.0'