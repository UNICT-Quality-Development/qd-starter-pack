from src.verify import is_num_present

def test_present() -> None:
    assert is_num_present(1) == True
    assert is_num_present(60) == False
    assert is_num_present(90) == True
    assert is_num_present(1300) == False