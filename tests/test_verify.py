from src.verify import is_there

def test_verify() -> None:
    arr = [3,4,5,1,2,3,4,9,13,0]
    assert is_there(arr,3,len(arr))
    assert is_there(arr,20,len(arr)) is False
    assert is_there(arr,4,len(arr))
    assert is_there(arr,35,len(arr)) is False
    