from pytest_mock import MockerFixture
import src.binary_converter as bc

def test_64(mocker: MockerFixture) -> None:    
    res = bc.converter(64)
    assert res == "1000000"