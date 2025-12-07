from src.binary_converter import binary_converter

def test_binary_converter() -> None:
    assert binary_converter(8) == "1000"
    assert binary_converter(0) == "0"
    assert binary_converter(5) == "101"
    assert binary_converter(15) == "1111"