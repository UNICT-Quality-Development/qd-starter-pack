from src.is_element_in_list import is_element_in_list

def test_is_element_in_list() -> None:
    assert is_element_in_list([1,2,3], 2) == True
    assert is_element_in_list([1,2,3], 4) == False
