from pytest_mock import MockerFixture

from src.random_number import generate_random_number


def test_generate_random_number_is_within_default_range() -> None:
    for _ in range(100):
        assert 1 <= generate_random_number() <= 10


def test_generate_random_number_is_within_custom_range() -> None:
    for _ in range(100):
        assert 50 <= generate_random_number(50, 60) <= 60


def test_generate_random_number_with_single_value_range() -> None:
    assert generate_random_number(7, 7) == 7


def test_generate_random_number_returns_value_from_random(
    mocker: MockerFixture,
) -> None:
    randint = mocker.patch("src.random_number.random.randint", return_value=4)

    assert generate_random_number() == 4
    randint.assert_called_once_with(1, 10)
