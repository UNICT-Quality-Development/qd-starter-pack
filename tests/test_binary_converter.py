from src.binary_converter import binary_convert


def test_binary_converter() -> None:
    assert binary_convert(3) == '0b11'
    assert binary_convert(7) == '0b111'
    assert binary_convert(15) == '0b1111'
