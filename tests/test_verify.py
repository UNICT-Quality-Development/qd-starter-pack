from src.verify import check
from src.verify import main
from pytest_mock import MockerFixture

def test_verify():
    N = (3, 4, 5, 1, 2, 3, 4, 9, 13, 0)
    assert check(N, 4) == True
    assert check(N, 10) == False

def test_main(mocker: MockerFixture):
    N = (3, 4, 5, 1, 2, 3, 4, 9, 13, 0)
    mock_verify_return = True
    mocker.patch(__name__ + '.check', return_value = mock_verify_return)

    res1 = main(N, 4)
    res2 = main(N, 10)

    assert res1 == "The number 4 is present in the array"
    assert res2 == "The number 10 is not present in the array"