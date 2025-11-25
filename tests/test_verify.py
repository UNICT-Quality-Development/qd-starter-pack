from src.verify import search_value
from src.verify import user_insert

def test_search_value() -> None:
    assert search_value(3) == True
    assert search_value(10) == False
    
def test_user_insert() -> None:
    assert user_insert("Inserisci: ") == int
