from pytest_mock import MockerFixture

from src import random_number


def test_generate_random_number(mocker: MockerFixture) -> None:
    mocker = mocker.patch("random.randint", return_value=42)

    random_num = random_number.generate_random_number()

    mocker.assert_called_once()
    assert random_num == 42
