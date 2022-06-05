from src.ex2 import day_of_week

def test_day_of_week() -> None:
    assert day_of_week(1) == "Monday"
    assert day_of_week(2) == "Tuesday"
    assert day_of_week(3) == "Wednesday"
    assert day_of_week(4) == "Thursday"
    assert day_of_week(5) == "Friday"
    assert day_of_week(6) == "Saturday"
    assert day_of_week(7) == "Sunday"
    assert day_of_week(8) == "Invalid input! Please enter week number between 1-7."
    