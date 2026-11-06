from pytest_mock import MockerFixture
import example


def test_a_1(mocker: MockerFixture) -> None:
    mock_random_return = 0.4
    mocker.patch.object(example, "random", return_value=mock_random_return)
    spy = mocker.spy(example, "random")

    res = example.a()

    assert res is False
    assert spy.call_count == 1
    assert spy.spy_return == mock_random_return


def test_a_2(mocker: MockerFixture) -> None:
    mock_random_return = 0.6
    mocker.patch.object(example, "random", return_value=mock_random_return)
    spy = mocker.spy(example, "random")

    res = example.a()

    assert res is True
    assert spy.call_count == 1
    assert spy.spy_return == mock_random_return


