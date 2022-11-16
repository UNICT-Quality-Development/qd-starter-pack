from src.verify import verify, list_numbers

def test_verify() -> None:
    assert verify(list_numbers, '4') == ""
    assert verify(list_numbers, '14') == " not"