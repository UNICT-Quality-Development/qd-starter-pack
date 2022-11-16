from typing import List
import pytest
from pytest_mock import MockerFixture
import src.ex1 as ex1




def test_ex1()->None:

    days = [
        "ERROR!",
        "Monday",
        "Thuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        ]

    i=0
    for day in days:
        assert ex1.get_day_of_week(i) == day
        i+=1 