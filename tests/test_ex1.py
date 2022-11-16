from src.ex1 import days_of_week

def test_days_of_week() -> None:
    assert days_of_week("1") == "Monday"
    assert days_of_week("2") == "Tuesday"
    assert days_of_week("3") == "Wednesday"
    assert days_of_week("4") == "Thursday"
    assert days_of_week("5") == "Friday"
    assert days_of_week("6") == "Saturday"
    assert days_of_week("7") == "Sunday"
    assert days_of_week("250") == "Invalid input! Please enter week number between 1-7"

test_days_of_week()

