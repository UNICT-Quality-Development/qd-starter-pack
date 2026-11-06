from pytest_mock import MockerFixture
import src.random_number as random_module
from src.random_number import random_number


def test_random_number_mocked(mocker: MockerFixture) -> None:
    mock_randint_return = 42
    mocker.patch.object(
        random_module.random, "randint", return_value=mock_randint_return
    )
    spy = mocker.spy(random_module.random, "randint")

    res = random_number()

    assert res == 42
    assert spy.call_count == 1
    assert spy.spy_return == mock_randint_return


def test_random_number_range_and_type() -> None:
    res = random_number()

    assert isinstance(res, int)
    assert 1 <= res <= 100
    