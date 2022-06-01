from curses.ascii import isdigit
from src.random_num import random_num
def test_random_num()->None:
    assert type(random_num())==int