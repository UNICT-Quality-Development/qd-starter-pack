from src.calculator import sum
from src.calculator import div
from src.calculator import sub
from src.calculator import mult


def test_sum():
    assert sum(3,2) == 5

def test_divsion():
    assert div (10,2) == 5

def test_multiplicaiton():
    assert mult(2,3) == 6

def test_sub():
    assert sub(5,3) == 2



