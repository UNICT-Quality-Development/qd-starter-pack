from src.esercizio_somma import sum

def test_sum()-> None:
    assert sum(3,4) == 7
    assert sum(9,8) == 17
    assert sum(2,3) == 5
    assert sum(88, 100) == 188
