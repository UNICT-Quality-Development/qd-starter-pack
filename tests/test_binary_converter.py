from src.binary_converter import BinaryConverter

def test_binary_converter() -> None:
    assert BinaryConverter(6) == "110"
    assert BinaryConverter(0) == "0"
    assert BinaryConverter(11) == "1011"
