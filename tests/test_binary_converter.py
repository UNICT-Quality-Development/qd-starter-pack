from src.binary_converter import to_binary

def test_to_binary() -> None:
    assert to_binary(0) == 0
    assert to_binary(1) == 1
    assert to_binary(2) == 10
    assert to_binary(1234) == 10011010010
