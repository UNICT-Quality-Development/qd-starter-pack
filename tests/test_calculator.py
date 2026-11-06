from src.calculator import sum, sub, multiple, divide,calculator
from pytest_mock import MockerFixture
def test_sum() -> None:
    assert sum(2,11) == 13
    assert sum(0.12,0.35) == 0.47
    assert type(sum(2,9)) is float
    assert type(sum(0.12,0.35)) is float

def test_sub() -> None:
    assert sub(11,2) == 9
    assert sub(0.47,0.35) == 0.12
    assert type(sub(11,2)) is float
    assert type(sub(0.47,0.35)) is float

def test_multiple() -> None:
    assert multiple(4,5) == 20
    assert multiple(2,0.35) == 0.7
    assert type(multiple(4,5)) is float
    assert type(multiple(2,0.35)) is float

def test_divide() -> None:
    assert divide(10,2) == 5
    assert divide(1,2) == 0.5
    assert type(divide(10,2)) is float
    assert type(divide(1,2)) is float


def test_calculator(mocker: MockerFixture) -> None:
    #SUM UNIT TEST

    #arrange
    mock_sum_return = 13
    mock_sum = mocker.patch("src.calculator.sum", return_value=mock_sum_return)

    #act
    res_sum=calculator("+",2,11)

    #assert 
    assert res_sum == mock_sum_return
    mock_sum.assert_called_once_with(2, 11)    

    #SUB UNIT TEST
    #arrange
    mock_sub_return = 9
    mock_sub = mocker.patch("src.calculator.sub", return_value=mock_sub_return)

    #act
    res_sub=calculator("-",11,2)

    #assert 
    assert res_sub == mock_sub_return
    mock_sub.assert_called_once_with(11,2)    

    #multiple UNIT TEST
    mock_multiple_return = 20
    mock_multiple = mocker.patch("src.calculator.multiple", return_value=mock_multiple_return)

    #act
    res_multiple=calculator("*",4,5)

    #assert 
    assert res_multiple == mock_multiple_return
    mock_multiple.assert_called_once_with(4, 5)    
    
    #DIVIDE UNIT TEST
    #arrange
    mock_divide_return = 2
    mock_divide = mocker.patch("src.calculator.divide", return_value=mock_divide_return)

    #act
    res_divide=calculator("/",10,5)

    #assert 
    assert res_divide == mock_divide_return
    mock_divide.assert_called_once_with(10, 5)        