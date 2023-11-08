import pytest
from src.binary_converter import decimal_to_binary

def test_binary_converter():
    # Verifica che 1 venga convertito correttamente in "1"
    assert decimal_to_binary(1) == '1'
    
    # Verifica che 2 venga convertito correttamente in "10"
    assert decimal_to_binary(2) == '10'
    
    # Verifica che 9 venga convertito correttamente in "1001"
    assert decimal_to_binary(9) == '1001'
    
    # Verifica che 63 venga convertito correttamente in "111111"
    assert decimal_to_binary(63) == '111111'
    
    # Verifica che 256 venga convertito correttamente in "100000000"
    assert decimal_to_binary(256) == '100000000'
    
    # Verifica che numeri negativi generino un'eccezione ValueError
    with pytest.raises(ValueError):
        decimal_to_binary(-5)

    # Verifica che 0 venga convertito correttamente in "0"
    assert decimal_to_binary(0) == '0'
    
    # Verifica che numeri molto grandi vengano convertiti correttamente
    assert decimal_to_binary(1024) == '10000000000'