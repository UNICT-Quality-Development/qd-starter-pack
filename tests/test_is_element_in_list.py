from src.is_element_in_list import is_element_in_list
import pytest

@pytest.mark.parametrize("input_1", [[1, 2, 3]])
@pytest.mark.parametrize("input_2, expected", [(2, True), (4, False)])
def test_is_element_in_list(input_1:list, input_2:int, expected:bool) -> None:
    assert is_element_in_list(input_1, input_2) == expected
