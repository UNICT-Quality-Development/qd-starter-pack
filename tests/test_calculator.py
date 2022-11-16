from src.calculator import sum, difference, multiplication, division, all

def test_sum ():
    assert(sum(4, 2) == 6)
    assert(sum(29, 95) == 124)

def test_all ():
    assert(all(4, 2) == [6, 2, 8, 2])
