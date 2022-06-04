from src import random_number
from pytest_mock import MockerFixture

def test_get_random_number(mocker: MockerFixture) -> None:
    mocker.patch.object(random_number, 'randint', return_value=0)
    spy = mocker.spy(random_number, 'randint')

    assert random_number.get_random_number(100) == 0
    assert random_number.get_random_number() == 0
    assert spy.spy_return == 0
    assert spy.call_count == 2