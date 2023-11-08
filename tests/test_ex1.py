from src.ex1 import get_week_day

def test_ex1() -> None:
    assert get_week_day(0) == ""
    assert get_week_day(1) == "Monday"
    assert get_week_day(2) == "Tuesday"
    assert get_week_day(8) == ""
    assert get_week_day(4) == "Thursday"
    assert get_week_day(7) == "Sunday"
    assert get_week_day(5) == "Friday"
    assert get_week_day(32) == ""
    assert get_week_day(3) == "Wednesday"
