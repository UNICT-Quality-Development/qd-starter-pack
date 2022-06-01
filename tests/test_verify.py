from src.verify import verify

def test_verify() -> None:
    assert verify(3) == True
    assert verify(6) == False
    assert verify(1.5) == False
