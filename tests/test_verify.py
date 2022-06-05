from src.verify import isThere

def test_verify() -> None:
    arr = [3,4,5,1,2,3,4,9,13,0]
    assert isThere(arr,3,len(arr)) is True
    assert isThere(arr,20,len(arr)) is False
    assert isThere(arr,4,len(arr)) is True
    assert isThere(arr,35,len(arr)) is False
    