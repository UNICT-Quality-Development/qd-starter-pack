from calendar import week
from src.ex2 import week_list
import pytest
def test_week() -> None:
    assert week_list(1) == "Monday"
    assert week_list(5) == "Friday"
    assert week_list(7) == "Sunday"
    assert week_list(99) == ""