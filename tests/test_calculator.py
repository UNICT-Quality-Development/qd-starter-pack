from src.calculator import somma
from src.calculator import differenza
from src.calculator import moltiplicazione
from src.calculator import divisione

def test_somma():
    assert somma(3, 5) == 8
    assert somma(5.6, 3) == 8.6

def test_differenza():
    assert differenza(10, 6) == 4
    assert differenza(4, 8) == -4    

def test_moltiplicazione():
    assert moltiplicazione(3, 5) == 15
    assert moltiplicazione(2, 0) == 0

def test_divisione():
    assert divisione(6, 3) == 2
    assert divisione(5, 2) == 2.5
    assert divisione(5, 0) == ZeroDivisionError
