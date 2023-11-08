import src.ex5 as ex5
import pytest
from pytest_mock import MockerFixture



def testex5(mocker : MockerFixture)->None:
    mocker.patch.object(ex5,"random",return_value = 10)

    assert ex5.ex5() == 10