import src.convert_to_binary as cbt
from pytest_mock import MockerFixture

def test_convert_to_binary(mocker: MockerFixture) -> None:
    mock_value = "1010"
    mocker.patch.object(cbt, "bin", return_value = mock_value)
    spy = mocker.spy(cbt, "bin")
    
    res_1 = cbt.convert_to_binary(10)
    res_2 = cbt.convert_to_binary(2.0)

    assert res_1 == mock_value
    assert res_2 == "ERRORE"
    assert spy.call_count == 1
