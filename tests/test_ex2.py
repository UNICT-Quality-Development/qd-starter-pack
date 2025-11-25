from pytest_mock import MockerFixture
from src import ex2

def test_week_number_1(mocker: MockerFixture) -> None:

    #arrange 
    mock_number_return = '1'
    mocker.patch.object(ex2, "input", return_value=mock_number_return)

    #act
    res = ex2.week_number()

    #assert
    assert res == 'Monday'
    assert type(res) is str

def test_week_number_2(mocker: MockerFixture) -> None:

    #arrange 
    mock_number_return = '9'
    mocker.patch.object(ex2, "input", return_value=mock_number_return)

    #act
    res = ex2.week_number()

    #assert
    assert res == ''
    assert type(res) is str
