from src.verify import f

k = [0,1,2,3,4,5,6]

def test_verify()->None:
    assert f(k,4) is True
    assert f(k,10) is False
