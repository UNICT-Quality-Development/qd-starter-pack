from pytest_mock import MockerFixture
import src.ex3


def test_get_description():
    # Arrange
    names = ['BarackObama','SandroPertini','NelsonMandela','MahatmaGandhi','DonaldKnuth','DennisRitchie']
    
    # Assert
    for name in names:
        assert src.ex3.get_description(name) == src.ex3.BIOS[name]
    assert src.ex3.get_description('FakeName') == 'Invalid input! Please enter a good name!'


def test_get_name(mocker: MockerFixture):
    # Arrange
    moker_input_return = 'BarackObama'
    mocker.patch.object(src.ex3, 'input', return_value=moker_input_return)
    spy = mocker.spy(src.ex3, 'input')

    # Act
    res = src.ex3.get_name()

    # Assert
    assert res == 'BarackObama'
    assert spy.call_count == 1
    assert spy.spy_return == moker_input_return
