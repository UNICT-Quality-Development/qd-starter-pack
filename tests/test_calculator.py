from src.calculator import operation, OperationType


def test_calculator_operations() -> None:
    assert operation(4, 2, op=OperationType.SUM) == 6  # SUM
    assert operation(4, 2, op=OperationType.DIFFERENCE) == 2  # DIFFERENCE
    assert operation(4, 2, op=OperationType.MULTIPLICATION) == 8  # MULTIPLICATION
    assert operation(4, 2, op=OperationType.DIVISION) == 2  # DIVISION
    try:
        operation(4, 0, op=OperationType.DIVISION)
        assert False
    except ValueError as _:
        assert True
