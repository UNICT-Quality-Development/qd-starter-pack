from src.ex2 import get_day

def test_get_day()-> None:
    assert get_day(1) == "Monday"
    assert get_day(2) == "Tuesday"
    assert get_day(3) == "Wednesday"
    assert get_day(4) == "Thursday"
    assert get_day(5) == "Friday"
    assert get_day(6) == "Saturday"
    assert get_day(7) == "Sunday"
    assert get_day(2666) == "Invalid input! Please enter week number between 1-7."
    assert type(get_day(1)) is str

test_get_day()
