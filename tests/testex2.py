import src.ex2 as ex2
import pytest


def testex2()->None:
    assert ex2.func(1) is "Monday"
    assert ex2.func(2) is "Tuesday"
    assert ex2.func(3) is "Wednesday"
    assert ex2.func(4) is "Thursday"
    assert ex2.func(5) is "Friday"
    assert ex2.func(6) is "Saturday"
    assert ex2.func(7) is "Sunday"
