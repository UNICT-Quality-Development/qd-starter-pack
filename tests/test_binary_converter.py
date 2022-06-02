from src.binary_converter import convert_to_binary

def test_convert_to_binary():
    # Assert
    assert convert_to_binary(1, 2) == '01'
    assert convert_to_binary(12, 4) == '1100'
    assert convert_to_binary(255, 8) == '11111111'
    assert type(convert_to_binary(2, 1)) == type('')