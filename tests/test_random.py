from src.random_number import generate
from pytest_mock import MockerFixture
from src import random_number

def test_random(mocker: MockerFixture) -> None:
    # arrange
    mock_random_return = 4
    mocker.patch.object(random_number, "generate", return_value=mock_random_return)
    spy=mocker.spy(random_number,"generate")
    
    # act
    res = random_number.generate()

    # assert
    assert res <= 10 and res >= 1
    assert spy.call_count == 1
    assert spy.spy_return == mock_random_return
