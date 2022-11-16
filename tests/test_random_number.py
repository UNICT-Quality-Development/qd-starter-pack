from src.random_number import random, random_number as rn

def test_random_number(mocker) -> None:
    # arrange
    mocker.patch.object(random, 'random', return_value = 0.4)
    spy = mocker.spy(random, 'random')

    # act
    result = rn()

    # assert
    assert result == 4
    assert spy.call_count == 1
