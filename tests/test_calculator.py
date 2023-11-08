from src.calculator import sum
from src.calculator import dif
from src.calculator import mul
from src.calculator import div

def test_sum() -> None:
    assert sum(3,4) == 7
    assert sum(0,0) == 0

def test_dif() -> None:
    assert dif(4,3) == 1
    assert dif(5,5) == 0

def test_mul() -> None:
    assert mul(4,3) == 12
    assert mul(5,0) == 0

def test_div() -> None:
    assert div(8,4) == 2
    assert div(4,1) == 4
