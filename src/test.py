#from pytest import pytest
import pytest
from calculator_ import*

def test_somma() -> None:
    assert Somma(3,4) == 7
def test_differenza() -> None:
    assert Differenza(3,4) == -1
def test_moltiplicazione() -> None:
    assert Moltiplicazione(3,4) == 12
def test_sottrazione() -> None:
    assert Divisione(4,2) == 2
#mocker va usato solo su funzioni terze
#spy  