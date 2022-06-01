from src.binary_converter import toBinary

def test_binary_converter()->None:
    assert toBinary(8) = "1000"
    assert toBinary(4) = "100"
    assert toBinary(17) = "10001"
