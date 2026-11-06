from src.calculator import calc 


def test_calc() -> None:
    expected_values1 = (6, -2, 8, 0.5)
    expected_values2 = (0, 0, 0, "Undefined (division by zero)")
    expected_values3 = (5, 1, 6, 1.5)
    expected_values4 = (10, 0, 25, 1.0)

    calculator_results1 = calc(2, 4)
    calculator_results2 = calc(0, 0)
    calculator_results3 = calc(3, 2)
    calculator_results4 = calc(5, 5)

    assert calculator_results1 == expected_values1
    assert calculator_results2 == expected_values2
    assert calculator_results3 == expected_values3
    assert calculator_results4 == expected_values4

