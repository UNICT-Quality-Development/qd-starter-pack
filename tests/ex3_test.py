import sys
from pytest_mock import MockerFixture
from src import ex3


def test_main(mocker: MockerFixture) -> None:
    # arrange
    inputs = [
        "BarackObama",
        "SandroPertini",
        "NelsonMandela",
        "MahatmaGandhi",
        "DonaldKnuth",
        "DennisRitchie",
        "InvalidName",
    ]
    expected_outputs = [
        "44th president of the United States",
        "Former President of the Italian Republic",
        "Former President of South Africa",
        "Bapu",
        "Creator of LaTeX",
        "Creator of C",
        "Invalid input! Please enter a good name!",
    ]
    spy = mocker.spy(ex3, "main")

    # act
    actual_outputs = []
    for name in inputs:
        mocker.patch.object(sys, "argv", ["ex3.py", name])
        actual_outputs.append(ex3.main())

    # assert
    assert actual_outputs == expected_outputs
    assert spy.call_count == 7
    assert spy.spy_return == expected_outputs[-1]
