from pytest_mock import MockerFixture

import src.verify as verify


def test_number_is_present(mocker: MockerFixture) -> None:
    # arrange
    mock_numbers = [1, 2, 3]
    mocker.patch.object(verify, "NUMBERS", mock_numbers)

    # act
    result = verify.is_number_present(2)

    # assert
    assert result is True


def test_number_is_not_present(mocker: MockerFixture) -> None:
    # arrange
    mock_numbers = [1, 2, 3]
    mocker.patch.object(verify, "NUMBERS", mock_numbers)

    # act
    result = verify.is_number_present(4)

    # assert
    assert result is False


def test_main_with_present_number(mocker: MockerFixture) -> None:
    # arrange
    mocker.patch("builtins.input", return_value="3")
    mock_print = mocker.patch("builtins.print")
    spy = mocker.spy(verify, "is_number_present")

    # act
    verify.main()

    # assert
    assert spy.call_count == 1
    assert spy.spy_return is True
    mock_print.assert_called_once_with(
        "The number 3 is present in the array."
    )


def test_main_with_invalid_input(mocker: MockerFixture) -> None:
    # arrange
    mocker.patch("builtins.input", return_value="hello")
    mock_print = mocker.patch("builtins.print")
    spy = mocker.spy(verify, "is_number_present")

    # act
    verify.main()

    # assert
    assert spy.call_count == 0
    mock_print.assert_called_once_with(
        "Invalid input! Please enter an integer."
    )
