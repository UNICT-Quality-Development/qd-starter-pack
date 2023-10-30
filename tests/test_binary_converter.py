from src.binary_converter import binary_converter


def test_binary_converter() -> None:
    assert binary_converter(7) == "111"
    assert binary_converter(13) == "1101"
    assert binary_converter(128) == "10000000"
