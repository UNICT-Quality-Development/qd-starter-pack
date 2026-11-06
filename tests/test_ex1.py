from pytest_mock import MockerFixture

import src.ex1 as ex1



def test_monday() -> None:
    # arrange
    week = 1

    # act
    result = ex1.get_weekday(week)

    # assert
    assert result == "Monday"
