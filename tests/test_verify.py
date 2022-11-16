import src.verify
from src.verify import check
from src.verify import main
from pytest_mock import MockerFixture

N = (3, 4, 5, 1, 2, 3, 4, 9, 13, 0)

def test_verify():
    assert check(N, 4)
    assert check(N, 10) == False

def test_main_a(mocker: MockerFixture):
    mock_verify_return = True
    mocker.patch(__name__ + '.check', return_value = mock_verify_return)
    spy = mocker.spy(src.verify, "check")
    
    res = main(N, 4)

    assert res == "The number 4 is present in the array"
    assert spy.call_count == 1
    assert spy.spy_return == mock_verify_return

def test_main_b(mocker: MockerFixture):
    mock_verify_return = False
    mocker.patch(__name__ + '.check', return_value = mock_verify_return)
    spy = mocker.spy(src.verify, "check")

    res = main(N, 10)

    assert res == "The number 10 is not present in the array"
    assert spy.call_count == 1
    assert spy.spy_return == mock_verify_return