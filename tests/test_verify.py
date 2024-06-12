from src.verify2 import foundNumber

def test_found()->None:
    assert foundNumber(3) == True
    assert foundNumber(12) == False
    assert foundNumber(8) == False
    assert foundNumber(1) == True
    assert foundNumber(13) == True