from src.verify import is_num_present

def test_is_num_present() -> None:
    assert is_num_present(1)
    assert not is_num_present(60)
    assert is_num_present(90)
    assert not is_num_present(1300)