from src.verify import verify

def test_verify() -> None:
    list_numbers = ('1','2','3','4','5','6','7','8','9','10')
    assert verify(list_numbers, '4') == ""
    assert verify(list_numbers, '14') == " not"
