from src.calculator import operation, OperationType

def test_calculator_operations() -> None:
    assert operation(4, 2, op=OperationType.SUM) == 6  # SUM
    assert operation(4, 2, op=OperationType.DIFFERENCE) == 2  # DIFFERENCE
    assert operation(4, 2, op=OperationType.MULTIPLICATION) == 8  # MULTIPLICATION
    assert operation(4, 2, op=OperationType.DIVISION) == 2  # DIVISION
    try:
        operation(4, 0, op=OperationType.DIVISION)
    except ValueError as e:
        assert str(e) == "Error: Division by zero"  # DIVISION by zero
    try:
        operation(4, 2, op=None)  # Invalid operation
    except ValueError as e:
        assert str(e) == "Invalid operation"
        
def test_calculator_main() -> None:
    import builtins
    import io
    import sys

    input_values = ["4", "2"]
    output = io.StringIO()
    sys.stdout = output

    def mock_input(s):
        return input_values.pop(0)

    builtins.input = mock_input

    # Re-import the main module to run the main function
    import src.calculator as calculator_module

    # Restore stdout
    sys.stdout = sys.__stdout__

    expected_output = (
        "Insert first number: Insert second number: SUM: 6.0\n"
        "Difference: 2.0\n"
        "Multiplication: 8.0\n"
        "Division: 2.0\n"
    )

    assert output.getvalue() == expected_output