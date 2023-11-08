from src.verify import verify

def test_verify() -> None:
    assert verify([1,2,3], 2) == True
    assert verify([1,2,3], 4) == False
