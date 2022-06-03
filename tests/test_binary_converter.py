from src.binary_converter import to_binary

def test_binary_converter()->None:
    assert to_binary(8) == "1000"
    assert to_binary(4) == "100"
    assert to_binary(17) == "10001"
