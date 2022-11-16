from src.riskrisiko import throwing_dice, random
from pytest_mock import MockerFixture




def test_throwing_dice_1(mocker: MockerFixture) -> None:
    mock_random_return = 0
    mocker.patch.object(random,"randint",return_value=mock_random_return)
    spy= mocker.spy(random,"randint")
    
    res = throwing_dice()
    
    assert res == 0
    assert spy.call_count == 1
    assert spy.spy_return == mock_random_return
    
 
def test_throwing_dice_2(mocker: MockerFixture) -> None:
     mock_random_return = 7
     mocker.patch.object(random,"randint",return_value=mock_random_return)
     spy= mocker.spy(random,"randint")
    
     res = throwing_dice()
    
     assert res == 7
     assert spy.call_count == 1
     assert spy.spy_return == mock_random_return
    
def test_throwing_dice_3(mocker: MockerFixture) -> None:
     mock_a_return = True
     mocker.patch(__name__+'randint',return_value=mock_a_return)
     spy = mocker.spy(random,"randint")
    
     res = throwing_dice()
    
     assert res == [1,2,3,4,5,6]
     assert spy.call_count == 7
     assert spy.spy_return == mock_a_return

    
# if __name__  == "__main__":
#     a_test_throwing_dice_1()
#     a_test_throwing_dice_2()
#     b_test_throwing_dice_1()
