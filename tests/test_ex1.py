from src.ex1 import days

def test_days() -> None:
    assert days(1) == "Monday"
    assert days(2) == "Tuesday"
    assert days(3) == "Wednesday"
    assert days(4) == "Thursday"
    assert days(5) == "Friday"
    assert days(6) == "Saturday"
    assert days(7) == "Sunday"
    assert days(8) == "Wrong number"
    assert type(days(6)) is str