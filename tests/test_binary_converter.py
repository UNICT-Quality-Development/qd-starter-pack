from src.binary_converter import convert

def test_convert():
    assert(convert(10) == "00000000000000000000000000001010")