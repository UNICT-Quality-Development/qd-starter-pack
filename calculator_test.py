from calculator import sum,diff,mul,div

def test_sum()-> None:
    assert sum(2,5)== 7
    assert sum(2,1.5)==3.5

def test_diff()->None:
    assert diff(8,2)==6
    assert diff(2,4)==-2

def test_mul()->None:
    assert mul(2,0)==0
    assert mul(3,4)==12

def test_div()->None:
    assert div(5,10)==0.5
    assert div(10,5)==2
    assert div(3,1)==3

