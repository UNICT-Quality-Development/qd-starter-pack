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
    actual_outputs = [ex3.main(name) for name in inputs]

    # assert
    assert actual_outputs == expected_outputs
    assert spy.call_count == 7
    assert [call.args[0] for call in spy.call_args_list] == inputs