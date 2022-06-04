from src.binary_converter import convert

def test_binary_converter() -> None:
    assert convert(8) == "1000"
    assert convert(5) == "101"
    assert convert(127) == "1111111"