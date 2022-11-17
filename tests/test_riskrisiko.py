from pytest_mock import MockerFixture

from src.riskrisiko import random, throwing_dice, tuple_dices


def test_throwing_dice_1(mocker: MockerFixture) -> None:
    mock_random_return = 0
    mocker.patch.object(random,"randint",return_value=mock_random_return)
    spy= mocker.spy(random,"randint")
    
    res = throwing_dice()
    
    assert res == 0
    assert spy.spy_return == mock_random_return
    spy.assert_called_once_with(1,6)
    
 
def test_throwing_dice_2(mocker: MockerFixture) -> None:
     mock_random_return = 7
     mocker.patch.object(random,"randint",return_value=mock_random_return)
     spy= mocker.spy(random,"randint")
    
     res = throwing_dice()
    
    
     assert res == 7
     assert spy.call_count == 1
     assert spy.spy_return == mock_random_return
     
def test_tuple_dices_1(mocker: MockerFixture) -> None:
    mock_random_return = 0
    mocker.patch.object(random,"randint",return_value=mock_random_return)
    spy = mocker.spy(random,"randint")
    
    res = tuple_dices("name")
    
    assert res == [0,0,0]
    assert spy.call_count == 3
    assert spy.spy_return == mock_random_return
    