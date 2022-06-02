import pytest
from pytest_mock import MockerFixture
from src.risk_risiko import risiko
from src import risk_risiko


def test_risiko(mocker: MockerFixture) -> None:
    #act
    ret = risiko()

    #assert
    assert bool(ret) is True