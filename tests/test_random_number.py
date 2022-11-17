from pytest_mock import MockerFixture
from src import random_number


def test_random_number(mocker: MockerFixture) -> None:
    # arrange
    mocker_return_value = 300
    mocker.patch.object(random_number, "random_gen",
                        return_value=mocker_return_value)
    spy = mocker.spy(random_number, "random_gen")

    # act
    random_number.random_gen()

    # assert

    assert spy.call_count == 1
    assert 1 <= spy.spy_return <= 1000
