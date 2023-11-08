import pytest
from src.calculator import  somma,sottrazione,divisione,moltiplicazione

# Test con 2 valori positivi
def test_calculator_1_1():
    # Verifica somma
    assert somma(1,1) == 2
    
    # Verifica sottrazione
    assert sottrazione(1,1) == 0
    
    # Verifica divisione
    assert divisione(1,1) == 1
    
    # Verifica moltiplicazione
    assert moltiplicazione(1,1) == 1

# Test con secondo numero = 0
def test_calculator_10_0():
    # Verifica somma
    assert somma(10,0) == 10
    
    # Verifica sottrazione
    assert sottrazione(10,0) == 10
    
    # Verifica divisione
    with pytest.raises(ValueError):
        divisione(10,0)
    
    # Verifica moltiplicazione
    assert moltiplicazione(10,0) == 0

# Test con primo numero = 0
def test_calculator_0_10():
    # Verifica somma
    assert somma(0,10) == 10
    
    # Verifica sottrazione
    assert sottrazione(0,10) == -10
    
    # Verifica divisione
    assert divisione(0,10) == 0
    
    # Verifica moltiplicazione
    assert moltiplicazione(0,10) == 0

# Test con numeri negativi
def test_calculator_n1_n1():
    # Verifica somma
    assert somma(-1,-1) == -2
    
    # Verifica sottrazione
    assert sottrazione(-1,-1) == 0
    
    # Verifica divisione
    assert divisione(-1,-1) == 1
    
    # Verifica moltiplicazione
    assert moltiplicazione(-1,-1) == 1









