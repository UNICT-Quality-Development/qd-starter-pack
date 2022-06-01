from src.binary_converter import binary_converter

def test_binary_converter() -> None:
    assert binary_converter(8) == 1000
    assert binary_converter(4) == 100
    assert binary_converter(2) == 10