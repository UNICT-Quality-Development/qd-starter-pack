import src.convert_to_binary as cbt
import pytest
from pytest_mock import MockerFixture

@pytest.mark.parametrize("input,expected,call_counter", [(10,"1010",1), (2.0, "ERRORE",0)])
def test_convert_to_binary(mocker: MockerFixture, input, expected, call_counter) -> None:
    mock_value = "1010"
    mocker.patch.object(cbt, "bin", return_value = mock_value)
    spy = mocker.spy(cbt, "bin")
    
    res= cbt.convert_to_binary(input)
   
    assert res == expected
    assert spy.call_count == call_counter
