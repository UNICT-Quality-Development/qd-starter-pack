from src.verify import is_num_present

def test_is_num_present() -> None:
    list_num_present = [1.00, 90.00, 14.00, 18.25, 19.15, 89.00]
    assert is_num_present(1, list_num_present)
    assert not is_num_present(60, list_num_present)
    assert is_num_present(90, list_num_present)
    assert not is_num_present(1300, list_num_present)
