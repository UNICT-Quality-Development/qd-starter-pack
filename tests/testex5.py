import src.ex5 
import pytest
from pytest_mock import MockerFixture

def testex5(mocker : MockerFixture):
    mocker.patch.object(ex5,"random",return_value = 10)

    assert src.ex5.ex5() == 10