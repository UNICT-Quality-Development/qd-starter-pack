from src.verify import search_value
from src import verify

from pytest_mock import MockerFixture

MOCKED_INTEGER_INPUT = 123

def test_search_value() -> None:
    assert search_value(3) is True
    assert search_value(10) is False

def test_user_insert(mocker: MockerFixture) -> None:

    mock_random_return = 43

    mocker.patch.object(verify, "input", return_value=mock_random_return)
    spy = mocker.spy(verify, "input")

    res = verify.user_insert("Inserisci: ")

    assert res is mock_random_return
    assert spy.call_count == 1
    assert spy.spy_return == mock_random_return
