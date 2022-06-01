from pytest_mock import MockerFixture
import src.ex3


def test_get_description():
    # Assert
    assert src.ex3.get_description('BarackObama') == src.ex3.BIOS['BarackObama']
    assert src.ex3.get_description('SandroPertini') == src.ex3.BIOS['SandroPertini']
    assert src.ex3.get_description('NelsonMandela') == src.ex3.BIOS['NelsonMandela']
    assert src.ex3.get_description('MahatmaGandi') == src.ex3.BIOS['MahatmaGandi']
    assert src.ex3.get_description('DonaldKnuth') == src.ex3.BIOS['DonaldKnuth']
    assert src.ex3.get_description('DennisRitchie') == src.ex3.BIOS['DennisRitchie']
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
