from typing import List
import pytest
from pytest_mock import MockerFixture
import src.ex1 as ex1

def test_ex1() -> None:

    days_to_test = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    i = 1
    for day in days_to_test:
        assert ex1.get_week_day(i) == day
        i += 1
